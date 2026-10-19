#!/usr/bin/env python3
"""Update blog.html and sitemap.xml for 2026-10-19 AM/PM articles."""
import re
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")

AM_SLUG = "blog-oem-private-label-ribbon-program-risk-mitigation-26-shock-14-recovery-pillar-architecture-b2b-procurement-2026-10-19-am"
AM_TITLE = "OEM Private Label Ribbon Program Risk Mitigation: The 26-Shock, 14-Recovery-Pillar Architecture for Resilient B2B Private-Label Programs (2026 Q1 2027 Outlook)"
AM_DESC = "A 2026 private-label OEM risk-mitigation playbook for global brand procurement, retail merchandising, and private-label controllers. Covers the 26-shock taxonomy, 14-recovery-pillar architecture, dual-sourcing, safety-stock, supplier-financial-health tier-2/tier-3 monitoring, and Q1 2027 Valentine cascade."
AM_DATE = "2026-10-19"

PM_SLUG = "blog-oem-ribbon-cost-analysis-hidden-landed-cost-decoder-25-component-should-cost-tariff-aware-multi-currency-fx-hedging-b2b-procurement-2026-10-19-pm"
PM_TITLE = "OEM Ribbon Cost Analysis Hidden Landed Cost Decoder: The 25-Component Should-Cost Model with Tariff-Aware Multi-Currency FX Hedging for B2B Procurement (2026)"
PM_DESC = "A 2026 cost-analysis and landed-cost-engineering playbook for OEM ribbon procurement. Covers the 25-component should-cost decoder, tariff-aware 9-scenario sensitivity heat-map, multi-currency FX hedging, EU CBAM carbon-adjusted TCO, and dual-sourcing supplier-benchmark anonymization."
PM_DATE = "2026-10-19"

AM_GRAD = "linear-gradient(135deg,#0d47a1,#1a5f7a)"
PM_GRAD = "linear-gradient(135deg,#1565c0,#0d47a1)"

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

am_block = blog_block(AM_SLUG, AM_TITLE, AM_DESC, AM_DATE, AM_GRAD, "OEM Private Label Ribbon Risk Mitigation 2026")
pm_block = blog_block(PM_SLUG, PM_TITLE, PM_DESC, PM_DATE, PM_GRAD, "OEM Ribbon Cost Analysis 25-Component Decoder 2026")

blog_path = DIR / "blog.html"
blog_text = blog_path.read_text()

# Find the most recent existing post block (after the 274 article)
marker = 'blog-oem-ribbon-supplier-selection-cost-engineering-19-signal-scorecard-tariff-aware-tco-architecture-b2b-procurement-2026.html'
idx = blog_text.find(marker)
if idx == -1:
    raise SystemExit("Marker not found")
# find end of that article block
end_marker = '</article>'
end_idx = blog_text.find(end_marker, idx)
insert_pos = end_idx + len(end_marker)
# Insert PM first (since it's more recent in the same day), then AM
# Actually convention: AM then PM. Let's insert AM, then PM right after.
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
