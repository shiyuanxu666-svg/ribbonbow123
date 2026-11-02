#!/usr/bin/env python3
"""Update blog.html and sitemap.xml for 2026-10-20 AM/PM articles."""
import re
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")

AM_SLUG = "blog-oem-custom-branded-ribbon-7-gate-vetting-architecture-47-signal-program-resilience-scorecard-b2b-procurement-2026-10-20-am"
AM_TITLE = "OEM Custom Branded Ribbon 7-Gate Vetting Architecture: The 47-Signal Program-Resilience Scorecard for B2B Private-Label Procurement (2026)"
AM_DESC = "A 2026 OEM vetting playbook for procurement directors, category managers, sourcing managers, and private-label controllers running custom-branded ribbon programs. Covers the 7-gate architecture, 47 hidden risk signals, program-resilience scorecard, dual-sourcing bridge-order migration, and FY2026 to Q1 2027 readiness."
AM_DATE = "2026-10-20"

PM_SLUG = "blog-oem-ribbon-certification-verification-4-stage-framework-iso-oeko-tex-fsc-bsci-cbam-b2b-procurement-compliance-2026-10-20-pm"
PM_TITLE = "OEM Ribbon Certification Verification 4-Stage Framework: ISO, OEKO-TEX, FSC, BSCI, SEDEX, GRS, and EU CBAM Phase-2 Compliance for B2B Procurement (2026)"
PM_DESC = "A 2026 OEM ribbon certification verification playbook for procurement controllers, sourcing finance managers, category buyers, and compliance officers. Covers the 4-stage framework (ISO, OEKO-TEX, FSC, BSCI, SEDEX, CBAM), the 41 percent misrepresentation rate, and EU Green Deal carbon-adjusted-tariff readiness."
PM_DATE = "2026-10-20"

AM_GRAD = "linear-gradient(135deg,#1565c0,#0d47a1)"
PM_GRAD = "linear-gradient(135deg,#1a5f7a,#0d47a1)"

def blog_block(slug, title, desc, date, gradient, short_title):
    return f'''  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="{slug}.html" class="blog-post-thumb" style="background:{gradient};" aria-label="{short_title}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{date}">{date}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
    <h3 class="blog-post-title"><a href="{slug}.html" itemprop="headline">{title}</a></h3>
    <p class="blog-post-excerpt" itemprop="description">{desc}</p>
    <a href="{slug}.html" class="blog-post-link">Read full playbook →</a>
  </article>'''

am_block = blog_block(AM_SLUG, AM_TITLE, AM_DESC, AM_DATE, AM_GRAD, "OEM Custom Branded Ribbon 7-Gate Vetting 2026")
pm_block = blog_block(PM_SLUG, PM_TITLE, PM_DESC, PM_DATE, PM_GRAD, "OEM Ribbon Certification 4-Stage Verification 2026")

blog_path = DIR / "blog.html"
blog_text = blog_path.read_text()

# Find the most recent existing post block (after the 276 article)
marker = 'blog-oem-ribbon-cost-analysis-hidden-landed-cost-decoder-25-component-should-cost-tariff-aware-multi-currency-fx-hedging-b2b-procurement-2026-10-19-pm'
idx = blog_text.find(marker)
if idx == -1:
    raise SystemExit("Marker not found")
# find end of that article block
end_marker = '</article>'
end_idx = blog_text.find(end_marker, idx)
insert_pos = end_idx + len(end_marker)
# Insert AM, then PM right after
new_blog = blog_text[:insert_pos] + "\n" + am_block + "\n" + pm_block + "\n" + blog_text[insert_pos:]
blog_path.write_text(new_blog)
print(f"blog.html updated, new size {len(new_blog)}")

# Sitemap update
sitemap_path = DIR / "sitemap.xml"
sm = sitemap_path.read_text()

def sm_entry(slug, date):
    return f'''  <url>
    <loc>https://ribbonbow123.com/{slug}.html</loc>
    <lastmod>{date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''

am_sm = sm_entry(AM_SLUG, AM_DATE)
pm_sm = sm_entry(PM_SLUG, PM_DATE)

# Insert before closing </urlset>
close_tag = "</urlset>"
close_idx = sm.rfind(close_tag)
new_sm = sm[:close_idx] + am_sm + pm_sm + sm[close_idx:]
sitemap_path.write_text(new_sm)
print(f"sitemap.xml updated, new size {len(new_sm)}")