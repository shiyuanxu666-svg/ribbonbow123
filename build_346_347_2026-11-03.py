#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #346 (AM) and #347 (PM) — 2026-11-03 cron (afternoon run).

#346 AM: Private label ribbon agreement — product / supply / legal contract structure, exit provisions
#347 PM: Trim-set & co-packing economics — BOM, assembly states, packaging spec, cost leaks

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, KPI strip, CTA, footer. Matches house template from #330-#345.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-03"

ARTICLES = [
    {
        "no": 346,
        "slot": "am",
        "pubtime": "2026-11-03T08:00:00+08:00",
        "slug": ("blog-private-label-ribbon-agreement-contracts-product-supply-legal-ownership-tooling-exit-"
                 "brand-procurement-guide-2026-11-03-am"),
        "title": ("Private Label Ribbon Agreement Guide &mdash; Product, Supply and Legal Contracts, "
                  "Ownership, Tooling and Exit for Brand Owners (2026)"),
        "desc": ("How to structure a private label ribbon agreement: specify the product with measurable "
                 "tolerances, fix MOQ and price windows, protect artwork, tooling and colour recipes, and "
                 "write exit terms before you need them."),
        "keywords": ("private label ribbon agreement, ribbon supply agreement, OEM ribbon contract, "
                     "ribbon contract structure, ribbon supplier contract clauses, ribbon MOQ price protection, "
                     "ribbon tooling ownership, ribbon colour recipe ownership, ribbon artwork IP, "
                     "ribbon agreement exit provisions, ribbon remedy ladder, ribbon acceptance criteria, "
                     "custom ribbon contract template, B2B ribbon procurement contract, "
                     "private label trim supplier agreement, ribbon quality agreement terms"),
        "body": Path("/tmp/rb346_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb346_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Private Label Ribbon: The Contract That Decides Whether Your Brand Scales",
            "Contract One: The Product Specification",
            "Contract Two: The Supply Agreement",
            "Contract Three: Ownership, Tooling and Exit",
            "The Commercial Terms Worth Getting Right",
            "Five Mistakes That Cost Private Label Buyers the Most",
            "How These Terms Work in Practice",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, category buyers and procurement managers most often ask "
                      "us about private label ribbon agreements and supply contracts. If your question is not here, "
                      "ask us directly."),
        "cat": "B2B Sourcing",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
        "read": "19 min read",
        "kpi": [
            ("3", "contracts every private label ribbon agreement needs"),
            ("4", "elements of ownership that protect you if the programme ends"),
            ("90", "days, a workable price protection window for a growing brand"),
        ],
    },
    {
        "no": 347,
        "slot": "pm",
        "pubtime": "2026-11-03T13:00:00+08:00",
        "slug": ("blog-ribbon-trim-set-co-packing-economics-bill-of-materials-assembly-packaging-specification-"
                 "cost-model-private-label-buyers-guide-2026-11-03-pm"),
        "title": ("Ribbon Trim Set &amp; Co-Packing Economics &mdash; Bill of Materials, Assembly States and "
                  "Packaging Specification for Private Label Buyers (2026)"),
        "desc": ("How to control the economics of a custom ribbon trim set: structure the bill of materials, "
                 "understand the four assembly states, specify packaging as a cost document, and find where "
                 "margin actually leaks."),
        "keywords": ("ribbon trim set co-packing, ribbon co-packing economics, trim set bill of materials, "
                     "custom ribbon packaging assembly, ribbon gift set private label, ribbon bow assembly cost, "
                     "co-packed ribbon packaging supplier, ribbon trim set MOQ, ribbon packaging specification cost, "
                     "gift packaging OEM co-packing, ribbon assembly rework rate, custom trim set procurement, "
                     "B2B ribbon packaging buyer guide, ribbon carton configuration freight cube, "
                     "private label gift packaging trim programme"),
        "body": Path("/tmp/rb347_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb347_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Beyond the Ribbon: How Trim-Set and Co-Packing Economics Decide Whether Your Packaging Programme Works",
            "Start With the Bill of Materials, Not the Ribbon",
            "What Co-Packing Actually Changes",
            "The Packaging Specification Is a Cost Document",
            "Where Trim-Set Programmes Leak Money",
            "Planning a Trim-Set Launch",
            "How We Run Trim-Set Programmes",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, category buyers and procurement managers most often ask "
                      "us about ribbon trim sets, co-packing and custom packaging programmes. If your question is "
                      "not here, ask us directly."),
        "cat": "B2B Packaging",
        "accent": "#7d3c98",
        "accent2": "#a569bd",
        "read": "18 min read",
        "kpi": [
            ("4", "assembly states, each with its own cost"),
            ("15–25%", "typical landed cost increase moving to co-packed"),
            ("8", "steps in a trim-set launch sequence"),
        ],
    },
]


