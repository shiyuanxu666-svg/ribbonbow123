#!/usr/bin/env python3
"""Update blog.html + sitemap.xml for ribbonbow123 article 281 (2026-10-21 PM slot)."""
from pathlib import Path

ROOT = Path("/workspace/ribbonbow123")
SLUG = ("oem-ribbon-contract-architecture-9-clauses-price-adjustment-capacity-guarantee-"
        "defect-remedy-ladder-b2b-procurement-2026-10-21-pm")
DATE = "2026-10-21"
TITLE = ("OEM Ribbon Contract Architecture: The 9 Clauses That Actually Carry the Cost - "
         "Price Adjustment, Capacity Guarantees, Defect Remedies and Change Control "
         "for B2B Procurement (2026)")
ARIA = "OEM Ribbon Contract Architecture 9 Clauses B2B Procurement 2026"
EXCERPT = ("A 2026 ribbon sourcing contract-architecture playbook for procurement teams. "
           "Covers price-adjustment mechanics, capacity guarantees and overbooking penalties, "
           "defect-remedy ladders anchored to ISO 2859-1 / ANSI ASQ Z1.4, tooling and brand-asset "
           "ownership, change control, and compliance currency under EU CBAM and CSRD ESRS E1.")

# ---------- blog.html ----------
blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")

if f'href="blog-{SLUG}.html"' in blog:
    print("[SKIP] blog.html already links article 281")
else:
    # Insert new card immediately after the last existing <article class="blog-post-card"> ... </article>
    last_open = blog.rfind('<article class="blog-post-card"')
    if last_open == -1:
        raise SystemExit("no blog-post-card found in blog.html")
    last_close = blog.find("</article>", last_open)
    if last_close == -1:
        raise SystemExit("unterminated blog-post-card in blog.html")
    insert_at = last_close + len("</article>")

    card = f"""
  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="blog-{SLUG}.html" class="blog-post-thumb" style="background:linear-gradient(135deg,#c2185b,#7b1fa2);" aria-label="{ARIA}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
    <h3 class="blog-post-title"><a href="blog-{SLUG}.html" itemprop="headline">{TITLE}</a></h3>
    <p class="blog-post-excerpt" itemprop="description">{EXCERPT}</p>
    <a href="blog-{SLUG}.html" class="blog-post-link">Read full playbook →</a>
  </article>"""

    blog_path.write_text(blog[:insert_at] + card + blog[insert_at:], encoding="utf-8")
    print("[OK] blog.html updated with article 281")

# ---------- sitemap.xml ----------
sm_path = ROOT / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")

if f"https://ribbonbow123.com/blog-{SLUG}.html" in sm:
    print("[SKIP] sitemap.xml already has article 281")
else:
    entry = (
        "  <url>\n"
        f"    <loc>https://ribbonbow123.com/blog-{SLUG}.html</loc>\n"
        f"    <lastmod>{DATE}</lastmod>\n"
        "    <changefreq>monthly</changefreq>\n"
        "    <priority>0.7</priority>\n"
        "  </url>\n"
    )
    close = "</urlset>"
    ci = sm.rfind(close)
    if ci == -1:
        raise SystemExit("</urlset> not found in sitemap.xml")
    sm_path.write_text(sm[:ci] + entry + sm[ci:], encoding="utf-8")
    print("[OK] sitemap.xml updated with article 281")

# ---------- verify ----------
v_blog = blog_path.read_text(encoding="utf-8")
n = v_blog.count(f'href="blog-{SLUG}.html"')
assert n >= 3, f"blog.html link count low: {n}"

v_sm = sm_path.read_text(encoding="utf-8")
assert f"https://ribbonbow123.com/blog-{SLUG}.html" in v_sm, "sitemap missing url"

import xml.etree.ElementTree as ET
ET.fromstring(v_sm)  # sitemap must stay well-formed
print(f"Verification OK: article 281 linked in blog.html ({n} links) and sitemap.xml (valid XML)")