#!/usr/bin/env python3
"""Insert article card 302 into ribbonbow123 blog.html, newest-first, then verify
schema/meta/FAQ/sitemap once."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-26"

ARTICLES = [
    {
        "num": "302",
        "slug": ("ribbon-narrow-width-micro-trim-manufacturing-6mm-13mm-weave-geometry-selvedge-"
                 "specification-b2b-brand-procurement-2026-10-26-pm"),
        "title": ("Narrow-Width &amp; Micro-Trim Ribbon Manufacturing &mdash; How 6&ndash;13&nbsp;mm Trims Are Woven, "
                  "Why They Need a Different Spec from 38&nbsp;mm Gift Wrap (2026)"),
        "aria": "Narrow Width Micro Trim Ribbon Manufacturing 2026",
        "excerpt": ("A 2026 manufacturing guide to narrow-width and micro-trim ribbon. Explains what physically changes "
                    "when a ribbon narrows from 38&nbsp;mm to 6&nbsp;mm - warp density, selvedge support, tension, "
                    "weft insertion and print registration - the six specification parameters that behave differently "
                    "at narrow widths, why tolerance bands written for gift wrap cannot be copied down, and how to plan "
                    "a micro-trim programme with realistic minimums and lead times."),
        "gradient": "linear-gradient(135deg,#00695c,#26a69a)",
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
