#!/usr/bin/env python3
"""Add ribbonbow123 article #307 to blog.html card grid (newest first) + verify."""
from pathlib import Path
import re

ROOT = Path("/workspace/ribbonbow123")
SLUG = ("ribbon-oem-compliance-claims-substantiation-greenwashing-risk-rohs-reach-prop65-"
        "chemical-and-environmental-claims-b2b-brand-procurement-2026-10-26-pm")
FILE = f"blog-{SLUG}.html"
DATE = "2026-10-26"
TITLE = ("Ribbon OEM Compliance &amp; Claims Substantiation &mdash; How to Defend Every Chemical, "
         "Sustainability and Country-of-Origin Claim You Print on the Packaging (2026)")
DESC = ("A 2026 guide to substantiating chemical, environmental and origin claims on imported ribbon and "
        "decorative trim. Explains what a RoHS, REACH, Prop 65, recycled-content, organic or carbon-neutral "
        "claim actually obliges you to prove, the test reports and certificates that do and do not support each "
        "claim, the greenwashing exposure when a mill supplies a marketing claim you cannot defend, the "
        "document chain that has to exist before a claim goes on a pack, and the audit questions a retailer or "
        "regulator will ask. Written for brand owners, packaging compliance managers and procurement leads "
        "running private-label ribbon programmes.")

CARD = f"""  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="{FILE}" class="blog-post-thumb" style="background:linear-gradient(135deg,#00695c,#26a69a);" aria-label="Ribbon OEM Compliance Claims Substantiation mdash How to Defend Every Chemical"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="{FILE}">{TITLE}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{DESC}</p>
  <a class="blog-post-link" href="{FILE}">Read more &rarr;</a>
</article>
"""

bp = ROOT / "blog.html"
bf = bp.read_text(encoding="utf-8")
if FILE in bf:
    print("[SKIP] blog.html already has article")
else:
    marker = '<div class="blog-grid">\n'
    idx = bf.find(marker)
    if idx == -1:
        raise SystemExit("blog-grid not found")
    idx += len(marker)
    bf = bf[:idx] + CARD + bf[idx:]
    bp.write_text(bf, encoding="utf-8")
    print("[OK] blog.html card added")

# ---- verification ----
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
bf = (ROOT / "blog.html").read_text(encoding="utf-8")
art = (ROOT / FILE).read_text(encoding="utf-8")
assert FILE in bf, "blog.html missing article"
assert f"https://ribbonbow123.com/{FILE}" in sm, "sitemap missing article"
assert f'content="{DATE}"' in bf, "blog.html date missing"
assert art.count("<h1>") == 1, "h1 count != 1"
assert "application/ld+json" in art, "no JSON-LD"

locs = re.findall(r"<loc>(.*?)</loc>", sm)
assert len(locs) == len(set(locs)), f"duplicate sitemap locs: {len(locs)} vs {len(set(locs))}"
future = [l for l in locs if re.search(r"2026-1[1-2]-\d\d", l)]
print(f"Verification OK: sitemap {len(locs)} unique locs, 0 dups; article linked in blog.html + sitemap.xml")
