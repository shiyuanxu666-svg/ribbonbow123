#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #330 (AM) and #331 (PM) — 2026-10-31 cron.

#330 AM: Ribbon OEM Development Brief — the 12 fields that make quotes comparable
#331 PM: Reading & Verifying Ribbon Certifications — scope, currency, bridge to SKU

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, CTA, footer. Matches house template from #329.
"""
from pathlib import Path
import json

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-10-31"

ARTICLES = [
    {
        "no": 330,
        "slot": "am",
        "pubtime": "2026-10-31T08:00:00+08:00",
        "slug": ("blog-ribbon-oem-development-brief-12-fields-comparable-quotes-request-for-quotation-"
                 "specification-guide-b2b-brand-procurement-2026-10-31-am"),
        "title": ("How to Write a Ribbon OEM Development Brief That Gets You Comparable Quotes &mdash; "
                  "12 Fields, Specification Guide and How to Read the Responses (2026)"),
        "desc": ("A practical guide to writing a ribbon OEM development brief so quotations are actually "
                 "comparable. Covers the 12 fields every brief needs (construction and material, width "
                 "and tolerance, decoration method, colour reference and approval route, certification, "
                 "format and packaging, firm order plus forecast, target price and retail price, Incoterms "
                 "and destination, required-on-shelf date, sampling expectations, artwork and tooling "
                 "ownership), why two quotes for the same product differ by 30 percent, how to read factory "
                 "responses, and the mistakes that cost buyers the most money."),
        "keywords": ("ribbon OEM development brief, ribbon request for quotation, how to brief a ribbon factory, "
                     "ribbon OEM specification guide, ribbon quote comparison, private label ribbon brief, "
                     "ribbon sourcing RFQ, ribbon OEM quote template, ribbon factory quotation guide, "
                     "ribbon OEM buyer guide, ribbon private label procurement, custom ribbon brief, "
                     "ribbon sourcing specification sheet, B2B ribbon procurement guide, ribbon OEM costing questions"),
        "body": Path("/tmp/rb330_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb330_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Why Two Quotes for \u201cThe Same Ribbon\u201d Differ by 30 Percent",
            "The Twelve Fields Every Ribbon Development Brief Needs",
            "What a Complete Brief Looks Like in Practice",
            "Reading the Responses You Get Back",
            "Common Mistakes That Cost Buyers Money",
            "Getting a Second Round of Clarification Right",
            "A Working Timeline for a First Programme",
            "Why Factories Prefer Complete Briefs",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners and procurement managers most often ask us about "
                      "OEM ribbon briefs and quotations. If your question is not here, ask us directly."),
        "cat": "B2B Sourcing",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
        "read": "24 min read",
        "kpi": [
            ("12", "fields required in a complete ribbon OEM brief"),
            ("3-5", "factories to send an identical brief to"),
            ("8-12", "weeks, brief to first shipment, typical first programme"),
        ],
    },
    {
        "no": 331,
        "slot": "pm",
        "pubtime": "2026-10-31T13:00:00+08:00",
        "slug": ("blog-ribbon-oem-certification-reading-verifying-scope-currency-oeko-tex-fsc-bsci-smeta-iso-9001-grs-"
                 "chain-of-custody-private-label-buyers-guide-2026-10-31-pm"),
        "title": ("How to Read and Verify Ribbon Factory Certifications &mdash; Scope, Currency, OEKO-TEX, FSC, "
                  "BSCI, SMETA, ISO 9001 and GRS for Private Label Buyers (2026)"),
        "desc": ("How to read and verify the certifications on your ribbon supplier's file rather than tick a "
                 "box. Covers what a certificate actually proves, the four conditions that fail independently "
                 "(scope, holder, facility, validity), OEKO-TEX Standard 100 product classes I to IV and ECO "
                 "PASSPORT, FSC chain of custody and claim types, what ISO 9001 does not prove, BSCI versus "
                 "SMETA versus SEDEX, GRS and GOTS recycled content transaction certificates, a five-step "
                 "verification routine, and the supply agreement clauses that keep credentials current."),
        "keywords": ("ribbon OEM certification verification, OEKO-TEX Standard 100 ribbon, ECO PASPORT ribbon, "
                     "FSC chain of custody packaging, ISO 9001 ribbon factory, BSCI audit ribbon supplier, "
                     "SMETA SEDEX social compliance, GRS recycled content ribbon, ribbon supplier compliance, "
                     "ribbon certification scope check, OEKO-TEX product class, private label compliance ribbon, "
                     "ribbon supplier verification checklist, B2B ribbon compliance guide, ribbon certification scope expiry"),
        "body": Path("/tmp/rb331_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb331_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "What a Certificate Actually Proves, and What It Does Not",
            "OEKO-TEX Standard 100: The One That Matters Most",
            "FSC: Paper Components and the Chain of Custody",
            "ISO 9001: The Quality System, Not the Product",
            "BSCI, SMETA and SEDEX: Social Compliance",
            "GRS and GOTS: Recycled Content Claims",
            "Other Credentials You Will Meet",
            "A Verification Routine That Scales",
            "What to Put in Your Supply Agreement",
            "When a Certificate Is Genuinely Absent",
            "Asking the Right Questions of Your Supplier",
            "The Real Purpose of Verification",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions procurement and compliance teams most often ask us about "
                      "supplier certificates and how to verify them. If your question is not here, ask us directly."),
        "cat": "B2B Sourcing",
        "accent": "#7b2cbf",
        "accent2": "#a569bd",
        "read": "26 min read",
        "kpi": [
            ("7", "items to request from any supplier for each certificate"),
            ("5", "steps in a verification routine that scales"),
            ("60", "days before expiry, when you should re-verify"),
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
                'background:#f4f8fc;border-left:4px solid #1a5276;padding:18px 22px;margin:28px 0;">']
    for val, label in a["kpi"]:
        kpi_html.append(
            '<div style="flex:1;min-width:170px;">'
            f'<div style="font-size:1.9rem;font-weight:700;color:#1a5276;">{val}</div>'
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
        '<p>Whether you need a development brief reviewed, a comparable quotation across several mills, or a '
        'certification scope checked against your compliance requirements, send us the details and we will tell '
        'you plainly what is required and what it costs.</p>\n'
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
        <p class="meta">By Xiamen Smith Ribbon&amp;amp;Bow Co., Ltd. | Published October 31, 2026 | Category: {a["cat"]} | Article #{a["no"]}</p>
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
    print(f"[OK] {out.name}")
    print(f"     body_words={body_words} total_words={len(html.split())} faq={len(a['faq'])}")


import re

if __name__ == "__main__":
    for a in ARTICLES:
        build(a)
