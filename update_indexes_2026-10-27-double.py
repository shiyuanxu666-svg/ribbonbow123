#!/usr/bin/env python3
"""Insert the 2026-10-27 articles (305 AM, 306 PM) into blog.html in
article:published_time descending order, and verify sitemap.xml integrity.

Ordering rule: newest published_time first.
  306 PM -> 2026-10-27T13:00:00+08:00
  305 AM -> 2026-10-27T08:00:00+08:00
  existing latest -> 2026-10-26 (13:00 / 08:00)
"""
import re
from pathlib import Path

DIR = Path("/workspace/ribbonbow123")
BLOG = DIR / "blog.html"

ARTICLES = [
    {
        "slug": "ribbon-oem-supplier-development-gate-review-sample-to-production-release-first-order-readiness-b2b-brand-procurement-2026-10-27-pm",
        "title": "Ribbon OEM Supplier Development &amp; Pre-Production &mdash; The 9 Gates From Sample to Production Release and What Breaks When One Is Skipped (2026)",
        "excerpt": "A 2026 guide to running a ribbon and decorative trim supplier development programme. Explains the nine gates between an initial sample and a production release, the specific failure that occurs when each one is skipped or rushed, how to structure the sample rounds so each one answers a question the previous one raised, the readiness criteria for releasing a first production order, and the documentation that makes the release defensible to a retailer or an auditor.",
        "date": "2026-10-27",
        "aria": "Ribbon OEM Supplier Development mdash The 9 Gates",
    },
    {
        "slug": "ribbon-oem-inventory-ownership-consignment-vmi-stock-risk-model-buyer-supplied-agreement-terms-b2b-brand-procurement-2026-10-27-am",
        "title": "Ribbon OEM Inventory Ownership &amp; Consignment &mdash; Who Holds the Stock, Who Carries the Risk, and How to Write Terms That Work (2026)",
        "excerpt": "A 2026 guide to inventory ownership models in ribbon and decorative trim OEM programmes. Explains the four structures buyers use - buyer-owned stock at the mill, consignment, vendor-managed inventory and a hybrid - what actually shifts between them, the six risk allocations that need explicit contractual wording, the consignment agreement terms that decide whether the arrangement works, and the accounting and tax questions buyers in different jurisdictions must resolve before the first pallet ships.",
        "date": "2026-10-27",
        "aria": "Ribbon OEM Inventory Ownership mdash Who Holds the Stock",
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

# Locate the insertion anchor: the FIRST blog-post-card block in the file.
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
        print(f"[skip] already present: {href}")
        continue
    card = CARD_TMPL.format(**art)
    html = html[:anchor] + card + html[anchor:]
    anchor += len(card)
    inserted.append(art["slug"])

BLOG.write_text(html, encoding="utf-8")
print(f"[ok] inserted {len(inserted)} card(s) into blog.html")

# --- Verify sitemap integrity ---
sm = (DIR / "sitemap.xml").read_text(encoding="utf-8")
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
dups = [u for u in set(locs) if locs.count(u) > 1]
print(f"[check] sitemap urls={len(locs)} unique={len(set(locs))} dups={len(dups)}")
if dups:
    for d in dups[:10]:
        print("  DUP:", d)
future = re.findall(r"<lastmod>(2026-1[1-9][^<]*)</lastmod>", sm)
print(f"[check] future-dated lastmod entries: {len(future)}")
for slug in inserted:
    u = f"https://ribbonbow123.com/blog-{slug}.html"
    print(f"[check] sitemap has {u}: {u in sm}")
