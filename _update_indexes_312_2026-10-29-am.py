#!/usr/bin/env python3
"""Insert the 2026-10-29 AM article (#312) into blog.html in
article:published_time descending order, and add it to sitemap.xml.

Ordering rule: newest published_time first. Card is inserted before the
first existing blog-post-card, which places it above #311 (2026-10-28 PM).
"""
import re
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")
BLOG = DIR / "blog.html"
SITEMAP = DIR / "sitemap.xml"
SITE = "ribbonbow123.com"
DATE = "2026-10-29"

ARTICLES = [
    {
        "slug": "ribbon-oem-shrinkage-relaxation-dimensional-stability-specification-testing-private-label-buyers-guide-2026-10-29-am",
        "title": "Ribbon Shrinkage, Relaxation &amp; Dimensional Stability &mdash; How to Specify It, Test It and Stop Shipped Stock Moving (2026)",
        "excerpt": "A buyer's guide to ribbon shrinkage, relaxation and dimensional stability in private-label programmes. Separates true shrinkage from roll relaxation and from cutting and creasing, covers the six causes - fibre relaxation, heat setting, dyeing tension, printing heat, weaving tension and finishing - and sets out how to write a testable dimensional specification with the right conditioning protocol, measurement method and acceptance tolerance.",
        "aria": "Ribbon Shrinkage, Relaxation and Dimensional Stability mdash How to Specify It, Test It",
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
    print(f"[check] blog.html card: {('blog-' + slug + '.html') in BLOG.read_text(encoding='utf-8')}")

# --- ordering check: first card should be the newest article ---
bh = BLOG.read_text(encoding="utf-8")
first = re.search(r'href="(blog-[^"]+\.html)"', bh)
print(f"[check] first blog card link: {first.group(1) if first else 'NONE'}")
