#!/usr/bin/env python3
"""Insert articles #320 and #321 into blog.html + index.html, then verify.

blog.html cards are inserted in article:published_time DESCENDING order: the
newest card goes before the first existing blog-post-card, so #321 (13:00)
lands above #320 (08:00) which lands above #319 (08:00, previous run).
"""
import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path("/workspace/ribbonbow123")
SITE = "ribbonbow123.com"
DATE = "2026-10-29"

ARTICLES = [
    {
        "slug": "ribbon-oem-die-cutting-laser-cutting-tolerance-edge-quality-tooling-conversion-private-label-buyers-guide-2026-10-29-pm",
        "title": "Ribbon Die-Cutting &amp; Laser Cutting &mdash; Edge Quality, Tolerance, Tooling Economics and How to Specify a Cut Ribbon Part (2026)",
        "excerpt": "A buyer's guide to die-cutting and laser-cutting ribbon in private-label programmes. Compares mechanical die-cutting, laser cutting and rotary knife cutting on edge quality, tolerance capability, tooling cost, unit economics and material compatibility, and sets out how to write a cut-part specification with a defined edge class, a realistic radius and a visible tooling line.",
        "aria": "Ribbon Die-Cutting and Laser Cutting mdash Edge Quality, Tolerance and Tooling Economics",
        "thumb": "linear-gradient(135deg,#b71c1c,#e64a19)",
    },
    {
        "slug": "ribbon-oem-flammability-fire-safety-compliance-specification-testing-private-label-buyers-guide-2026-10-29-am",
        "title": "Ribbon Flammability &amp; Fire Safety Compliance &mdash; How to Specify It, Test It and Document It for Private Label (2026)",
        "excerpt": "A buyer's guide to ribbon flammability and fire-safety compliance in private-label programmes. Maps the four test families and the standards behind them (EN 13773, NFPA 701, 16 CFR 1610, BS 5867, CAL 117), explains what construction changes invalidate a result, and sets out how to write a testable fire-performance specification with a re-test trigger.",
        "aria": "Ribbon Flammability and Fire Safety Compliance mdash How to Specify, Test and Document It",
        "thumb": "linear-gradient(135deg,#4a148c,#7b1fa2)",
    },
]

CARD_TMPL = """  <article class="blog-post-card" itemscope itemtype="https://schema.org/BlogPosting">
  <a href="blog-{slug}.html" class="blog-post-thumb" style="background:{thumb};" aria-label="{aria}"></a>
  <div class="blog-post-meta">
    <span class="blog-post-date" itemprop="datePublished" content="{date}">{date}</span>
    <span class="blog-post-category">B2B Sourcing</span>
  </div>
  <h3 class="blog-post-title" itemprop="headline"><a href="blog-{slug}.html">{title}</a></h3>
  <p class="blog-post-excerpt" itemprop="description">{excerpt}</p>
  <a class="blog-post-link" href="blog-{slug}.html">Read more &rarr;</a>
</article>
"""

# ---------- blog.html ----------
bp = ROOT / "blog.html"
blog = bp.read_text(encoding="utf-8")
anchor = None
for m in re.finditer(r'<article class="blog-post-card"[^>]*>', blog):
    anchor = m.start()
    break
if anchor is None:
    raise SystemExit("no blog-post-card found in blog.html")

n = 0
for art in ARTICLES:
    href = f"blog-{art['slug']}.html"
    if href in blog:
        print(f"[skip] blog.html already has {href[:60]}")
        continue
    card = CARD_TMPL.format(date=DATE, **art)
    blog = blog[:anchor] + card + blog[anchor:]
    anchor += len(card)
    n += 1
bp.write_text(blog, encoding="utf-8")
print(f"[ok] inserted {n} card(s) into blog.html")