def esc_attr(s):
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))


def build(a):
    url = f"{BASE}/{a['slug']}.html"

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": ans}}
            for q, ans in a["faq"]
        ],
    }

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "@id": url + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog.html"},
            {"@type": "ListItem", "position": 3, "name": a["title"].split(" &mdash; ")[0], "item": url},
        ],
    }

    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["desc"],
        "author": {"@type": "Organization", "name": "Xiamen Smith Ribbon&Bow Co., Ltd.", "url": f"{BASE}/about.html"},
        "publisher": {"@type": "Organization", "name": "Xiamen Smith Ribbon&Bow Co., Ltd.", "url": BASE},
        "datePublished": DATE,
        "dateModified": DATE,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": a["keywords"],
        "inLanguage": "en-US",
    }

    blogposting_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": a["title"],
        "description": a["desc"],
        "image": f"{BASE}/img/banner.png",
        "author": {"@type": "Organization", "name": "Xiamen Smith Ribbon&Bow Co., Ltd.", "url": f"{BASE}/about.html"},
        "publisher": {
            "@type": "Organization",
            "name": "Xiamen Smith Ribbon&Bow Co., Ltd.",
            "url": BASE,
            "logo": {"@type": "ImageObject", "url": f"{BASE}/img/banner.png"},
        },
        "datePublished": DATE,
        "dateModified": DATE,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": a["keywords"],
        "articleSection": a["cat"],
        "wordCount": 3400,
        "inLanguage": "en-US",
    }

    faq_html = [f'<h2 id="faq">{a["faq_heading"]}</h2>', f'<p>{a["faq_intro"]}</p>']
    for i, (q, ans) in enumerate(a["faq"], 1):
        faq_html.append(
            f'<div class="faq-item" id="faq-{i}">\n'
            f'  <h3 class="faq-q">{i}. {esc_attr(q)}</h3>\n'
            f'  <p class="faq-a">{ans}</p>\n'
            f'</div>\n'
        )
    faq_block = "\n".join(faq_html)

    kpi_html = ['<div class="kpi-box" style="display:flex;gap:24px;flex-wrap:wrap;'
                f'background:#f4f8fc;border-left:4px solid {a["accent"]};padding:18px 22px;margin:28px 0;">']
    for val, label in a["kpi"]:
        kpi_html.append(
            '<div style="flex:1;min-width:170px;">'
            f'<div style="font-size:1.9rem;font-weight:700;color:{a["accent"]};">{val}</div>'
            f'<div style="font-size:0.92rem;color:#444;">{label}</div></div>'
        )
    kpi_html.append("</div>")
    kpi_block = "\n".join(kpi_html)

    toc_items = "\n".join(f"                <li>{t}</li>" for t in a["toc"])
    toc_block = (
        '        <div class="toc">\n'
        '            <h3>Table of Contents</h3>\n'
        '            <ol>\n'
        f'{toc_items}\n'
        f'                <li>{a["faq_heading"]}</li>\n'
        '            </ol>\n'
        '        </div>\n'
    )

    if a["no"] == 346:
        cta_body = (
            'Smith Ribbon has been manufacturing ribbon, bows, tassels and decorative trim in Xiamen since 2004, '
            'with our own 15,000 m&sup2; factory, more than 200 employees, daily output of 100,000 metres, and '
            'certification including OEKO-TEX, FSC, BSCI, SEDEX/SMETA and ISO 9001. We ship to more than 50 countries '
            'and support OEM and ODM customisation from 1,000 metres, with small-batch runs from 500 metres.'
        )
        cta_second = (
            'Whether you need a supply agreement reviewed before you sign it, a specification rewritten so that '
            'every attribute carries a unit and a tolerance, an exit clause set drafted for your volume profile, or '
            'a colour and sample ladder built around your approval process, send us the details and we will tell you '
            'plainly what is required and what it costs.'
        )
    else:
        cta_body = (
            'Smith Ribbon has been manufacturing ribbon, bows, tassels and decorative trim in Xiamen since 2004, '
            'with our own 15,000 m&sup2; factory, more than 200 employees, daily output of 100,000 metres, and '
            'certification including OEKO-TEX, FSC, BSCI, SEDEX/SMETA and ISO 9001. We ship to more than 50 countries '
            'and support OEM and ODM customisation from 1,000 metres, with small-batch runs from 500 metres.'
        )
        cta_second = (
            'Whether you need a bill of materials built for your trim set, an assembly state and pricing model '
            'compared across two or three suppliers, a packaging specification reviewed for cost, or a pilot run '
            'through our own assembly line with the rework rate measured, send us the details and we will tell you '
            'plainly what is required and what it costs.'
        )

    cta_block = (
        '\n<hr>\n'
        '<h2>Talk to Us About Your Programme</h2>\n'
        f'<p>{cta_body}</p>\n'
        f'<p>{cta_second}</p>\n'
        '<p><strong>Email:</strong> <a href="mailto:xmmsd@126.com">xmmsd@126.com</a> &nbsp;|&nbsp; '
        '<strong>Mobile / WeChat:</strong> <a href="tel:+8613779951780">+86 137 7995 1780</a> &nbsp;|&nbsp; '
        '<strong>Office:</strong> +86-592-5095373</p>\n'
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{a["title"]}</title>
    <meta name="description" content="{esc_attr(a["desc"])}">
    <meta name="keywords" content="{esc_attr(a["keywords"])}">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN-35" />
    <meta name="geo.placename" content="Xiamen, Fujian, China" />
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{a["title"]}">
    <meta property="og:description" content="{esc_attr(a["desc"])}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{BASE}/img/banner.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="Ribbon OEM manufacturing and procurement guide from Smith Ribbon, Xiamen">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{a["pubtime"]}">
    <meta property="article:modified_time" content="{a["pubtime"]}">
    <meta property="article:author" content="Xiamen Smith Ribbon&amp;Bow Co., Ltd.">
    <meta property="article:section" content="{a["cat"]}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{a["title"]}">
    <meta name="twitter:description" content="{esc_attr(a["desc"])}">
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
        <h1>{a["title"]}</h1>
        <p class="meta">By Xiamen Smith Ribbon&amp;Bow Co., Ltd. | Published November 3, 2026 | Category: {a["cat"]} | Article #{a["no"]}</p>
{toc_block}
{kpi_block}
{a["body"]}

{cta_block}
{faq_block}
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

    out = ROOT / f"{a['slug']}.html"
    out.write_text(html, encoding="utf-8")
    body_words = len(re.sub(r"<[^>]+>", " ", a["body"]).split())
    visible = len(re.sub(r"<[^>]+>", " ", html).split())
    print(f"[OK] {out.name}")
    print(f"     body_words={body_words} visible_words={visible} faq={len(a['faq'])}")


if __name__ == "__main__":
    for a in ARTICLES:
        build(a)
