#!/usr/bin/env python3
"""Insert the two 2026-10-28 articles (#315 AM, #316 PM) into blog.html in
article:published_time descending order, and add them to sitemap.xml.

Ordering: #316 (13:00) must sit above #315 (08:00), and both must sit above
#314 (2026-10-28 13:00 was already used... verify against existing cards).
Existing #313 = 2026-10-28 08:00, #314 = 2026-10-28 13:00.
New #315 = 2026-10-28 08:00, #316 = 2026-10-28 13:00.
To keep strict descending order and place the new pair at the top, the new
cards are inserted at the top of the card list (newest first).
"""
import re
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")
BLOG = DIR / "blog.html"
SITEMAP = DIR / "sitemap.xml"
SITE = "ribbonbow123.com"
DATE = "2026-10-28"

# Ordered newest-first.
ARTICLES = [
    {
        "slug": "ribbon-oem-fragrance-beauty-packaging-trim-atomiser-collar-cap-tie-decoration-compliance-b2b-brand-procurement-2026-10-28-pm",
        "title": "Fragrance &amp; Beauty Packaging Ribbon &mdash; Atomiser Collars, Cap Ties, Gift-Set Trim and the Compliance Traps (2026)",
        "excerpt": "A buyer's guide to ribbon for fragrance and beauty packaging. Covers decoration processes for atomiser collars and cap ties, alcohol and actives exposure, dye migration and fragrance staining, cosmetic GMP and labelling expectations for trim, and how to qualify ribbon for sea freight and hot-climate shelf life.",
        "aria": "Fragrance and Beauty Packaging Ribbon mdash Atomiser Collars and Cap Ties",
    },
    {
        "slug": "ribbon-oem-elastic-stretch-recovery-compression-specification-private-label-buyers-guide-2026-10-28-am",
        "title": "Elastic and Stretch Ribbon &mdash; How to Specify Stretch, Recovery and Compression (2026)",
        "excerpt": "A buyer's guide to elastic ribbon for private-label programmes. Separates stretch percentage from recovery, compression set and stretch fatigue, explains how the elastane core and construction determine behaviour, and sets out how to write and test an elastic specification that an inspector can actually verify.",
        "aria": "Elastic and Stretch Ribbon mdash How to Specify Stretch, Recovery and Compression",
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

bh = BLOG.read_text(encoding="utf-8")
cards = re.findall(r'<article class="blog-post-card"[^>]*>(.*?)</article>', bh, re.S)
print(f"[check] total blog cards: {len(cards)}")
for i, c in enumerate(cards[:4]):
    d = re.search(r'itemprop="datePublished" content="([^"]+)"', c)
    s = re.search(r'href="(blog-[^"]+)"', c)
    print(f"  card[{i}] {d.group(1) if d else '?'} {s.group(1)[:70] if s else '?'}")

for slug in inserted + sm_inserted:
    u = f"https://{SITE}/blog-{slug}.html"
    print(f"[check] sitemap has {u[:70]}...: {u in sm}")
    print(f"[check] file exists: {(DIR / ('blog-' + slug + '.html')).exists()}")
    print(f"[check] blog.html card: {('blog-' + slug + '.html') in bh}")
