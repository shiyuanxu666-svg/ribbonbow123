#!/usr/bin/env python3
"""
Remove dead internal links from real indexable pages, keeping HTML balanced.

Strategy: for each <a href="X.html"> whose target file does NOT exist,
remove the ENTIRE anchor element (open tag .. matching </a>), so tag counts
stay balanced. If the anchor has no matching </a> (pre-existing malformed
HTML), remove just the <a ...> open tag AND the orphan closing tag if the
next sibling structure implies it.

Also un-nest invalid nested <a> elements (an <a> inside an <a>) which are
invalid HTML5 and confuse crawlers.
"""
import re
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

sm = open("sitemap.xml", encoding="utf-8").read()
locs = [os.path.basename(m.group(1).rstrip("/")) for m in re.finditer(r"<loc>([^<]+)</loc>", sm)]
real = [n for n in locs if n and os.path.isfile(n)]


def target_exists(href):
    if href.startswith("http"):
        return True
    return os.path.isfile(href.lstrip("/").split("#")[0])


def strip_dead_anchors(h):
    """Remove whole <a ...>...</a> elements pointing to missing files."""
    out = []
    i = 0
    removed = 0
    n = len(h)
    while True:
        m = re.compile(r'<a\b([^>]*)>').search(h, i)
        if not m:
            out.append(h[i:])
            break
        out.append(h[i:m.start()])
        attrs = m.group(1)
        hm = re.search(r'href\s*=\s*"([^"]*)"', attrs)
        href = hm.group(1) if hm else ""
        # find matching </a>
        depth = 1
        j = m.end()
        while j < n:
            no = re.compile(r'<a\b[^>]*>').search(h, j)
            nc = h.find('</a>', j)
            if nc == -1:
                break
            if no and no.start() < nc:
                depth += 1
                j = no.end()
                continue
            depth -= 1
            if depth == 0:
                break
            j = nc + 4
        if depth == 0:
            end = j + 4                      # past </a>
        else:
            end = m.end()                   # orphan open tag only
        if href and not target_exists(href):
            removed += 1
            # keep any inner text? No: drop the whole element to stay valid.
            i = end
        else:
            out.append(h[m.start():end])
            i = end
    return "".join(out), removed


def unnest(h):
    """Fix invalid nested anchors: <a href=X ...> ... <a href=Y> ... </a> ... </a>
    Replace the inner anchor with a plain span preserving its content."""
    changed = 0
    for _ in range(5):
        m = re.search(r'<a\b[^>]*>(?:(?!</a>).)*?<a\b([^>]*)>', h, re.S)
        if not m:
            break
        inner_open = m.start(0)
        inner_tag = m.group(0)
        # locate inner anchor's </a>
        inner_close = h.find('</a>', m.end())
        if inner_close == -1:
            break
        inner_html = h[m.start():inner_close + 4]
        # drop inner <a ...> and its </a>
        new_inner = re.sub(r'^<a\b[^>]*>', '<span>', inner_html, count=1)
        new_inner = new_inner[:-4] + '</span>'
        h = h[:m.start()] + new_inner + h[inner_close + 4:]
        changed += 1
    return h, changed


total = {}
for n in real:
    h = open(n, encoding="utf-8", errors="replace").read()
    orig = h
    h, rem = strip_dead_anchors(h)
    if rem:
        h, un = unnest(h)
        open(n, "w", encoding="utf-8").write(h)
        total[n] = (rem, un)

print("dead anchors removed (page: anchors, un-nested):")
for k, v in sorted(total.items(), key=lambda x: -x[1][0]):
    print(f"   {v[0]:4d}  {k[:72]}")

print("\n--- validation ---")
bad = 0
for n in real:
    h = open(n, encoding="utf-8", errors="replace").read()
    a, c = len(re.findall(r"<a\b", h)), len(re.findall(r"</a>", h))
    if a != c:
        print(f"  UNBALANCED <a> {a}/{c}  {n[:70]}")
        bad += 1
print("  unbalanced files:", bad)

smt = open("sitemap.xml", encoding="utf-8").read()
tot = 0
for n in real:
    h = open(n, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r'href="([^"#?]+\.html)"', h):
        if not m.group(1).startswith("http") and not target_exists(m.group(1)):
            tot += 1
print("  remaining dead hrefs:", tot)
print("  future lastmod:", [m.group(1) for m in
      re.finditer(r"<lastmod>(2026-\d\d-\d\d)</lastmod>", smt) if m.group(1) > "2026-10-25"])
