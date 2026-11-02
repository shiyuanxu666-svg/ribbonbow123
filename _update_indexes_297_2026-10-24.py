#!/usr/bin/env python3
"""Insert article card 297 (PM) into ribbonbow123 blog.html (newest-first position),
then verify schema/meta/FAQ/sitemap for the new article."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-24"

ARTICLES = [
    {
        "num": "297",
        "slug": ("oem-ribbon-care-labelling-wash-care-instruction-compliance-fastness-specification-decoder-"
                 "7-point-verification-checklist-b2b-brand-procurement-2026-10-24-pm"),
        "title": ("OEM Ribbon Care Labelling &amp; Wash-Care Instruction Compliance &mdash; Why the Care Regime "
                  "You Choose Decides Your Ribbon Fastness Specification (2026)"),
        "aria": "OEM Ribbon Care Labelling Compliance 2026",
        "excerpt": ("A 2026 buyer's guide to ribbon care labelling and wash-care instruction compliance. Explains how "
                    "the care regime printed on your pack becomes the specification your ribbon mill must actually "
                    "meet, the six standard care instruction categories and what each demands of a trim, the "
                    "seven-point verification sequence to run before approving care text, and the four costing "
                    "failures that appear when care instructions are written last instead of first."),
        "gradient": "linear-gradient(135deg,#00695c,#00897b)",
    },
]

blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")

for art in ARTICLES:
    href = f'href="blog-{art["slug"]}.html"'
    if href in blog:
        print(f"[SKIP] blog.html already links article {art['num']}")
        continue
    last_open = blog.rfind('<article class="blog-post-card"')
    if last_open == -1:
        raise SystemExit("no blog-post-card found in blog.html")
    last_close = blog.find("</article>", last_open)
    if last_close == -1:
        raise SystemExit("unterminated blog-post-card in blog.html")
    insert_at = last_close + len("</article>")
    card = f"""
  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="blog-{art['slug']}.html" class="blog-post-thumb" style="background:{art["gradient"]};" aria-label="{art["aria"]}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="blog-{art['slug']}.html">{art["title"]}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{art["excerpt"]}</p>
  <a class="blog-post-link" href="blog-{art["slug"]}.html">Read more &rarr;</a>
</article>"""
    blog = blog[:insert_at] + card + blog[insert_at:]
    print(f"[OK] blog.html updated with article {art['num']}")

blog_path.write_text(blog, encoding="utf-8")

# ---------------- verify (single pass) ----------------
v_blog = blog_path.read_text(encoding="utf-8")
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
for art in ARTICLES:
    n = v_blog.count(f'href="blog-{art["slug"]}.html"')
    assert n >= 3, f"article {art['num']} link count low: {n}"
    url = f"https://ribbonbow123.com/blog-{art['slug']}.html"
    assert url in sm, f"article {art['num']} missing from sitemap"
    print(f"  article {art['num']}: {n} links in blog.html, present in sitemap")

ET.fromstring(sm)
locs = re.findall(r"<loc>(.*?)</loc>", sm)
dupes = {x for x in locs if locs.count(x) > 1}
assert not dupes, f"duplicate sitemap URLs: {list(dupes)[:5]}"
print(f"Verification OK: sitemap valid XML, {len(locs)} URLs, 0 duplicates")

for art in ARTICLES:
    ah = (ROOT / f'blog-{art["slug"]}.html').read_text(encoding="utf-8")
    for token in ['"@type": "BlogPosting"', '"@type": "FAQPage"', "og:title", "twitter:card",
                  'rel="canonical"', 'name="description"', 'name="keywords"', 'og:image',
                  'article:published_time', '"@type": "Article"']:
        assert token in ah, f"article {art['num']} missing {token}"
    assert ah.count("<h1>") == 1, f"article {art['num']} H1 count = {ah.count('<h1>')}"
    body = ah.split("</head>")[1]
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.S)
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    n_faq = ah.split('<div class="faq">')[1].split("</div>")[0].count("<h3>")
    print(f"  article {art['num']}: words={words}, FAQ items={n_faq}")
    assert words >= 1200, f"article {art['num']} too short: {words}"
    assert 5 <= n_faq <= 7, f"article {art['num']} FAQ count {n_faq} out of 5-7 range"
    assert "since 2004" in ah, f"article {art['num']} missing 'since 2004' entity statement"

print("New article 297: BlogPosting + Article + FAQPage + meta + OG + single H1 + word count confirmed")
