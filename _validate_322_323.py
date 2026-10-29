#!/usr/bin/env python3
"""Single validation pass for articles #322 and #323 and all index updates."""
import re, os, json, html as html_mod

WORK = "/workspace/ribbonbow123"
ART322_FILE = "blog-ribbon-oem-jewellery-watch-luxury-gift-packaging-trim-small-format-high-value-specification-private-label-buyers-guide-2026-10-29-am.html"
ART323_FILE = "blog-ribbon-oem-athletic-activewear-performance-apparel-trim-stretch-recovery-sweat-chlorine-wash-durability-branding-private-label-buyers-guide-2026-10-29-pm.html"

ok = True
def check(cond, msg):
    global ok
    print(("  [PASS] " if cond else "  [FAIL] ") + msg)
    if not cond:
        ok = False

for f in (ART322_FILE, ART323_FILE):
    p = os.path.join(WORK, f)
    print(f"\n=== {f} ===")
    if not os.path.exists(p):
        check(False, "file exists")
        continue
    h = open(p, encoding="utf-8").read()
    check(h.startswith("<!DOCTYPE html>"), "DOCTYPE present")
    for m in ["<title>", 'name="description"', 'name="keywords"', 'name="robots"',
              'rel="canonical"', 'property="og:title"', 'property="og:description"',
              'property="og:type"', 'property="og:image"', 'property="og:url"',
              'property="article:published_time"', 'property="article:modified_time"',
              'name="twitter:card"', 'name="twitter:title"']:
        check(m in h, f"meta {m}")
    # JSON-LD blocks
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    check(len(blocks) >= 3, f"has >=3 JSON-LD blocks (found {len(blocks)})")
    types = []
    for b in blocks:
        try:
            d = json.loads(b)
            types.append(d.get("@type"))
        except Exception as e:
            check(False, f"JSON-LD parses: {e}")
    check("Article" in types, "Article schema")
    check("BlogPosting" in types, "BlogPosting schema")
    check("FAQPage" in types, "FAQPage schema")
    # FAQ visible section
    check("Frequently Asked Questions" in h, "visible FAQ heading")
    faq_h3 = len(re.findall(r'<h3>', h.split("class=\"faq\"")[1])) if 'class="faq"' in h else 0
    check(5 <= faq_h3 <= 7, f"FAQ count 5-7 (found {faq_h3})")
    # FAQPage mainEntity count matches
    for b in blocks:
        d = json.loads(b)
        if d.get("@type") == "FAQPage":
            check(5 <= len(d["mainEntity"]) <= 7, f"FAQPage mainEntity 5-7 ({len(d['mainEntity'])})")
    # word count (visible text)
    body = re.sub(r'<script.*?</script>', '', h, flags=re.S)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.S)
    text = html_mod.unescape(re.sub(r'<[^>]+>', ' ', body))
    words = len(text.split())
    check(words >= 1200, f"word count >= 1200 (found {words})")
    # entity discipline
    check("since 2004" in h or "in Xiamen since 2004" in h, "uses 'since 2004'")
    check("established in 2004" not in h and "founded in 2004" not in h, "no conflicting founding-year phrasing")
    # no keyword-spam module architecture patterns
    check("Module" not in h and "module" not in h.replace("modules", ""), "no 'Module' architecture spam")

print("\n=== blog.html ===")
b = open(os.path.join(WORK, "blog.html"), encoding="utf-8").read()
for f in (ART322_FILE, ART323_FILE):
    check(b.count(f) == 1, f"{f[:50]}... appears exactly once ({b.count(f)})")
# order check: PM (#323, 13:00) before AM (#322, 08:00)
i322, i323 = b.find(ART322_FILE), b.find(ART323_FILE)
check(i323 != -1 and i322 != -1 and i323 < i322, "blog.html order: PM (#323) before AM (#322)")

print("\n=== en-blog.html ===")
e = open(os.path.join(WORK, "en-blog.html"), encoding="utf-8").read()
for f in (ART322_FILE, ART323_FILE):
    check(e.count(f) == 1, f"{f[:50]}... appears exactly once ({e.count(f)})")

print("\n=== index.html ===")
i = open(os.path.join(WORK, "index.html"), encoding="utf-8").read()
for f in (ART322_FILE, ART323_FILE):
    check(i.count(f) == 1, f"{f[:50]}... appears exactly once ({i.count(f)})")
check(i.count("</body>") == 1, "index.html body not corrupted")

print("\n=== sitemap.xml ===")
s = open(os.path.join(WORK, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", s)
print(f"  total locs: {len(locs)}")
dups = {x for x in locs if locs.count(x) > 1}
check(not dups, f"0 duplicate locs (dups: {list(dups)[:3]})")
for f in (ART322_FILE, ART323_FILE):
    check(f"https://ribbonbow123.com/{f}" in locs, f"sitemap has {f[:50]}...")
check(s.count("</urlset>") == 1, "sitemap single urlset")
# every article html file referenced in sitemap
import glob
files = {os.path.basename(x) for x in glob.glob(os.path.join(WORK, "blog-*.html"))}
slugs = {l.rsplit("/", 1)[-1] for l in locs}
missing = files - slugs
check(not missing, f"0 blog articles missing from sitemap (missing: {list(missing)[:3]})")

print("\n=== RESULT: " + ("ALL CHECKS PASSED" if ok else "FAILURES PRESENT") + " ===")
