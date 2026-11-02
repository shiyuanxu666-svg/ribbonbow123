#!/usr/bin/env python3
"""Update blog.html + sitemap.xml for ribbonbow123 articles 282 (AM) and 283 (PM), 2026-10-21."""
from pathlib import Path

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-21"

ARTICLES = [
    {
        "num": "282",
        "slug": "ribbon-oem-8-layer-specification-pyramid-oem-private-label-sourcing-guide-2026-10-21-am",
        "title": "OEM Ribbon Sourcing Guide: The 8-Layer Specification Pyramid for Private-Label Brand Owners and Category Buyers (2026)",
        "aria": "OEM Ribbon Sourcing 8-Layer Specification Pyramid 2026",
        "excerpt": ("A 2026 OEM ribbon sourcing playbook for private-label brand owners and category buyers. "
                    "Covers the 8-layer ribbon specification pyramid - product identity, material chemistry, "
                    "physical geometry, color and appearance, print decoration, performance and compliance, "
                    "packaging and logistics, commercial governance - and how it drives comparable RFQ quotes, "
                    "first-pass sample approval and audit-ready incoming inspection."),
        "gradient": "linear-gradient(135deg,#c2185b,#7b1fa2)",
    },
    {
        "num": "283",
        "slug": "private-label-ribbon-12-signal-quality-scorecard-incoming-inspection-b2b-oem-2026-10-21-pm",
        "title": "Private-Label Ribbon Quality Control: The 12-Signal Scorecard for Incoming Inspection and Supplier Management (2026)",
        "aria": "Private Label Ribbon 12-Signal Quality Scorecard 2026",
        "excerpt": ("A 2026 private-label ribbon quality-control playbook for brand owners and QA leads. "
                    "Covers the 12-signal ribbon quality scorecard across geometric, color/print and "
                    "compliance/logistics families, with numeric thresholds, measurement methods, critical-failure "
                    "rules, a pre-agreed consequence ladder and rolling supplier scoring for QBR reviews."),
        "gradient": "linear-gradient(135deg,#00695c,#00838f)",
    },
]

# ---------- blog.html ----------
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")
added = []
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
  <a href="blog-{art['slug']}.html" class="blog-post-thumb" style="background:{art['gradient']};" aria-label="{art['aria']}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
    <h3 class="blog-post-title"><a href="blog-{art['slug']}.html" itemprop="headline">{art['title']}</a></h3>
    <p class="blog-post-excerpt" itemprop="description">{art['excerpt']}</p>
    <a href="blog-{art['slug']}.html" class="blog-post-link">Read full playbook →</a>
  </article>"""

    blog = blog[:insert_at] + card + blog[insert_at:]
    added.append(art["num"])

if added:
    blog_path.write_text(blog, encoding="utf-8")
    print(f"[OK] blog.html updated with articles {', '.join(added)}")

# ---------- sitemap.xml ----------
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
sm_added = []
for art in ARTICLES:
    url = f"https://ribbonbow123.com/blog-{art['slug']}.html"
    if url in sm:
        print(f"[SKIP] sitemap.xml already has article {art['num']}")
        continue
    entry = (
        "  <url>\n"
        f"    <loc>{url}</loc>\n"
        f"    <lastmod>{DATE}</lastmod>\n"
        "    <changefreq>monthly</changefreq>\n"
        "    <priority>0.7</priority>\n"
        "  </url>\n"
    )
    close = "</urlset>"
    ci = sm.rfind(close)
    if ci == -1:
        raise SystemExit("</urlset> not found in sitemap.xml")
    sm = sm[:ci] + entry + sm[ci:]
    sm_added.append(art["num"])

if sm_added:
    sm_path.write_text(sm, encoding="utf-8")
    print(f"[OK] sitemap.xml updated with articles {', '.join(sm_added)}")

# ---------- verify ----------
v_blog = blog_path.read_text(encoding="utf-8")
for art in ARTICLES:
    n = v_blog.count(f'href="blog-{art["slug"]}.html"')
    assert n >= 3, f"article {art['num']} blog.html link count low: {n}"

v_sm = sm_path.read_text(encoding="utf-8")
for art in ARTICLES:
    assert f"https://ribbonbow123.com/blog-{art['slug']}.html" in v_sm, f"article {art['num']} missing from sitemap"

import xml.etree.ElementTree as ET
ET.fromstring(v_sm)
print("Verification OK: articles 282 + 283 linked in blog.html and sitemap.xml (valid XML)")