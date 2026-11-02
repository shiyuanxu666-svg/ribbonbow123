#!/usr/bin/env python3
"""
Fix future-dated metadata on ribbonbow123 WITHOUT breaking live URLs.

Context (2026-10-25):
  - M300 (tech-pack) and M301 (trim-testing) were published with a '2026-10-26'
    slug and are ALREADY LIVE at that URL (HTTP 200) -> slug must stay.
  - M302 (micro-trim) was never published -> renamed to '2026-10-25' already.

For M300/M301 we only normalize the explicit date fields
(datePublished / dateModified / og published+modified time) to 2026-10-25,
leaving canonical, og:url and every filename reference untouched.
"""
import re
import shutil
import os

BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE)

TARGETS = [
    "blog-oem-ribbon-technical-specification-tech-pack-guide-14-required-fields-acceptance-criteria-ambiguity-removal-handoff-discipline-b2b-brand-procurement-2026-10-26-am.html",
    "blog-ribbon-trim-performance-testing-end-use-hair-accessory-gift-bow-pet-beauty-floral-9-tests-predict-field-failure-pass-fail-criteria-b2b-brand-procurement-2026-10-26-pm.html",
]

DATE_FIELDS = [
    ('"datePublished": "2026-10-26"', '"datePublished": "2026-10-25"'),
    ('"dateModified": "2026-10-26"', '"dateModified": "2026-10-25"'),
    ('content="2026-10-26T', 'content="2026-10-25T'),
]

for f in TARGETS:
    bak = "/tmp/%s.bak" % f
    if os.path.exists(bak):
        shutil.copy(bak, f)  # always start from the pristine original
    t = open(f, encoding="utf-8").read()
    before = t
    for a, b in DATE_FIELDS:
        t = t.replace(a, b)
    open(f, "w", encoding="utf-8").write(t)

    canonical = re.search(r'<link rel="canonical" href="([^"]*)"', t)
    ogurl = re.search(r'og:url" content="([^"]*)"', t)
    dpub = re.search(r'"datePublished": "([^"]*)"', t)
    dmod = re.search(r'"dateModified": "([^"]*)"', t)
    slug = os.path.basename(f)

    print("===", slug[:58])
    print("  canonical  :", (canonical.group(1)[-52:] if canonical else None))
    print("  canonical matches filename:", bool(canonical) and canonical.group(1).endswith(slug))
    print("  og:url matches filename    :", bool(ogurl) and ogurl.group(1).endswith(slug))
    print("  datePublished/Modified    :", dpub.group(1) if dpub else None, "/", dmod.group(1) if dmod else None)
    print("  changed from original     :", before != t)
    print()

# ---- validate sitemap + blog.html reference only live/valid slugs ----
sm = open("sitemap.xml", encoding="utf-8").read()
blog = open("blog.html", encoding="utf-8").read()

print("--- sitemap loc validation ---")
bad = 0
for m in re.finditer(r"<loc>([^<]+)</loc>", sm):
    loc = m.group(1)
    name = os.path.basename(loc)
    if not os.path.exists(name):
        print("  MISSING FILE:", name)
        bad += 1
print("  sitemap locs:", len(re.findall(r"<loc>", sm)), "| missing on disk:", bad)

print("--- blog.html href validation ---")
bad2 = 0
for m in re.finditer(r'href="([^"]+\.html)"', blog):
    h = m.group(1)
    if h.startswith("http"):
        continue
    if not os.path.exists(h):
        print("  MISSING FILE:", h)
        bad2 += 1
print("  blog hrefs:", len(re.findall(r'href="[^"]+\.html"', blog)), "| missing on disk:", bad2)

print("--- future lastmod check ---")
fut = [m.group(0) for m in re.finditer(r"<lastmod>(2026-1[12]-[0-9]{2})</lastmod>", sm)
       if m.group(1) > "2026-10-25"]
print("  future-dated lastmod entries:", len(fut), fut[:5])