# ---------- index.html ----------
ip = ROOT / "index.html"
idxh = ip.read_text(encoding="utf-8")
n = 0
for art in reversed(ARTICLES):  # newest first
    href = f"blog-{art['slug']}.html"
    if href in idxh:
        print(f"[skip] index.html already has {href[:60]}")
        continue
    link = f'<li><a href="{href}">{art["title"]}</a></li>'
    i = idxh.rfind("</li>")
    if i == -1:
        raise SystemExit("no </li> in index.html")
    i += len("</li>")
    idxh = idxh[:i] + "\n" + link + idxh[i:]
    n += 1
ip.write_text(idxh, encoding="utf-8")
print(f"[ok] inserted {n} link(s) into index.html")

# ================= VERIFY (single pass) =================
print("\n--- VERIFY ---")
sm_f = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ET.fromstring(sm_f)
blog_f = bp.read_text(encoding="utf-8")
idx_f = ip.read_text(encoding="utf-8")

ok = True
for art in ARTICLES:
    slug = art["slug"]
    fname = f"blog-{slug}.html"
    ap_path = ROOT / fname
    if not ap_path.exists():
        print(f"  [FAIL] missing file {fname}")
        ok = False
        continue
    ap = ap_path.read_text(encoding="utf-8")

    assert fname in blog_f, f"blog.html missing card for {slug}"
    assert fname in idx_f, f"index.html missing link for {slug}"
    assert f"https://{SITE}/{fname}" in sm_f, f"sitemap missing loc for {slug}"

    assert ap.count("<h1>") == 1, f"{fname}: h1 count {ap.count('<h1>')}"
    assert 'rel="canonical"' in ap, f"{fname}: no canonical"
    assert 'property="og:title"' in ap and 'property="og:image"' in ap, f"{fname}: OG missing"
    assert 'property="article:published_time"' in ap, f"{fname}: no published_time"
    assert 'name="twitter:card"' in ap, f"{fname}: twitter card missing"
    assert "<h2>Frequently Asked Questions</h2>" in ap, f"{fname}: no visible FAQ h2"
    assert "since 2004" in ap, f"{fname}: no 'since 2004'"
    assert "XXX-Module" not in ap, f"{fname}: placeholder leaked"
    assert "2026-10-29" in ap, f"{fname}: date missing"

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', ap, re.S)
    types = [json.loads(b).get("@type") for b in blocks]
    for required in ("Article", "BlogPosting", "FAQPage"):
        assert required in types, f"{fname}: no {required} schema (got {types})"

    nq = sum(len(json.loads(b)["mainEntity"]) for b in blocks
             if json.loads(b).get("@type") == "FAQPage")
    assert 5 <= nq <= 7, f"{fname}: FAQ question count {nq} outside 5-7"
    assert ap.count("<h3>") >= nq, f"{fname}: visible h3 {ap.count('<h3>')} < {nq}"

    missing = []
    for href in set(re.findall(r'href="([^"#][^"]*\.html)"', ap)):
        if href.startswith("http"):
            continue
        if not (ROOT / href).exists():
            missing.append(href)
    assert not missing, f"{fname}: dead internal links {missing}"

    words = len(re.sub(r"<[^>]+>", " ", ap).split())
    assert words >= 1200, f"{fname}: only {words} words"
    print(f"  [OK] {fname[:58]}")
    print(f"       words={words} schema={types} faqQ={nq} deadlinks=0")

locs = re.findall(r"<loc>(.*?)</loc>", sm_f)
assert len(locs) == len(set(locs)), f"duplicate sitemap locs {len(locs)} vs {len(set(locs))}"
missing_files = [l.replace(f"https://{SITE}/", "") for l in locs
                  if l.endswith(".html") and not (ROOT / l.replace(f"https://{SITE}/", "")).exists()]
print(f"\nSitemap: {len(locs)} locs, {len(locs)-len(set(locs))} dups, {len(missing_files)} missing files")

first = re.search(r'href="(blog-[^"]+\.html)"', blog_f)
print(f"First blog card: {first.group(1) if first else 'NONE'}")
print("VERIFY OK" if ok else "VERIFY HAD FAILURES")
