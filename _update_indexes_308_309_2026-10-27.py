#!/usr/bin/env python3
"""Insert the 2026-10-27 articles (308 AM, 309 PM) into blog.html in
article:published_time descending order, and add them to sitemap.xml.

Ordering rule: newest published_time first.
  309 PM -> 2026-10-27T13:00:00+08:00
  308 AM -> 2026-10-27T08:00:00+08:00
"""
import re
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")
BLOG = DIR / "blog.html"
SITEMAP = DIR / "sitemap.xml"
SITE = "ribbonbow123.com"
DATE = "2026-10-27"

ARTICLES = [
    {
        "slug": "ribbon-oem-certificate-scope-supplier-qualification-verifying-what-a-badge-actually-covers-b2b-retail-procurement-2026-10-27-pm",
        "title": "What a Ribbon Certificate Actually Covers &mdash; Reading Scope, Verifying It, and Qualifying a Supplier You Can Ship With (2026)",
        "excerpt": "A practical guide to using ribbon supplier certificates properly. Explains why a badge on a PDF usually does not cover the exact product you are buying, how to read scope and certificate number on six common standards - OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA - how to verify each with the issuing body in minutes, the eight qualification gates for approving a new factory, and the questions that expose a supplier who cannot answer them.",
        "aria": "What a Ribbon Certificate Actually Covers mdash Reading Scope",
    },
    {
        "slug": "ribbon-oem-quoted-price-line-by-line-where-the-money-goes-defending-a-factory-number-b2b-procurement-2026-10-27-am",
        "title": "Ribbon OEM Quoted Price, Line by Line &mdash; Where the Money Actually Goes and How to Defend a Factory Number (2026)",
        "excerpt": "A practical guide to reading a woven ribbon factory quotation. Breaks a mill price into fourteen cost lines - yarn, dyeing, weaving, finishing, sizing, tooling, QC, packing, overhead, margin, freight and duty - shows what each line should look like for a given width, material and print process, explains the five places where quotes quietly differ from each other without the buyer noticing, and gives a negotiation sequence that protects margin without pushing the mill into a quality corner.",
        "aria": "Ribbon OEM Quoted Price Line by Line mdash Where the Money Goes",
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
