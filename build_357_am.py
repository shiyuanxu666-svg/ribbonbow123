#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B article #357 (AM, 08:00 slot) — 2026-11-06 cron.

#357 AM: OEM Custom Packaging & Private-Label Ribbon Programme Guide — the nine
         fields a factory cannot guess, the five-step sample ladder, artwork and
         tooling ownership, decoration method selection for costing, MOQ and cost
         drivers, first-order readiness checklist, agreement structure.

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, KPI strip, CTA, footer. Matches house template #330-#356.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-06"
DATE_LONG = "November 6, 2026"

ARTICLES = [
    {
        "no": 357,
        "slot": "am",
        "pubtime": "2026-11-06T08:00:00+08:00",
        "slug": ("blog-oem-custom-packaging-private-label-ribbon-programme-guide-nine-field-brief-"
                 "sample-ladder-artwork-ownership-decoration-method-moq-cost-drivers-first-order-"
                 "readiness-checklist-private-label-buyers-guide-2026-11-06-am"),
        "title": ("OEM Custom Packaging &amp; Private-Label Ribbon Programme Guide &mdash; The Nine-Field "
                  "Brief, Sample Ladder and First-Order Readiness Checklist (2026)"),
        "desc": ("How to build an OEM custom ribbon and packaging programme: the nine specification fields "
                 "a factory cannot guess, a five-step sample ladder, artwork and tooling ownership rules, "
                 "decoration method selection, MOQ cost drivers and a first-order readiness checklist."),
        "keywords": ("OEM custom packaging, private label ribbon programme, ribbon OEM brief, ribbon "
                     "sample ladder, golden sample ribbon, artwork ownership ribbon OEM, ribbon "
                     "decoration method selection, ribbon MOQ cost drivers, private label packaging "
                     "guide, ribbon factory development brief, OEM ribbon first order checklist, "
                     "custom printed ribbon specification, private label ribbon buyer guide, ribbon "
                     "tooling ownership, B2B ribbon OEM programme"),
        "body": Path("/tmp/rb357_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb357_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "What an OEM Packaging Programme Actually Is",
            "The Nine Fields a Factory Cannot Guess",
            "The Sample Ladder: Five Steps, Each Proving a Different Thing",
            "Artwork and Ownership: Get This Right Before You Print",
            "Choosing a Decoration Method You Can Actually Cost",
            "MOQ and the Cost Drivers Behind Your Unit Price",
            "Building the First Order: A Readiness Checklist",
            "How to Structure the Agreement",
            "Common Mistakes and How to Avoid Them",
            "What a Good First Conversation Looks Like",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, procurement managers and private-label "
                      "buyers most often ask us about setting up an OEM custom ribbon and packaging "
                      "programme, from MOQ and artwork ownership to colour tolerance and sample "
                      "approval. If your question is not here, ask us directly."),
        "cat": "B2B OEM Guides",
        "accent": "#1f4e79",
        "accent2": "#2e75b6",
        "read": "18 min read",
        "kpi": [
            ("9", "specification fields a factory cannot guess"),
            ("5", "sample steps, each proving a different thing"),
            ("45-70", "days from complete brief to shipment"),
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
        "itemElement": [
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
        "wordCount": 3600,
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

    cta_body = (
        'Smith Ribbon has been manufacturing ribbon, bows, tassels and decorative trim in Xiamen since 2004, '
        'with our own 15,000 m&sup2; factory, more than 200 employees, daily output of 100,000 metres, and '
        'certification including OEKO-TEX, FSC, BSCI, SEDEX/SMETA and ISO 9001. We ship to more than 50 countries '
        'and support OEM and ODM customisation from 1,000 metres, with small-batch runs from 500 metres.'
    )
    cta_second = (
        'Whether you need a nine-field development brief built out for your specific programme, a sample '
        'ladder structured so each step proves the right thing, artwork and tooling ownership terms that '
        'let you leave later without rebuilding your brand, a decoration method recommendation you can '
        'actually cost, or a first-order readiness review before you commit a launch date, send us the '
        'details and we will tell you plainly what is required and what it costs.'
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
    <meta property="og:image:alt" content="OEM custom packaging and private-label ribbon programme guide from Smith Ribbon, Xiamen">
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
        <p class="meta">By Xiamen Smith Ribbon&amp;Bow Co., Ltd. | Published {DATE_LONG} | Category: {a["cat"]} | Article #{a["no"]}</p>
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
