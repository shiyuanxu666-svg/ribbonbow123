#!/usr/bin/env python3
"""Insert the 2026-10-28 articles (310 AM, 311 PM) into blog.html in
article:published_time descending order, and add them to sitemap.xml.

Ordering rule: newest published_time first.
  311 PM -> 2026-10-28T13:00:00+08:00
  310 AM -> 2026-10-28T08:00:00+08:00
"""
import re
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")
BLOG = DIR / "blog.html"
SITEMAP = DIR / "sitemap.xml"
SITE = "ribbonbow123.com"
DATE = "2026-10-28"

ARTICLES = [
    {
        "slug": "ribbon-oem-sampling-and-pre-production-approval-what-each-sample-proves-avoiding-the-wrong-approval-b2b-brand-procurement-2026-10-28-pm",
        "title": "Ribbon OEM Sampling &amp; Pre-Production Approval &mdash; What Each Sample Actually Proves (2026)",
        "excerpt": "A practical guide to sampling in private-label ribbon programmes. Breaks the sample ladder down into eight distinct jobs a ribbon sample can do - colour lab dip, greige, printed strike-off, production sample, construction sample, performance test sample, assembly sample and packing sample - explains what each one proves and what it does not, sets a sensible sampling budget and sample cost rules, and shows how to write a pre-production approval record that still means something when the roll arrives.",
        "aria": "Ribbon OEM Sampling and Pre-Production Approval mdash What Each Sample Proves",
    },
    {
        "slug": "ribbon-oem-decoration-process-selection-screen-print-heat-transfer-foil-jacquard-private-label-buyers-guide-2026-10-28-am",
        "title": "Choosing a Ribbon Decoration Method &mdash; Screen Print, Heat Transfer, Foil, Jacquard and Sublimation for Private Label (2026)",
        "excerpt": "A buyer's guide to specifying decoration on custom ribbon. Compares screen printing, heat transfer printing, foil stamping, jacquard weaving and sublimation across colour capability, cost per metre, durability under rubbing, washing, light and abrasion, minimum order quantities, setup charges and lead time. Explains how to match the method to the end use - gift packaging, apparel trim, hair accessories, florals, pet and seasonal decoration - and how to specify decoration so the mill quotes the right process.",
        "aria": "Choosing a Ribbon Decoration Method mdash Screen Print, Heat Transfer, Foil, Jacquard",
    },
]

CARD_TMPL = """  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="blog-{slug}.html" class="blog-post-thumb" style="background:linear-gradient(135deg,#00695c,#26a69a);" aria-label="{aria}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{date}">{date}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="blog-{slug}.html">{title}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{excerpt}</p>
  <a class="blog-post-link" href="blog-{slug}.html">Read more &rarr;</a>
</article>
"""

html = BLOG.read_text(encoding="utf-8")

anchor = None
for m in re.finditer(r'<article class="blog-post-card"[^>]*>', html):
    anchor = m.start()
    break
if anchor is None:
    raise SystemExit("no blog-post-card found in blog.html")

inserted = []
for art in ARTICLES:
    href = f"blog-{art['slug']}.html"
    if href in html:
        print(f"[skip] already present in blog.html: {href}")
        continue
    card = CARD_TMPL.format(date=DATE, **art)
    html = html[:anchor] + card + html[anchor:]
    anchor += len(card)
    inserted.append(art["slug"])

BLOG.write_text(html, encoding="utf-8")
print(f"[ok] inserted {len(inserted)} card(s) into blog.html")

# --- sitemap.xml ---
sm = SITEMAP.read_text(encoding="utf-8")
sm_inserted = []
for art in ARTICLES:
    url = f"https://{SITE}/blog-{art['slug']}.html"
    if url in sm:
        print(f"[skip] sitemap already has {url}")
        continue
    entry = (
        "  <url>\n"
        f"    <loc>{url}</loc>\n"
        f"    <lastmod>{DATE}</lastmod>\n"
        "    <changefreq>monthly</changefreq>\n"
        "    <priority>0.7</priority>\n"
        "  </url>\n"
    )
    idx = sm.rfind("</urlset>")
    if idx == -1:
        raise SystemExit("</urlset> not found in sitemap.xml")
    sm = sm[:idx] + entry + sm[idx:]
    sm_inserted.append(art["slug"])

SITEMAP.write_text(sm, encoding="utf-8")
print(f"[ok] inserted {len(sm_inserted)} url(s) into sitemap.xml")

# --- verify ---
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
dups = [u for u in set(locs) if locs.count(u) > 1]
print(f"[check] sitemap urls={len(locs)} unique={len(set(locs))} dups={len(dups)}")
for d in dups[:10]:
    print("  DUP:", d)
future = re.findall(r"<lastmod>(2026-1[1-9][^<]*)</lastmod>", sm)
print(f"[check] future-dated lastmod entries: {len(future)}")
for slug in inserted + sm_inserted:
    u = f"https://{SITE}/blog-{slug}.html"
    print(f"[check] sitemap has {u}: {u in sm}")
    print(f"[check] file exists: {(DIR / ('blog-' + slug + '.html')).exists()}")
