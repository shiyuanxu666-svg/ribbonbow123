#!/usr/bin/env python3
"""Add FAQPage JSON-LD to article 292 (2026-10-23 PM) which was missing it,
then link articles 293 and 294 into blog.html and verify sitemap."""
from pathlib import Path
import json, re, html as html_mod
import xml.etree.ElementTree as ET

ROOT = Path("/workspace/ribbonbow123")
DATE = "2026-10-24"

# ---------------- 1. FAQPage for article 292 ----------------
OLD = "blog-oem-ribbon-sample-approval-ppap-process-architecture-6-stage-gate-preproduction-part-approval-evidence-signoff-b2b-brand-procurement-2026-10-23-pm.html"
p = ROOT / OLD
t = p.read_text(encoding="utf-8")
if "FAQPage" not in t:
    # extract the visible FAQ Q&A pairs from the rendered HTML
    faq_part = t.split('<div class="faq">')[1].split("</div>")[0]
    pairs = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", faq_part, re.S)
    pairs = [(html_mod.unescape(q), html_mod.unescape(a)) for q, a in pairs]
    assert len(pairs) == 6, f"expected 6 FAQ pairs, got {len(pairs)}"
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": html_mod.escape(q),
                "acceptedAnswer": {"@type": "Answer", "text": html_mod.escape(a)},
            }
            for q, a in pairs
        ],
    }
    block = '<script type="application/ld+json">\n' + json.dumps(faq_schema, indent=4, ensure_ascii=False) + "\n    </script>\n"
    anchor = "</head>"
    assert anchor in t
    t = t.replace(anchor, block + anchor, 1)
    p.write_text(t, encoding="utf-8")
    print(f"[OK] FAQPage added to article 292 ({len(pairs)} items)")
else:
    print("[skip] article 292 already has FAQPage")

# ---------------- 2. blog.html cards ----------------
ARTICLES = [
    {
        "num": "293",
        "slug": ("oem-custom-ribbon-moq-order-lot-economics-small-brand-scale-up-guide-lower-case-foiling-"
                 "colour-development-cost-tradeoffs-b2b-brand-owners-2026-10-24-am"),
        "title": ("OEM Custom Ribbon MOQ &amp; Order-Lot Economics: A Small-Brand Scale-Up Guide to Lowering "
                  "Case Folding, Colour Development Cost and the Trade-offs That Decide Your Unit Price (2026)"),
        "aria": "OEM Custom Ribbon MOQ and Order-Lot Economics 2026",
        "excerpt": ("A 2026 OEM custom ribbon MOQ and order-lot economics guide for brand owners and procurement "
                    "leads. Covers the five quantity floors inside a ribbon MOQ, the three variable-cost tiers "
                    "that dominate unit price at low volume, case folding and colour development cost, and how "
                    "to structure a ramp from a validation run to a multi-SKU programme without paying "
                    "development cost twice."),
        "gradient": "linear-gradient(135deg,#2e7d32,#43a047)",
    },
    {
        "num": "294",
        "slug": ("oem-ribbon-supply-contract-price-adjustment-framework-capacity-reservation-index-linked-"
                 "pricing-defect-remedy-ladder-b2b-brand-procurement-2026-10-24-pm"),
        "title": ("OEM Ribbon Supply Contract &amp; Price Adjustment Framework: Capacity Reservation, "
                  "Index-Linked Pricing and the Defect Remedy Ladder Every Brand Agreement Should Contain (2026)"),
        "aria": "OEM Ribbon Supply Contract and Price Adjustment Framework 2026",
        "excerpt": ("A 2026 OEM ribbon supply contract and price adjustment framework for brand owners and "
                    "procurement managers. Covers the eight clauses that govern a ribbon supply relationship, "
                    "index-linked price adjustment with a collar, what a credible peak-season capacity "
                    "reservation contains, and the five-rung defect remedy ladder that resolves quality failures "
                    "without a dispute."),
        "gradient": "linear-gradient(135deg,#c62828,#ef6c00)",
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

# ---------------- 3. verify ----------------
v_blog = blog_path.read_text(encoding="utf-8")
for art in ARTICLES:
    n = v_blog.count(f'href="blog-{art["slug"]}.html"')
    assert n >= 3, f"article {art['num']} link count low: {n}"
    url = f"https://ribbonbow123.com/blog-{art['slug']}.html"
    assert url in (ROOT / "sitemap.xml").read_text(encoding="utf-8"), f"article {art['num']} missing from sitemap"
    print(f"  article {art['num']}: {n} links in blog.html, present in sitemap")

sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm)
# sitemap duplicate check
locs = re.findall(r"<loc>(.*?)</loc>", sm)
dupes = {x for x in locs if locs.count(x) > 1}
assert not dupes, f"duplicate sitemap URLs: {list(dupes)[:5]}"
print(f"Verification OK: sitemap valid XML, {len(locs)} URLs, 0 duplicates")

# ordering check in blog.html (newest first)
order_ok = v_blog.find(f'blog-{ARTICLES[0]["slug"]}.html') < v_blog.find(f'blog-{ARTICLES[1]["slug"]}.html')
print(f"blog.html ordering (293 before 294): {order_ok}")

for art in ARTICLES:
    ah = (ROOT / f'blog-{art["slug"]}.html').read_text(encoding="utf-8")
    for token in ['"@type": "BlogPosting"', '"@type": "FAQPage"', "og:title", "twitter:card", 'rel="canonical"', 'name="description"', 'name="keywords"']:
        assert token in ah, f"article {art['num']} missing {token}"
    h1 = ah.count("<h1>")
    assert h1 == 1, f"article {art['num']} has {h1} H1s"
print("Both new articles: BlogPosting + FAQPage + meta + OG + single H1 confirmed")
