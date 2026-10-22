#!/usr/bin/env python3
"""Update blog.html + sitemap.xml for ribbonbow123 articles 288 (AM) and 289 (PM), 2026-10-22."""
from pathlib import Path

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-22"

ARTICLES = [
    {
        "num": "288",
        "slug": "oem-private-label-ribbon-supplier-vetting-architecture-37-signal-9-gate-financial-resilience-compliance-audit-b2b-procurement-2026-10-22-am",
        "title": "OEM Private-Label Ribbon Supplier Vetting Architecture: The 37-Signal, 9-Gate Financial-Resilience, Compliance-Audit and Production-Capacity Vetting Playbook for Brand Procurement (2026)",
        "aria": "OEM Private-Label Ribbon Supplier Vetting Architecture 2026",
        "excerpt": ("A 2026 OEM private-label ribbon supplier-vetting playbook for brand procurement leads, sourcing "
                    "directors, compliance officers and NPI program managers. Covers the 37-signal supplier-vetting "
                    "scorecard, the 9-gate funnel from long-list to award, the red-flag signature catalogue (10 "
                    "patterns), and the mill-side onboarding runbook for a vetted supplier."),
        "gradient": "linear-gradient(135deg,#1a237e,#283593)",
    },
    {
        "num": "289",
        "slug": "oem-custom-ribbon-should-cost-tco-decoder-21-component-should-cost-tariff-aware-multi-currency-fx-hedging-b2b-procurement-2026-10-22-pm",
        "title": "OEM Custom Ribbon Should-Cost TCO Decoder Architecture: The 21-Component Should-Cost, Tariff-Aware, Multi-Currency FX-Hedged Total-Cost-of-Ownership Playbook for Private-Label Brand Buyers (2026)",
        "aria": "OEM Custom Ribbon Should-Cost TCO Decoder 2026",
        "excerpt": ("A 2026 OEM custom ribbon should-cost and total-cost-of-ownership playbook for private-label brand "
                    "buyers, category managers, finance controllers and sourcing directors. Covers the 21-component "
                    "should-cost model, the 5-tier tariff-and-trade-mitigation map under Section 301 / CBAM / UFLPA, "
                    "the FX hedging ladder for CNY/USD/EUR, and the should-cost-to-award price-band translation."),
        "gradient": "linear-gradient(135deg,#004d40,#00695c)",
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

# ---------- sitemap.xml (already partially updated by generator, idempotent re-check) ----------
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
print("Verification OK: articles 288 + 289 linked in blog.html and sitemap.xml (valid XML)")
