#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B article #329 - 2026-10-30 cron 15:00 (PM).

Topic: How to Store Ribbon So It Still Performs Months Later
        - storage conditions (temperature, RH, light)
        - the four storage-sensitive properties (moisture, colour/bloom, drape, integrity)
        - stacking, winding, roll geometry, FIFO
        - packing decisions made at the mill that determine the warehouse outcome
        - recovering stock stored badly
        - building storage clauses into the quality agreement

House template follows article #314: full meta + OG + Twitter,
Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD, visible FAQ block,
KPI box, CTA section, footer.
"""
from pathlib import Path
import json

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-10-30"
SLOT = "pm"
PUBTIME = "2026-10-30T15:00:00+08:00"
ARTICLE_NO = 329

SLUG = ("blog-ribbon-oem-ribbon-storage-shelf-life-warehouse-conditions-temperature-humidity-light-"
        "bloom-differential-fifo-rotation-recovering-damaged-stock-b2b-brand-procurement-"
        "2026-10-30-pm")

TITLE = ("How to Store Ribbon So It Still Performs Months Later &mdash; Warehouse Conditions, " +
         "Shelf Life, FIFO Rotation and Recovering Damaged Stock (2026)")

DESC = ("A buyer's guide to storing ribbon so it still performs months after delivery. Covers the four " +
        "properties that storage damages and in what order, the temperature and humidity range that keeps " +
        "ribbon stable, why satin goes dull in storage and why it cannot be fixed, how to stack and rotate " +
        "rolls, which packing decisions at the mill determine your warehouse outcome, how to recover stock " +
        "stored badly instead of writing it off, and the eight storage clauses to put in your supply " +
        "agreement.")

KEYWORDS = ("ribbon storage, ribbon shelf life, ribbon warehouse conditions, ribbon storage temperature, " +
            "ribbon humidity storage, satin ribbon bloom, ribbon FIFO rotation, ribbon roll stacking, " +
            "ribbon moisture barrier packaging, ribbon colour fading storage, ribbon stock recovery, " +
            "ribbon inventory storage best practice, how to store ribbon, ribbon storage specification, " +
            "B2B ribbon procurement storage, ribbon handling and storage guide")

BODY = Path("/tmp/rb_body.html").read_text(encoding="utf-8")
FAQ = json.loads(Path("/tmp/rb_faq.json").read_text(encoding="utf-8"))

URL = f"{BASE}/{SLUG}.html"


def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in FAQ
    ],
}

breadcrumb = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "@id": URL + "#breadcrumb",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog.html"},
        {"@type": "ListItem", "position": 3, "name": SLUG.replace("-", " "), "item": URL},
    ],
}

article_schema = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": TITLE,
    "description": DESC,
    "author": {
        "@type": "Organization",
        "name": "Xiamen Smith Ribbon&Bow Co., Ltd.",
        "url": f"{BASE}/about.html",
    },
    "publisher": {
        "@type": "Organization",
        "name": "Xiamen Smith Ribbon&Bow Co., Ltd.",
        "url": BASE,
    },
    "datePublished": DATE,
    "dateModified": DATE,
    "mainEntityOfPage": {"@type": "WebPage", "@id": URL},
    "keywords": KEYWORDS,
}

blogposting_schema = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": TITLE,
    "description": DESC,
    "image": f"{BASE}/img/banner.png",
    "author": {
        "@type": "Organization",
        "name": "Xiamen Smith Ribbon&Bow Co., Ltd.",
        "url": f"{BASE}/about.html",
    },
    "publisher": {
        "@type": "Organization",
        "name": "Xiamen Smith Ribbon&Bow Co., Ltd.",
        "url": BASE,
        "logo": {"@type": "ImageObject", "url": f"{BASE}/img/banner.png"},
    },
    "datePublished": DATE,
    "dateModified": DATE,
    "mainEntityOfPage": {"@type": "WebPage", "@id": URL},
    "keywords": KEYWORDS,
    "articleSection": "B2B Sourcing",
    "wordCount": 5200,
    "inLanguage": "en-US",
}

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE}</title>
    <meta name="description" content="{esc_attr(DESC)}">
    <meta name="keywords" content="{esc_attr(KEYWORDS)}">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN-35" />
    <meta name="geo.placename" content="Xiamen, Fujian, China" />
    <link rel="canonical" href="{URL}">
    <meta property="og:title" content="{TITLE}">
    <meta property="og:description" content="{esc_attr(DESC)}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{BASE}/img/banner.png">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:url" content="{URL}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{PUBTIME}">
    <meta property="article:modified_time" content="{PUBTIME}">
    <meta property="article:author" content="Xiamen Smith Ribbon&amp;Bow Co., Ltd.">
    <meta property="article:section" content="B2B Sourcing">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{TITLE}">
    <meta name="twitter:description" content="{esc_attr(DESC)}">
    <meta name="twitter:image" content="{BASE}/img/banner.png">
    <script type="application/ld+json">
{json.dumps(article_schema, indent=4, ensure_ascii=False)}
    </script>
    <script type="application/ld+json">
{json.dumps(blogposting_schema, indent=4, ensure_ascii=False)}
    </script>
    <script type="application/ld+json">
{json.dumps(faq_schema, indent=4, ensure_ascii=False)}
    </script>
    <script type="application/ld+json">
{json.dumps(breadcrumb, indent=4, ensure_ascii=False)}
    </script>
</head>
<body>
    <nav>
        <div class="logo">Smith Ribbon</div>
        <div><a href="https://ribbonbow123.com/">Home</a> | <a href="https://ribbonbow123.com/blog.html">Blog</a> | <a href="https://ribbonbow123.com/about.html">About</a></div>
    </nav>
    <div class="container">
        <h1>{TITLE}</h1>
        <p class="meta">By Xiamen Smith Ribbon&amp;amp;Bow Co., Ltd. | Published October 30, 2026 | Category: B2B Sourcing | Article #{ARTICLE_NO}</p>
        <div class="toc">
            <h3>Table of Contents</h3>
            <ol>
                <li>Why Ribbon Is More Vulnerable in Storage Than Most Buyers Expect</li>
                <li>Temperature and Humidity: The Two Numbers That Matter Most</li>
                <li>Light: The Only Exposure You Cannot Correct Later</li>
                <li>Stacking, Winding and the Physics of a Stored Roll</li>
                <li>Packing: A Factory Decision That Determines Your Storage Outcome</li>
                <li>Recovering Stock That Has Been Stored Badly</li>
                <li>Building Storage Conditions Into the Supply Agreement</li>
                <li>Frequently Asked Questions</li>
            </ol>
        </div>

{BODY}
    </div>
    <footer>
        <p>&copy; 2026 Smith Ribbon Co., Ltd. (Xiamen Meisida Decoration Co., Ltd.) | OEM &amp; ODM Custom Ribbon Manufacturer</p>
        <p>
            <a href="https://ribbonbow123.com/">Home</a>
            <a href="https://ribbonbow123.com/blog.html">Blog</a>
            <a href="https://ribbonbow123.com/about.html">About</a>
            <a href="mailto:xmmsd@126.com">Contact</a>
        </p>
    </footer>
</body>
</html>
"""

out = ROOT / f"{SLUG}.html"
out.write_text(html, encoding="utf-8")
print(f"[OK] {out.name}")
print(f"     words={len(html.split())} chars={len(html)}")
