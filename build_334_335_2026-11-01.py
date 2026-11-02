#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #334 (AM) and #335 (PM) — 2026-11-01 cron.

#334 AM: Private label ribbon programme — from brief to repeat order
#335 PM: Ribbon landed cost & cost analysis for brand owners

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, CTA, footer. Matches house template from #330/#331.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-01"

ARTICLES = [
    {
        "no": 334,
        "slot": "am",
        "pubtime": "2026-11-01T08:00:00+08:00",
        "slug": ("blog-private-label-ribbon-programme-guide-brief-samples-approval-gates-reorder-economics-"
                 "packaging-documentation-metrics-private-label-buyers-guide-2026-11-01-am"),
        "title": ("Private Label Ribbon Programme Guide &mdash; From Development Brief to Repeat Order: Samples, "
                  "Approval Gates, Reorder Economics, Packaging and Documentation for Brand Owners (2026)"),
        "desc": ("A practical guide to structuring a private label ribbon and decorative trim programme as a "
                 "repeatable supply programme rather than a series of purchase orders. Covers the four private "
                 "label models and how each changes the specification, what a development brief must contain, how "
                 "to run the sample ladder without approving the wrong thing, how to build an approval gate "
                 "schedule with named owners, reorder economics including MOQ exposure per SKU and tooling "
                 "amortisation, packaging specification, the documentation set to fix before the first shipment, "
                 "the programme metrics worth tracking, and where private label programmes usually come apart."),
        "keywords": ("private label ribbon programme, ribbon OEM programme guide, private label ribbon buyer guide, "
                     "ribbon development brief, ribbon sample approval, ribbon approval gates, ribbon reorder "
                     "economics, ribbon MOQ exposure, ribbon packaging specification, ribbon artwork ownership, "
                     "ribbon private label documentation, B2B ribbon procurement guide, custom ribbon programme, "
                     "ribbon supplier programme management, private label trim sourcing"),
        "body": Path("/tmp/rb334_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb334_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Private Label Ribbon: A Programme, Not a Purchase",
            "Step One: Define the Programme, Not the Order",
            "Step Two: A Brief That Survives Contact With a Factory",
            "Step Three: Run the Sample Ladder Deliberately",
            "Step Four: Put Gates in the Schedule, Not in the Inbox",
            "Step Five: Understand the Reorder Economics",
            "Step Six: Treat Packaging as Part of the Product",
            "Step Seven: Fix the Documentation Before the First Shipment",
            "Step Eight: Measure the Programme, Not the Shipment",
            "Step Nine: Scaling Without Losing Control",
            "Where Programmes Usually Come Apart",
            "A Working Programme, End to End",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners and procurement managers most often ask us about running "
                      "a private label ribbon programme. If your question is not here, ask us directly."),
        "cat": "B2B Sourcing",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
        "read": "25 min read",
        "kpi": [
            ("4", "private label models, and how each changes the spec"),
            ("4", "stages in a deliberate sample ladder"),
            ("8-12", "weeks, brief to first shipment on a new programme"),
        ],
    },
    {
        "no": 335,
        "slot": "pm",
        "pubtime": "2026-11-01T13:00:00+08:00",
        "slug": ("blog-ribbon-landed-cost-model-cost-analysis-12-components-tariff-freight-working-capital-"
                 "quality-loss-oem-brand-procurement-2026-11-01-pm"),
        "title": ("Ribbon Landed Cost &amp; Cost Analysis &mdash; The 12 Components of a Defensible Model, "
                  "Tariff, Freight, Working Capital and Quality Loss for OEM Brand Owners (2026)"),
        "desc": ("A working cost model for buying ribbon and decorative trim, and why the quoted factory price "
                 "is often less than half of the delivered cost. Covers all twelve landed cost components from "
                 "ex-works value to internal conversion labour, how to read a factory's cost structure out of the "
                 "quotation itself, where the money actually goes on a typical programme, how to compare two "
                 "valid quotations on a normalised basis, the cost-reduction levers that actually move the "
                 "number, and how to keep the model current as terms and tariffs change."),
        "keywords": ("ribbon landed cost model, ribbon cost analysis, ribbon OEM costing, import duty ribbon, "
                     "ribbon freight cost calculation, ribbon total landed cost, ribbon working capital cost, "
                     "ribbon cost comparison quotes, private label ribbon costing, B2B ribbon procurement guide, "
                     "ribbon unit economics, ribbon TCO decoder, OEM ribbon price negotiation, brand owner "
                     "ribbon cost model, ribbon packaging cost, ribbon quality cost of poor quality"),
        "body": Path("/tmp/rb335_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb335_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "The Price You Were Quoted Is Not the Price You Will Pay",
            "Build the Model in Two Currencies",
            "The Cost Components, Line by Line",
            "Reading a Factory's Cost Structure",
            "Where the Money Actually Goes",
            "Reducing Cost Where It Actually Moves",
            "Comparing Two Quotations Properly",
            "Keeping the Model Alive",
            "The Bottom Line",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions finance, procurement and sourcing teams most often ask us about "
                      "ribbon cost analysis and landed cost modelling. If your question is not here, ask us directly."),
        "cat": "Cost & Pricing",
        "accent": "#b9770e",
        "accent2": "#e0a458",
        "read": "24 min read",
        "kpi": [
            ("12", "landed cost components in the model"),
            ("3", "cost levers that move more than price negotiation"),
            ("30%", "typical gap between two valid quotations, before normalising"),
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
        "wordCount": 4600,
        "inLanguage": "en-US",
    }

    # visible FAQ block
    faq_html = [f'<h2 id="faq">{a["faq_heading"]}</h2>', f'<p>{a["faq_intro"]}</p>']
    for i, (q, ans) in enumerate(a["faq"], 1):
        faq_html.append(
            f'<div class="faq-item" id="faq-{i}">\n'
            f'  <h3 class="faq-q">{i}. {esc_attr(q)}</h3>\n'
            f'  <p class="faq-a">{ans}</p>\n'
            f'</div>\n'
        )
    faq_block = "\n".join(faq_html)

    # KPI strip
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

    cta_block = (
        '\n<hr>\n'
        '<h2>Talk to Us About Your Programme</h2>\n'
        '<p>Smith Ribbon has been manufacturing ribbon, bows, tassels and decorative trim in Xiamen since 2004, '
        'with our own 15,000 m&sup2; factory, more than 200 employees, daily output of 100,000 metres, and '
        'certification including OEKO-TEX, FSC, BSCI, SEDEX/SMETA and ISO 9001. We ship to more than 50 countries '
        'and support OEM and ODM customisation from 1,000 metres, with small-batch runs from 500 metres.</p>\n'
        '<p>Whether you need a development brief reviewed, a landed cost model built for your programme, or a '
        'comparable quotation across several mills, send us the details and we will tell you plainly what is '
        'required and what it costs.</p>\n'
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
    <meta property="og:image:alt" content="Ribbon OEM manufacturing and private label sourcing guide from Smith Ribbon, Xiamen">
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
        <p class="meta">By Xiamen Smith Ribbon&amp;amp;Bow Co., Ltd. | Published November 1, 2026 | Category: {a["cat"]} | Article #{a["no"]}</p>
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
