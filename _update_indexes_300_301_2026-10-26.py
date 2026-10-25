#!/usr/bin/env python3
"""Insert article cards 300 (AM) and 301 (PM) into ribbonbow123 blog.html,
newest-first, then verify schema/meta/FAQ/sitemap once."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-26"

ARTICLES = [
    {
        "num": "301",
        "slug": ("ribbon-trim-performance-testing-end-use-hair-accessory-gift-bow-pet-beauty-floral-"
                 "9-tests-predict-field-failure-pass-fail-criteria-b2b-brand-procurement-2026-10-26-pm"),
        "title": ("Ribbon Trim Performance Testing by End-Use &mdash; 9 Tests That Predict Field Failure in Hair "
                  "Accessories, Gift Bows, Pet, Beauty and Floral (2026)"),
        "aria": "Ribbon Trim Performance Testing End-Use 2026",
        "excerpt": ("A 2026 quality guide to ribbon trim performance testing by end-use. Explains why a generic ribbon "
                    "test suite predicts little, the nine physical tests that actually predict field failure across hair "
                    "accessories, gift bows, pet products, beauty packaging and floral trim, how to write a pass/fail "
                    "criterion for each, and the specification discipline that stops the same test being run ten times "
                    "on ten versions of the same ribbon."),
        "gradient": "linear-gradient(135deg,#00695c,#26a69a)",
    },
    {
        "num": "300",
        "slug": ("oem-ribbon-technical-specification-tech-pack-guide-14-required-fields-acceptance-criteria-"
                 "ambiguity-removal-handoff-discipline-b2b-brand-procurement-2026-10-26-am"),
        "title": ("OEM Ribbon Technical Specification &amp; Tech Pack Guide &mdash; 14 Required Fields, "
                  "Acceptance Criteria and How to Remove Ambiguity (2026)"),
        "aria": "OEM Ribbon Technical Specification Tech Pack 2026",
        "excerpt": ("A 2026 procurement guide to writing an OEM ribbon technical specification and tech pack. Explains why "
                    "most ribbon disputes are specification disputes, the 14 fields every ribbon spec must contain to be "
                    "quotable and enforceable, the seven acceptance criteria that turn a description into a testable "
                    "requirement, and the handoff discipline that stops a brief being reinterpreted on the shop floor."),
        "gradient": "linear-gradient(135deg,#4527a0,#7e57c2)",
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
                  'article:published_time', '"@type": "Article"', "since 2004"]:
        assert token in ah, f"article {art['num']} missing {token}"
    assert ah.count('"@type": "Question"') >= 5, f"article {art['num']} FAQ too short"
    words = len(re.sub(r"<[^>]+>", " ", ah).split())
    assert words >= 1200, f"article {art['num']} too short: {words} words"
    print(f"  article {art['num']}: schema/meta/FAQ OK, ~{words} words")
print("All checks passed.")
