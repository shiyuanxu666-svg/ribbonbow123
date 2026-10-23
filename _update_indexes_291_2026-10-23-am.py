#!/usr/bin/env python3
"""Link ribbonbow123 article 291 (2026-10-23 AM) into blog.html and verify sitemap."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-23"

ART = {
    "num": "291",
    "slug": ("oem-private-label-ribbon-packaging-compliance-labelling-documentation-architecture-"
             "4-layer-evidence-stack-market-access-gate-regulatory-declaration-b2b-oem-2026-10-23-am"),
    "title": ("OEM &amp; Private-Label Ribbon Packaging Compliance &amp; Labelling Documentation Architecture: "
              "The 4-Layer Evidence Stack, Market-Access Gate and Regulatory-Declaration Decoder "
              "for Cross-Border Ribbon Programmes (2026)"),
    "aria": "OEM Private-Label Ribbon Packaging Compliance and Labelling Documentation Architecture 2026",
    "excerpt": ("A 2026 OEM private-label ribbon packaging compliance and labelling documentation playbook for "
                "brand procurement leads and packaging compliance engineers. Covers the 4-layer compliance "
                "evidence stack from fibre chemistry to market label, the market-access gate that blocks "
                "non-compliant ribbon from specific destinations, a 19-claim regulatory-declaration decoder, "
                "and a mill-side compliance documentation runbook."),
    "gradient": "linear-gradient(135deg,#00695c,#00897b)",
}

blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
href = f'href="blog-{ART["slug"]}.html"'

if href in blog:
    print(f"[SKIP] blog.html already links article {ART['num']}")
else:
    last_open = blog.rfind('<article class="blog-post-card"')
    if last_open == -1:
        raise SystemExit("no blog-post-card found in blog.html")
    last_close = blog.find("</article>", last_open)
    if last_close == -1:
        raise SystemExit("unterminated blog-post-card in blog.html")
    insert_at = last_close + len("</article>")

    card = f"""
  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="blog-{ART['slug']}.html" class="blog-post-thumb" style="background:{ART['gradient']};" aria-label="{ART['aria']}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="blog-{ART['slug']}.html">{ART['title']}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{ART['excerpt']}</p>
  <a class="blog-post-link" href="blog-{ART['slug']}.html">Read more &rarr;</a>
</article>"""
    blog = blog[:insert_at] + card + blog[insert_at:]
    blog_path.write_text(blog, encoding="utf-8")
    print(f"[OK] blog.html updated with article {ART['num']}")

# ---------- verify ----------
v_blog = blog_path.read_text(encoding="utf-8")
n = v_blog.count(href)
assert n >= 3, f"blog.html link count low: {n}"

sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
url = f"https://ribbonbow123.com/blog-{ART['slug']}.html"
assert url in sm, "article 291 missing from sitemap.xml"
ET.fromstring(sm)
print(f"Verification OK: article 291 linked in blog.html ({n} links) and sitemap.xml (valid XML)")

art_html = (ROOT / f"blog-{ART['slug']}.html").read_text(encoding="utf-8")
for token in ["application/ld+json", "BlogPosting", "og:title", "twitter:card", "<h1>", "rel=\"canonical\""]:
    assert token in art_html, f"missing {token}"
words = len(art_html.split())
print(f"Article 291: {len(art_html):,} bytes, ~{words} total tokens, meta/OG/JSON-LD present")