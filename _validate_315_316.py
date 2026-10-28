#!/usr/bin/env python3
"""Validate the two 2026-10-28 ribbonbow123 articles before commit."""
import re
import json

PAIRS = [
    ("ribbon-oem-elastic-stretch-recovery-compression-specification-private-label-buyers-guide-2026-10-28-am", "#315 AM elastic"),
    ("ribbon-oem-fragrance-beauty-packaging-trim-atomiser-collar-cap-tie-decoration-compliance-b2b-brand-procurement-2026-10-28-pm", "#316 PM beauty"),
]

DQ = chr(34)

for slug, label in PAIRS:
    h = open(f"/workspace/ribbonbow123/blog-{slug}.html", encoding="utf-8").read()
    m = re.search(r'<div class="container">(.*?)</div>\s*<footer>', h, re.S)
    body = m.group(1)
    txt = re.sub(r"<[^>]+>", " ", body)
    wc = len(txt.split())

    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    types = []
    for s in schemas:
        types.append(json.loads(s).get("@type"))

    faq_html = re.search(r'<div class="faq">(.*?)</div>', h, re.S).group(1)
    n_faq = len(re.findall(r"<h3>", faq_html))
    n_h2 = len(re.findall(r"<h2>", body))

    checks = {
        "title": "<title>" in h,
        "meta_description": ('name=' + DQ + 'description' + DQ) in h,
        "meta_keywords": ('name=' + DQ + 'keywords' + DQ) in h,
        "meta_robots": ('name=' + DQ + 'robots' + DQ) in h,
        "canonical": "rel=" + DQ + 'canonical' + DQ in h,
        "og_title": ("og:title" in h),
        "og_description": ("og:description" in h),
        "og_image": ("og:image" in h),
        "og_url": ("og:url" in h),
        "og_type": ("og:type" in h),
        "published_time": ("article:published_time" in h),
        "modified_time": ("article:modified_time" in h),
        "twitter_card": ("twitter:card" in h),
        "geo": ("geo.region" in h),
    }
    failed = [k for k, v in checks.items() if not v]

    print(f"=== {label} ===")
    print(f"  slug: {slug[:70]}")
    print(f"  words: {wc}  (target 1200+)  -> {'PASS' if wc >= 1200 else 'FAIL'}")
    print(f"  h2 sections: {n_h2}   FAQ items: {n_faq}  -> {'PASS' if 5 <= n_faq <= 7 else 'FAIL'}")
    print(f"  schema types: {types}")
    ok_schema = "BlogPosting" in types and "FAQPage" in types
    print(f"  BlogPosting+FAQPage -> {'PASS' if ok_schema else 'FAIL'}")
    print(f"  meta/OG checks: {'ALL PASS' if not failed else 'FAILED: ' + str(failed)}")
    print(f"  since 2004 present: {'since 2004' in h}")
    print(f"  bad-year check (2019/2021/2023 fabrications): "
          f"{[y for y in ['2019','2021','2023','2025 '] if y in txt]}")
    print()

print("ALL VALIDATIONS DONE")
