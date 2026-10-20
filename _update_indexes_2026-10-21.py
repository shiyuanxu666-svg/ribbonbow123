#!/usr/bin/env python3
"""Update blog.html and sitemap.xml for 2026-10-21 AM/PM articles."""
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")

AM_SLUG = "blog-oem-custom-branded-ribbon-14-touchpoint-onboarding-runway-tracker-npi-speed-to-market-2026-10-21-am"
AM_TITLE = "OEM Custom Branded Ribbon Onboarding: The 14-Touchpoint Runway Tracker and 90-Day NPI Speed-to-Market Playbook for Private-Label Brand Owners (2026)"
AM_DESC = "A 2026 OEM onboarding playbook for private-label brand owners and NPI managers. Covers the 14-touchpoint onboarding runway tracker, parallel-track sequencing, the 90-day NPI critical path, and FY2026 holiday-peak to Q1 2027 cascade planning."
AM_DATE = "2026-10-21"

PM_SLUG = "blog-oem-ribbon-supplier-selection-cost-engineering-25-signal-tco-scorecard-b2b-procurement-2026-10-21-pm"
PM_TITLE = "OEM Ribbon Supplier Selection and Cost Engineering: The 25-Signal Risk-Adjusted TCO Scorecard for B2B Global Brand Procurement (2026)"
PM_DESC = "A 2026 supplier-selection and cost-engineering playbook for procurement directors. Covers the 25-signal scorecard, the 23-component should-cost model, risk-adjusted TCO, and weighted-decision matrix governance."
PM_DATE = "2026-10-21"

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


am_block = blog_block(AM_SLUG, AM_TITLE, AM_DESC, AM_DATE, AM_GRAD,
                      "OEM Ribbon 14-Touchpoint Onboarding Runway Tracker 2026")
pm_block = blog_block(PM_SLUG, PM_TITLE, PM_DESC, PM_DATE, PM_GRAD,
                      "OEM Ribbon Supplier Selection 25-Signal TCO Scorecard 2026")

blog_path = DIR / "blog.html"
blog_text = blog_path.read_text()

# Anchor on the most recently published article (2026-10-20 PM)
marker = 'blog-oem-ribbon-certification-verification-4-stage-framework-iso-oeko-tex-fsc-bsci-cbam-b2b-procurement-compliance-2026-10-20-pm'
idx = blog_text.find(marker)
if idx == -1:
    raise SystemExit("Marker (2026-10-20 PM article) not found in blog.html")
end_marker = '</article>'
end_idx = blog_text.find(end_marker, idx)
if end_idx == -1:
    raise SystemExit("Closing </article> not found")
insert_pos = end_idx + len(end_marker)

new_blog = blog_text[:insert_pos] + "\n" + am_block + "\n" + pm_block + "\n" + blog_text[insert_pos:]
blog_path.write_text(new_blog)
print(f"blog.html updated -> {len(new_blog)} bytes")

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

close_tag = "</urlset>"
close_idx = sm.rfind(close_tag)
if close_idx == -1:
    raise SystemExit("</urlset> not found in sitemap.xml")
new_sm = sm[:close_idx] + am_sm + pm_sm + sm[close_idx:]
sitemap_path.write_text(new_sm)
print(f"sitemap.xml updated -> {len(new_sm)} bytes")

# Verify
verify_blog = blog_path.read_text()
for slug in (AM_SLUG, PM_SLUG):
    assert verify_blog.count(f'href="{slug}.html"') >= 2, f"blog.html link count low for {slug}"
verify_sm = sitemap_path.read_text()
for slug in (AM_SLUG, PM_SLUG):
    assert f"https://ribbonbow123.com/{slug}.html" in verify_sm, f"sitemap missing {slug}"
print("Verification OK: both articles linked in blog.html and sitemap.xml")