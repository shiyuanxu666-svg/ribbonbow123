#!/usr/bin/env python3
"""Add ribbonbow123 article #317 (2026-10-28 PM) to blog.html + index.html, then verify.

Follows the established ribbonbow123 blog-card structure:
  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
    <a href="SLUG.html" class="blog-post-thumb" style="background:linear-gradient(...)" aria-label="..."></a>
    <div class="blog-post-meta">
      <span class="blog-post-date" itemprop="datePublished" content="2026-10-28">2026-10-28</span>
      <span class="blog-post-category">B2B Sourcing</span>
    </div>
    <h3 class="blog-post-title" itemprop="headline"><a href="SLUG.html">TITLE</a></h3>
    <p class="blog-post-excerpt" itemprop="description">DESC</p>
    <a class="blog-post-link" href="SLUG.html">Read more &rarr;</a>
  </article>
"""
from pathlib import Path
import re
import json
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-28"
SLUG = ("blog-ribbon-oem-subscription-box-curated-gifting-trim-set-economics-seasonal-rotation-"
        "unboxing-b2b-brand-procurement-2026-10-28-pm.html")
TITLE = ("Ribbon for Subscription Boxes &amp; Curated Gifting &mdash; Trim Set Design, "
         "Per-Box Economics, Seasonal Rotation and the Unboxing Moment (2026)")
DESC = ("A buyer's guide to ribbon trims for subscription boxes and curated gifting programmes. Covers how to "
        "structure a trim set and what each piece does, the per-box trim cost that actually matters at volume, "
        "seasonal colour rotation and how to manage it without a SKU explosion, what survives or fails in the "
        "unboxing moment and in a hot mail box, and how to specify ribbon for a programme that repeats every month.")
ARIA = "Ribbon for Subscription Boxes and Curated Gifting mdash Trim Set Design and Per-Box Economics"
THUMB = "linear-gradient(135deg,#6a1b9a,#8e24aa)"

# ---------- blog.html ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
if SLUG in blog:
    print(f"[SKIP] blog.html already has {SLUG[:50]}")
else:
    card = f'''<article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="{SLUG}" class="blog-post-thumb" style="background:{THUMB};" aria-label="{ARIA}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="{SLUG}">{TITLE}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{DESC}</p>
  <a class="blog-post-link" href="{SLUG}">Read more &rarr;</a>
</article>'''
    # insert after the last complete </article>
    idx = blog.rfind("</article>")
    if idx == -1:
        raise SystemExit("no </article> in blog.html")
    idx += len("</article>")
    blog = blog[:idx] + "\n" + card + blog[idx:]
    bp.write_text(blog, encoding="utf-8")
    print(f"[OK] blog.html + 1 card for #{SLUG[5:20]}")

# ---------- index.html ----------
ip = ROOT / "index.html"
idxh = ip.read_text(encoding="utf-8")
if SLUG in idxh:
    print(f"[SKIP] index.html already has {SLUG[:50]}")
else:
    link = f'<li><a href="{SLUG}">{TITLE}</a></li>'
    i = idxh.rfind("</li>")
    if i == -1:
        raise SystemExit("no </li> in index.html")
    i += len("</li>")
    idxh = idxh[:i] + "\n" + link + idxh[i:]
    ip.write_text(idxh, encoding="utf-8")
    print("[OK] index.html + 1 link")

# ================= VERIFY (single pass) =================
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)  # well-formedness
blog_f = (ROOT / "blog.html").read_text(encoding="utf-8")
idx_f = (ROOT / "index.html").read_text(encoding="utf-8")
ap = (ROOT / SLUG).read_text(encoding="utf-8")

assert SLUG in blog_f, "blog.html missing card"
assert SLUG in idx_f, "index.html missing link"
assert f"https://ribbonbow123.com/{SLUG}" in sm_f, "sitemap missing loc"

assert ap.count("<h1>") == 1, f"h1 count = {ap.count('<h1>')}"
assert 'rel="canonical"' in ap, "no canonical"
assert 'property="og:title"' in ap and 'property="og:image"' in ap, "OG missing"
assert 'name="twitter:card"' in ap, "twitter card missing"
assert "<h2>Frequently Asked Questions</h2>" in ap, "no visible FAQ h2"
assert "since 2004" in ap, "no 'since 2004'"
assert "XXX-Module" not in ap, "template placeholder leaked"
assert "Article #317" in ap, "article number wrong"
assert "2026-10-28" in ap, "date missing"

blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', ap, re.S)
types = [json.loads(b).get("@type") for b in blocks]
for required in ("Article", "BlogPosting", "FAQPage"):
    assert required in types, f"no {required} schema (got {types})"

# FAQ visible answers must match schema question count
nq = sum(len(json.loads(b)["mainEntity"]) for b in blocks if json.loads(b).get("@type") == "FAQPage")
assert ap.count('<h3>') >= nq, f"visible h3 {ap.count('<h3>')} < schema questions {nq}"

# internal link sanity: every href to a local .html in the article must exist
missing = []
for href in set(re.findall(r'href="([^"#][^"]*\.html)"', ap)):
    if href.startswith("http"):
        continue
    if not (ROOT / href).exists():
        missing.append(href)
assert not missing, f"dead internal links: {missing}"

words = len(re.sub(r"<[^>]+>", " ", ap).split())
print(f"[VERIFIED] {SLUG[:60]}")
print(f"           words={words} | schema={types} | faqQ={nq} | h2={ap.count('<h2>')} | deadlinks=0")

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate sitemap locs: {len(locs)} vs {len(set(locs))}"
missing_files = [l.replace("https://ribbonbow123.com/", "") for l in locs
                  if l.endswith(".html") and not (ROOT / l.replace("https://ribbonbow123.com/", "")).exists()]
future = re.findall(r"<lastmod>(2026-10-(?:29|30|31))</lastmod>", sm_f)
print(f"\nSitemap: {len(locs)} unique locs, {len(locs)-len(set(locs))} dups, "
      f"{len(missing_files)} missing files, {len(future)} future lastmod")
print("PUBLISH VERIFY OK")
