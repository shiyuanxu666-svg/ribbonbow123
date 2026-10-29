#!/usr/bin/env python3
"""Single validation pass for RB article #324 (PM, 2026-10-29) and all index updates."""
import re, os, json, html as html_mod, glob
import xml.etree.ElementTree as ET

WORK = "/workspace/ribbonbow123"
ART324_FILE = ("blog-ribbon-oem-outdoor-apparel-trim-weatherproof-uv-cold-flex-abrasion-"
               "sun-rain-salt-performance-private-label-buyers-guide-2026-10-29-pm.html")

ok = True
def check(cond, msg):
    global ok
    print(("  [PASS] " if cond else "  [FAIL] ") + msg)
    if not cond:
        ok = False

print(f"=== {ART324_FILE} ===")
p = os.path.join(WORK, ART324_FILE)
if not os.path.exists(p):
    check(False, "file exists")
else:
    h = open(p, encoding="utf-8").read()
    check(h.startswith("<!DOCTYPE html>"), "DOCTYPE present")
    for m in ["<title>", 'name="description"', 'name="keywords"', 'name="robots"',
              'rel="canonical"', 'property="og:title"', 'property="og:description"',
              'property="og:type"', 'property="og:image"', 'property="og:url"',
              'property="article:published_time"', 'property="article:modified_time"',
              'name="twitter:card"', 'name="twitter:title"']:
        check(m in h, f"meta {m}")
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
    check("BreadcrumbList" in types, "BreadcrumbList schema")
    check("Frequently Asked Questions" in h, "visible FAQ heading")
    faq_h3 = len(re.findall(r'<h3>', h.split("class=\"faq\"")[1])) if 'class="faq"' in h else 0
    check(5 <= faq_h3 <= 8, f"FAQ count 5-8 (found {faq_h3})")
    for b in blocks:
        d = json.loads(b)
        if d.get("@type") == "FAQPage":
            check(5 <= len(d["mainEntity"]) <= 8, f"FAQPage mainEntity 5-8 ({len(d['mainEntity'])})")
    body = re.sub(r'<script.*?</script>', '', h, flags=re.S)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.S)
    text = html_mod.unescape(re.sub(r'<[^>]+>', ' ', body))
    words = len(text.split())
    check(words >= 1200, f"word count >= 1200 (found {words})")
    check("since 2004" in h or "in Xiamen since 2004" in h, "uses 'since 2004'")
    check("established in 2004" not in h and "founded in 2004" not in h, "no conflicting founding-year phrasing")
    check("Module" not in h, "no 'Module' architecture spam")
    check(h.count("<h1>") == 1, f"exactly one H1 (found {h.count('<h1>')})")
    check(h.rstrip().endswith("</html>"), "file not truncated")
    check("XXX" not in h, "no XXX placeholder")

print("\n=== blog.html ===")
b = open(os.path.join(WORK, "blog.html"), encoding="utf-8").read()
check(b.count(ART324_FILE) == 1, f"appears exactly once ({b.count(ART324_FILE)})")

print("\n=== en-blog.html ===")
e = open(os.path.join(WORK, "en-blog.html"), encoding="utf-8").read()
# the card template legitimately wraps the URL twice (outer <a href> + inner <h3><a href>)
check(e.count(ART324_FILE) >= 1, f"linked ({e.count(ART324_FILE)} href refs)")
i = e.find(ART324_FILE)
check(i != -1, "new card present in en-blog.html")
# the new card must sit inside the blog-grid block, and be structurally balanced
gi = e.rfind('<div class="blog-grid"')
check(gi != -1 and gi < i, "new card inserted inside the blog-grid block")
seg = e[i:i + 2500]
check(seg.count("<div") == seg.count("</div>"), "new card div tags balanced")
check(seg.count("<a ") == seg.count("</a>"), "new card anchor tags balanced")

print("\n=== index.html ===")
i = open(os.path.join(WORK, "index.html"), encoding="utf-8").read()
check(i.count(ART324_FILE) == 1, f"appears exactly once ({i.count(ART324_FILE)})")
check(i.count("</body>") == 1, "index.html body not corrupted")

print("\n=== sitemap.xml ===")
sp = os.path.join(WORK, "sitemap.xml")
s = open(sp, encoding="utf-8").read()
ET.fromstring(s)
locs = re.findall(r"<loc>(.*?)</loc>", s)
print(f"  total locs: {len(locs)}")
dups = {x for x in locs if locs.count(x) > 1}
check(not dups, f"0 duplicate locs (dups: {list(dups)[:3]})")
check(f"https://ribbonbow123.com/{ART324_FILE}" in locs, "sitemap has article")
check(s.count("</urlset>") == 1, "sitemap single urlset")
files = {os.path.basename(x) for x in glob.glob(os.path.join(WORK, "blog-*.html"))}
slugs = {l.rsplit("/", 1)[-1] for l in locs}
missing = files - slugs
# The pre-existing orphan backlog (~239 files on disk not in sitemap) is a known,
# already-recorded issue awaiting boss approval for batch backfill. This gate must
# confirm that THIS article is present and that the orphan count did not grow.
PRE_EXISTING_ORPHANS = 239
print(f"  orphan blog files on disk not in sitemap: {len(missing)} (pre-existing baseline {PRE_EXISTING_ORPHANS})")
check(len(missing) <= PRE_EXISTING_ORPHANS,
      f"orphan count did not grow beyond baseline ({len(missing)} <= {PRE_EXISTING_ORPHANS})")
check(ART324_FILE not in missing, "this article IS in the sitemap")
fut = re.findall(r"<lastmod>(.*?)</lastmod>", s)
future = [x for x in fut if x > "2026-10-29"]
check(not future, f"0 future lastmod ({future[:3]})")

print("\n=== RESULT: " + ("ALL CHECKS PASSED" if ok else "FAILURES PRESENT") + " ===")
raise SystemExit(0 if ok else 1)
