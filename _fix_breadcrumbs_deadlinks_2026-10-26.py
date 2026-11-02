#!/usr/bin/env python3
"""
Fix pass for ribbonbow123 (2026-10-26 audit):
  A) add missing BreadcrumbList JSON-LD to real pages that lack it
  B) remove dead internal hrefs (links to files that no longer exist) from
     real indexable pages — keeping the anchor text/label but dropping the
     broken <a href> so crawlers/users don't hit 404s.
"""
import re
import os
import shutil

ROOT = "/workspace/ribbonbow123"
os.chdir(ROOT)

sm = open("sitemap.xml", encoding="utf-8").read()
locs = [os.path.basename(m.group(1).rstrip("/")) for m in re.finditer(r"<loc>([^<]+)</loc>", sm)]
real = [n for n in locs if n and os.path.isfile(n)]


def has_breadcrumb(h):
    return "BreadcrumbList" in h


def make_breadcrumb(name, h):
    """Insert a BreadcrumbList JSON-LD graph entry if missing."""
    # find existing ld+json blocks and their @graph
    if "BreadcrumbList" in h:
        return h
    # derive a readable label from the filename
    stem = re.sub(r"\.html$", "", name)
    pretty = re.sub(r"-b2b-[a-z0-9-]*$", "", stem)
    pretty = pretty.replace("blog-", "").replace("blog-oem-", "").replace("-", " ").strip()
    pretty = re.sub(r"\s+", " ", pretty)
    if not pretty:
        pretty = "Home"
    pretty = pretty[:1].upper() + pretty[1:]
    crumb = {
        "@type": "BreadcrumbList",
        "@id": "https://ribbonbow123.com/%s#breadcrumb" % name,
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home",
             "item": "https://ribbonbow123.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog",
             "item": "https://ribbonbow123.com/blog.html"},
            {"@type": "ListItem", "position": 3, "name": pretty,
             "item": "https://ribbonbow123.com/%s" % name},
        ],
    }
    block = '<script type="application/ld+json">%s</script>' % json_dumps(crumb)
    # insert right before </head>
    if "</head>" in h:
        return h.replace("</head>", "  " + block + "\n</head>", 1)
    return h


def json_dumps(obj):
    import json
    return json.dumps(obj, ensure_ascii=False, indent=2)


# ---------- A) breadcrumbs ----------
fixed_bc = []
for n in real:
    h = open(n, encoding="utf-8", errors="replace").read()
    if not has_breadcrumb(h):
        # only for complete documents
        if "<html" not in h.lower():
            continue
        nh = make_breadcrumb(n, h)
        if nh != h:
            open(n, "w", encoding="utf-8").write(nh)
            fixed_bc.append(n)
print("A) BreadcrumbList added to %d pages:" % len(fixed_bc))
for n in fixed_bc:
    print("   ", n)

# ---------- B) dead internal links ----------
def dead_hrefs(h):
    out = []
    for m in re.finditer(r'href="([^"#?]+\.html)(#[^"]*)?"', h):
        t = m.group(1)
        if t.startswith("http"):
            continue
        if not os.path.isfile(t.lstrip("/")):
            out.append(m)
    return out


changed = {}
for n in real:
    h = open(n, encoding="utf-8", errors="replace").read()
    ms = dead_hrefs(h)
    if not ms:
        continue
    nh = h
    for m in ms:
        nh = nh.replace(m.group(0), "")   # drop the broken anchor entirely
    open(n, "w", encoding="utf-8").write(nh)
    changed[n] = len(ms)

print("\nB) dead internal links removed:")
for k, v in sorted(changed.items(), key=lambda x: -x[1]):
    print(f"   {v:4d}  {k}")

# ---------- validate ----------
print("\n--- re-validation ---")
tot = 0
for n in real:
    h = open(n, encoding="utf-8", errors="replace").read()
    if "BreadcrumbList" not in h and "<html" in h.lower():
        print("  still no BreadcrumbList:", n)
    d = len(dead_hrefs(h))
    if d:
        print(f"  still {d} dead in {n}")
        tot += d
print("  total remaining dead links:", tot)
print("  sitemap lastmod future:", [m.group(1) for m in
      re.finditer(r"<lastmod>(2026-\d\d-\d\d)</lastmod>", open("sitemap.xml", encoding="utf-8").read())
      if m.group(1) > "2026-10-25"])
