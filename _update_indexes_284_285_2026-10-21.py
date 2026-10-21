#!/usr/bin/env python3
"""Update blog.html + sitemap.xml for ribbonbow123 articles 284 (AM) and 285 (PM), 2026-10-21."""
from pathlib import Path

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-21"

ARTICLES = [
    {
        "num": "284",
        "slug": "oem-custom-ribbon-7-layer-color-governance-colorimetric-delta-e-lot-continuity-private-label-2026-10-21-am",
        "title": "OEM Custom Ribbon Color Governance: The 7-Layer System for Controlling Color Drift Across Multi-Lot Production Programs (2026)",
        "aria": "OEM Custom Ribbon 7-Layer Color Governance System 2026",
        "excerpt": ("A 2026 color governance playbook for brand owners, category managers and QC leads running OEM "
                    "custom ribbon programs. Covers the 7-layer ribbon color governance system - colorimetric "
                    "standard, Delta E tolerance bands by application risk, lot continuity bridging, substrate "
                    "declaration, print registration and ink system control, cross-illuminant metamerism testing, "
                    "and change control with a substitution register - plus the business case for standing it up."),
        "gradient": "linear-gradient(135deg,#ad1457,#6a1b9a)",
    },
    {
        "num": "285",
        "slug": "oem-vs-in-house-ribbon-manufacturing-insourcing-outsourcing-fixed-cost-tco-decision-framework-2026-10-21-pm",
        "title": "OEM vs In-House Ribbon Manufacturing: The Fixed-Cost, Scale-Threshold and Risk-Asymmetry Decision Framework (2026)",
        "aria": "OEM vs In-House Ribbon Manufacturing Decision Framework 2026",
        "excerpt": ("A 2026 make-versus-buy playbook for brand owners and sourcing directors evaluating insourcing "
                    "custom ribbon manufacturing. Covers the hidden fixed-cost stack (capital, utilities, specialist "
                    "labor, compliance, working capital), the sustained-volume scale threshold, the risk asymmetry of "
                    "lost-season exposure, the hybrid control model with dual sourcing and managed assets, and a "
                    "five-question decision framework with defined thresholds."),
        "gradient": "linear-gradient(135deg,#37474f,#546e7a)",
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
print("Verification OK: articles 284 + 285 linked in blog.html and sitemap.xml (valid XML)")
