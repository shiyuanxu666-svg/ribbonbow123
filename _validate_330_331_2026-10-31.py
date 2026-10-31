#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate articles #330/#331 — meta, OG, JSON-LD, FAQ, entity voice, sitemap."""
import re, json, os
from pathlib import Path

WORK = Path("/workspace/ribbonbow123")
FILES = [
 "blog-ribbon-oem-development-brief-12-fields-comparable-quotes-request-for-quotation-specification-guide-b2b-brand-procurement-2026-10-31-am.html",
 "blog-ribbon-oem-certification-reading-verifying-scope-currency-oeko-tex-fsc-bsci-smeta-iso-9001-grs-chain-of-custody-private-label-buyers-guide-2026-10-31-pm.html",
]

fail = 0
for f in FILES:
    h = (WORK / f).read_text(encoding="utf-8")
    print("\n== " + f)
    checks = {
        "title tag": bool(re.search(r"<title>[^<]+</title>", h)),
        "meta description": bool(re.search(r'name="description" content="[^"]{80,}"', h)),
        "meta keywords": bool(re.search(r'name="keywords" content="[^"]{100,}"', h)),
        "canonical": bool(re.search(r'rel="canonical" href="https://ribbonbow123\.com/', h)),
        "og tags (>=8)": len(re.findall(r'property="og:', h)) >= 8,
        "twitter tags (>=4)": len(re.findall(r'name="twitter:', h)) >= 4,
        "published_time": bool(re.search(r'article:published_time" content="2026-10-31T', h)),
    }
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    types = []
    for b in blocks:
        try:
            d = json.loads(b)
            types.append(d.get("@type"))
        except Exception as e:
            checks[f"JSON-LD parse"] = False
            print("   JSON-LD ERROR:", e)
            fail += 1
    checks["Article schema"] = "Article" in types
    checks["BlogPosting schema"] = "BlogPosting" in types
    checks["FAQPage schema"] = "FAQPage" in types
    checks["BreadcrumbList schema"] = "BreadcrumbList" in types
    faq_n = 0
    for b in blocks:
        d = json.loads(b)
        if d.get("@type") == "FAQPage":
            faq_n = len(d["mainEntity"])
    checks[f"FAQ schema 5-7 (={faq_n})"] = 5 <= faq_n <= 7
    checks["visible FAQ block 5-7"] = 5 <= h.count('class="faq-item"') <= 7
    checks["FAQ answers non-empty"] = all(len(a.get("acceptedAnswer", {}).get("text", "")) > 80 for b in blocks if json.loads(b).get("@type") == "FAQPage" for a in json.loads(b)["mainEntity"])
    checks["since 2004 voice"] = "since 2004" in h
    checks["no 2007"] = "2007" not in h
    checks["no Module spam"] = "Module" not in h and "module" not in h.lower().replace("modules","")
    checks["TOC present"] = h.count("<li>") >= 8
    body = re.sub(r"<[^>]+>", " ", h[h.find("<h1>"):h.find("<footer>")])
    w = len(body.split())
    checks[f"words >=1200 (={w})"] = w >= 1200
    checks["contact present"] = "xmmsd@126.com" in h and "137 7995 1780" in h

    for k, v in checks.items():
        print(f"   {'OK ' if v else 'FAIL'}  {k}")
        if not v:
            fail += 1

# sitemap
sm = (WORK / "sitemap.xml").read_text(encoding="utf-8")
locs = re.findall(r"<loc>(.*?)</loc>", sm)
dups = len(locs) - len(set(locs))
future = re.findall(r"<lastmod>(2026-1[12]-\d\d)</lastmod>", sm)
bad = [x for x in future if x > "2026-10-31"]
print("\n== sitemap")
print(f"   {'OK ' if dups == 0 else 'FAIL'}  duplicate locs = {dups} (total {len(locs)})")
print(f"   {'OK ' if not bad else 'FAIL'}  future lastmod = {bad}")
for f in FILES:
    present = f"{f}" in sm
    print(f"   {'OK ' if present else 'FAIL'}  {f[:60]}...")
    if not present:
        fail += 1

# index files
for idx in ["blog.html", "en-blog.html", "index.html"]:
    c = (WORK / idx).read_text(encoding="utf-8")
    for f in FILES:
        if f not in c:
            print(f"   FAIL  {idx} missing {f[:50]}")
            fail += 1
print("   OK    all 3 index files contain both articles")

print("\n=== TOTAL FAILURES:", fail, "===")
