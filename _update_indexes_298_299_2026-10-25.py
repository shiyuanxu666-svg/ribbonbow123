#!/usr/bin/env python3
"""Insert article cards 298 (AM) and 299 (PM) into ribbonbow123 blog.html,
newest-first, then verify schema/meta/FAQ/sitemap once."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-25"

ARTICLES = [
    {
        "num": "299",
        "slug": ("oem-ribbon-quality-escalation-capa-post-shipping-failure-7-step-corrective-action-loop-"
                 "root-cause-discipline-claim-evidence-architecture-b2b-brand-procurement-2026-10-25-pm"),
        "title": ("OEM Ribbon Quality Escalation &amp; CAPA &mdash; The 7-Step Corrective Action Loop When "
                  "a Trim Fails in the Market (2026)"),
        "aria": "OEM Ribbon Quality Escalation CAPA 2026",
        "excerpt": ("A 2026 buyer's guide to ribbon quality escalation and CAPA for OEM programmes. Explains why "
                    "most trim complaints are never properly closed, the seven-step corrective action loop that "
                    "separates a genuine root cause from a convenient one, the discipline that stops a recurring "
                    "defect from returning, and the documentation set that allows a claim to be settled on evidence "
                    "rather than on argument."),
        "gradient": "linear-gradient(135deg,#b71c1c,#e53935)",
    },
    {
        "num": "298",
        "slug": ("oem-ribbon-co-packing-kitting-specification-assembled-trim-set-bill-of-materials-"
                 "8-point-definition-assembly-stage-controls-single-sku-b2b-brand-procurement-2026-10-25-am"),
        "title": ("OEM Co-Packing &amp; Kitting Specification &mdash; How to Define a Packaged Trim Set "
                  "(Ribbon, Bow, Organza Bag &amp; Card) as One Sellable SKU (2026)"),
        "aria": "OEM Ribbon Co-Packing Kitting Specification 2026",
        "excerpt": ("A 2026 buyer's guide to OEM co-packing and kitting for ribbon programs. Explains why a trim set "
                    "specified as a loose list of parts cannot be quoted, scheduled or inspected, the eight-point "
                    "bill of materials definition that turns separate components into one sellable SKU, the "
                    "assembly stage controls that stop set-level defects escaping to retail, and the four costing "
                    "failures that appear when the set is specified part by part instead of as an assembly."),
        "gradient": "linear-gradient(135deg,#00695c,#26a69a)",
    },
]

blog_path = ROOT / "blog.html"
blog = blog_path.read_text(encoding="utf-8")

for art in ARTICLES:
    href = f'href="blog-{art["slug"]}.html"'
    if href in blog:
        print(f"[SKIP] blog.html already links article {art['num']}")
        continue
    last_open = blog.rfind('<article class="blog-post-card"')
    if last_open == -1:
        raise SystemExit("no blog-post-card found in blog.html")
    last_close = blog.find("</article>", last_open)
    if last_close == -1:
        raise SystemExit("unterminated blog-post-card in blog.html")
    insert_at = last_close + len("</article>")
    card = f"""
  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="blog-{art["slug"]}.html" class="blog-post-thumb" style="background:{art["gradient"]};" aria-label="{art["aria"]}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{DATE}">{DATE}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="blog-{art["slug"]}.html">{art["title"]}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{art["excerpt"]}</p>
  <a class="blog-post-link" href="blog-{art["slug"]}.html">Read more &rarr;</a>
</article>"""
    blog = blog[:insert_at] + card + blog[insert_at:]
    print(f"[OK] blog.html updated with article {art['num']}")

blog_path.write_text(blog, encoding="utf-8")

# ---------------- verify (single pass) ----------------
v_blog = blog_path.read_text(encoding="utf-8")
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
for art in ARTICLES:
    n = v_blog.count(f'href="blog-{art["slug"]}.html"')
    assert n >= 3, f"article {art['num']} link count low: {n}"
    url = f"https://ribbonbow123.com/blog-{art['slug']}.html"
    assert url in sm, f"article {art['num']} missing from sitemap"
    print(f"  article {art['num']}: {n} links in blog.html, present in sitemap")

ET.fromstring(sm)
locs = re.findall(r"<loc>(.*?)</loc>", sm)
dupes = {x for x in locs if locs.count(x) > 1}
assert not dupes, f"duplicate sitemap URLs: {list(dupes)[:5]}"
print(f"Verification OK: sitemap valid XML, {len(locs)} URLs, 0 duplicates")

for art in ARTICLES:
    ah = (ROOT / f'blog-{art["slug"]}.html').read_text(encoding="utf-8")
    for token in ['"@type": "BlogPosting"', '"@type": "FAQPage"', "og:title", "twitter:card",
                  'rel="canonical"', 'name="description"', 'name="keywords"', 'og:image',
                  'article:published_time', '"@type": "Article"', "since 2004"]:
        assert token in ah, f"article {art['num']} missing {token}"
    assert ah.count('"@type": "Question"') >= 5, f"article {art['num']} FAQ too short"
    words = len(re.sub(r"<[^>]+>", " ", ah).split())
    print(f"  article {art['num']}: schema/meta/FAQ OK, ~{words} words")
print("All checks passed.")
