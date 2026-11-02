#!/usr/bin/env python3
"""Insert article cards 295 (AM) and 296 (PM) into blog.html newest-first,
then verify schema/meta/FAQ/sitemap for both."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-25"

ARTICLES = [
    {
        "num": "295",
        "slug": ("oem-custom-ribbon-retail-packaging-engineering-shelf-presentation-secondary-packaging-"
                 "specification-carton-configuration-brand-owner-b2b-procurement-2026-10-25-am"),
        "title": ("OEM Custom Ribbon Retail Packaging Engineering: A Shelf-Presentation &amp; Secondary Packaging "
                  "Specification Guide for Brand Owners and Packaging Procurement Leads (2026)"),
        "aria": "OEM Custom Ribbon Retail Packaging Engineering 2026",
        "excerpt": ("A 2026 OEM custom ribbon retail packaging engineering guide for brand owners and packaging "
                    "procurement leads. Covers primary, secondary and tertiary packaging layers, the seven "
                    "pack-configuration decisions that determine shelf presentation, carton cube and landed cost, "
                    "label content and compliance marking rules, and the five production checks that catch a "
                    "packaging specification error before it reaches a container."),
        "gradient": "linear-gradient(135deg,#00695c,#00897b)",
    },
    {
        "num": "296",
        "slug": ("decoding-ribbon-certifications-oeko-tex-fsc-bsci-grs-smeta-iso-9001-scope-expiry-"
                 "verification-checklist-b2b-brand-procurement-2026-10-25-pm"),
        "title": ("Decoding Ribbon Certifications: What OEKO-TEX&reg;, FSC&reg;, BSCI, GRS, SMETA and ISO 9001 "
                  "Actually Prove &mdash; and How to Verify a Certificate Before You Order (2026)"),
        "aria": "Decoding Ribbon Certifications 2026",
        "excerpt": ("A 2026 buyer's guide to reading ribbon certifications. Sets out what OEKO-TEX, FSC, BSCI, GRS, "
                    "SMETA and ISO 9001 each actually assert, where every certificate stops and what it does not "
                    "cover, why an expired or out-of-scope certificate is worse than no certificate, the seven-point "
                    "verification sequence, and how to map credentials to the claims a brand actually makes on pack."),
        "gradient": "linear-gradient(135deg,#4527a0,#6a1b9a)",
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
  <a href="blog-{art["slug"]}.html" class="blog-post-thumb" style="background:{art["gradient"]};" aria-label="{art["aria"]}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="blog-{art["slug"]}.html">{art["title"]}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{art["excerpt"]}</p>
  <a class="blog-post-link" href="blog-{art["slug"]}.html">Read more &rarr;</a>
</article>"""
    blog = blog[:insert_at] + card + blog[insert_at:]
    print(f"[OK] blog.html updated with article {art['num']}")

blog_path.write_text(blog, encoding="utf-8")

# ---------------- verify (single pass) ----------------
v_blog = blog_path.read_text(encoding="utf-8")
for art in ARTICLES:
    n = v_blog.count(f'href="blog-{art["slug"]}.html"')
    assert n >= 3, f"article {art['num']} link count low: {n}"
    url = f"https://ribbonbow123.com/blog-{art['slug']}.html"
    assert url in (ROOT / "sitemap.xml").read_text(encoding="utf-8"), f"article {art['num']} missing from sitemap"
    print(f"  article {art['num']}: {n} links in blog.html, present in sitemap")

sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm)
locs = re.findall(r"<loc>(.*?)</loc>", sm)
dupes = {x for x in locs if locs.count(x) > 1}
assert not dupes, f"duplicate sitemap URLs: {list(dupes)[:5]}"
print(f"Verification OK: sitemap valid XML, {len(locs)} URLs, 0 duplicates")

order_ok = v_blog.find(f'blog-{ARTICLES[0]["slug"]}.html') < v_blog.find(f'blog-{ARTICLES[1]["slug"]}.html')
print(f"blog.html ordering (295 before 296): {order_ok}")

for art in ARTICLES:
    ah = (ROOT / f'blog-{art["slug"]}.html').read_text(encoding="utf-8")
    for token in ['"@type": "BlogPosting"', '"@type": "FAQPage"', "og:title", "twitter:card",
                  'rel="canonical"', 'name="description"', 'name="keywords"', 'og:image',
                  'article:published_time', '"@type": "Article"']:
        assert token in ah, f"article {art['num']} missing {token}"
    assert ah.count("<h1>") == 1, f"article {art['num']} H1 count = {ah.count('<h1>')}"
    # body word count (visible text only, excluding head/style)
    body = ah.split("</head>")[1]
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.S)
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    faq_count = ah.count('<div class="faq">')
    assert faq_count == 1
    n_faq = ah.split('<div class="faq">')[1].split("</div>")[0].count("<h3>")
    print(f"  article {art['num']}: words={words}, FAQ items={n_faq}")
    assert words >= 1200, f"article {art['num']} too short: {words}"
    assert 5 <= n_faq <= 7, f"article {art['num']} FAQ count {n_faq} out of 5-7 range"
    assert "since 2004" in ah, f"article {art['num']} missing 'since 2004' entity statement"

print("Both new articles: BlogPosting + Article + FAQPage + meta + OG + single H1 + word count confirmed")
