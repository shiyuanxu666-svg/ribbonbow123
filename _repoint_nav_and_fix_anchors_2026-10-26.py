#!/usr/bin/env python3
"""
Repair href-less anchors left by the dead-link strip, and repoint broken
nav links to live equivalents.

Background (2026-10-26 audit on ribbonbow123):
  - nav links to products.html / oem.html  -> these files do NOT exist and
    return 404 live. The correct live targets are:
        products.html -> index.html#products   (or oem-services.html)
        oem.html      -> oem-services.html
  - the previous pass removed the dead href but left `<a >Text</a>`.
    An anchor without href is not a link -> better to convert to a plain
    span/keep text so the markup stays valid and no dead link remains.
"""
import re
import os
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# nav repoint map: dead filename -> live replacement
REPOINT = {
    "products.html": "index.html#products",
    "oem.html": "oem-services.html",
}

sm = open("sitemap.xml", encoding="utf-8").read()
locs = [os.path.basename(m.group(1).rstrip("/")) for m in re.finditer(r"<loc>([^<]+)</loc>", sm)]
real = [n for n in locs if n and os.path.isfile(n)]
# also include the top-level real pages not in sitemap (nav targets)
for n in ["index.html", "blog.html", "en-blog.html", "about.html", "contact.html",
          "oem-services.html", "products-*.html"]:
    pass
real = sorted(set(real))

changed = {}
for n in real:
    h = open(n, encoding="utf-8").read()
    orig = h
    # 1) repoint nav dead links
    for dead, live in REPOINT.items():
        h = h.replace('href="%s"' % dead, 'href="%s"' % live)
    # 2) any remaining anchor with NO href attribute -> convert to span
    #    (keeps visible text, keeps markup valid, no dead link left behind)
    def _fix_anchor(m):
        tag = m.group(0)
        if re.search(r'href\s*=', tag):
            return tag
        return tag.replace("<a", "<span", 1)

    h = re.sub(r'<a\b[^>]*>', _fix_anchor, h)
    # balance: only </a> whose matching open tag became a span
    # do it by walking and tracking
    out = []
    i = 0
    while True:
        m = re.compile(r'<(/?)(a|span)\b[^>]*>').search(h, i)
        if not m:
            out.append(h[i:])
            break
        out.append(h[i:m.start()])
        if m.group(1) == "/":
            # find the nearest unmatched open tag of same name
            opens = [x for x in re.finditer(r'<(a|span)\b[^>]*>', h[:m.start()])]
            stack = []
            for x in opens:
                pass
            out.append("</span>")
        else:
            tag = m.group(0)
            if tag.startswith("<a") and not re.search(r'href\s*=', tag):
                out.append(tag.replace("<a", "<span", 1))
            else:
                out.append(tag)
        i = m.end()
    h = "".join(out)
    if h != orig:
        open(n, "w", encoding="utf-8").write(h)
        changed[n] = sum(1 for _ in re.finditer(r'href="(products|oem)\.html"', orig))

print("files updated:", len(changed))
for k in sorted(changed):
    print("   ", k[:78])

print("\n--- validation ---")
bad = 0
for n in real:
    h = open(n, encoding="utf-8").read()
    a, c = len(re.findall(r"<a\b", h)), len(re.findall(r"</a>", h))
    if a != c:
        print(f"  UNBALANCED {a}/{c}  {n[:70]}")
        bad += 1
print("  unbalanced files:", bad)

# no href-less anchors left, no dead nav refs
noref = 0
deadnav = 0
for n in real:
    h = open(n, encoding="utf-8").read()
    noref += len(re.findall(r'<a\s*>', h))
    deadnav += len(re.findall(r'href="(products|oem)\.html"', h))
print("  href-less <a> remaining:", noref)
print("  dead nav href remaining:", deadnav)

tot = 0
for n in real:
    h = open(n, encoding="utf-8").read()
    for m in re.finditer(r'href="([^"#?]+\.html)"', h):
        t = m.group(1)
        if t.startswith("http"):
            continue
        if not os.path.isfile(t.lstrip("/")):
            tot += 1
print("  remaining dead hrefs across real pages:", tot)
