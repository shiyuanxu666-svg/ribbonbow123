#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #352 (AM) and #353 (PM) — 2026-11-05 cron.

#352 AM: Private label / white-label ribbon programme setup — artwork ownership,
         decoration method, SKU planning, sample ladder, programme agreement.
#353 PM: Certification as a procurement decision — cost analysis, scope verification,
         weighting in a supplier scorecard.

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, KPI strip, CTA, footer. Matches house template from #330-#351.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-05"

ARTICLES = [
    {
        "no": 352,
        "slot": "am",
        "pubtime": "2026-11-05T08:00:00+08:00",
        "slug": ("blog-private-label-ribbon-programme-setup-oem-white-label-artwork-ownership-"
                 "decoration-method-sample-ladder-private-label-buyers-guide-2026-11-05-am"),
        "title": ("Private Label Ribbon Programme Setup &mdash; OEM, White Label and the Structure "
                  "Behind a Repeatable Brand Order (2026)"),
        "desc": ("How to set up a private label ribbon programme that can be reordered: artwork "
                 "ownership, decoration method, SKU planning, sample ladder and the agreement terms that matter."),
        "keywords": ("private label ribbon programme, OEM ribbon setup, white label ribbon, ribbon OEM "
                     "guide, ribbon artwork ownership, ribbon decoration method selection, ribbon screen "
                     "printing vs foil stamping, ribbon sample ladder, ribbon MOQ per SKU, ribbon reorder "
                     "consistency, ribbon packaging specification, private label ribbon agreement, B2B "
                     "ribbon brand programme, ribbon customisation for brands, ribbon private labelling "
                     "guide 2026"),
        "body": Path("/tmp/rb352_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb352_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "The Difference Between Buying Ribbon and Buying a Private Label Programme",
            "Six Decisions You Make Before the First Metre Is Woven",
            "Building the Specification So It Can Be Ordered Again",
            "Packaging and Presentation as a Programme Decision",
            "How the Sample Ladder Works",
            "What a Good Private Label Agreement Should Contain",
            "How Private Label Programmes Fail",
            "Building a Programme That Scales",
            "What Good Looks Like in Practice",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand managers, category buyers and procurement teams most "
                      "often ask us about setting up a private label ribbon programme, from artwork ownership "
                      "to sample approval and reorder consistency. If your question is not here, ask us directly."),
        "cat": "B2B OEM",
        "accent": "#6a1b9a",
        "accent2": "#9c27b0",
        "read": "18 min read",
        "kpi": [
            ("6", "decisions to settle before the first metre is woven"),
            ("4", "sample stages, each proving something different"),
            ("500m", "small-batch entry point for OEM customisation"),
        ],
    },
    {
        "no": 353,
        "slot": "pm",
        "pubtime": "2026-11-05T13:00:00+08:00",
        "slug": ("blog-ribbon-certification-procurement-cost-analysis-scope-verification-"
                 "supplier-scorecard-certification-roi-brand-procurement-guide-2026-11-05-pm"),
        "title": ("Ribbon Certification as a Procurement Decision &mdash; Cost Analysis, Scope "
                  "Verification and What It Is Worth to a Brand (2026)"),
        "desc": ("Which ribbon certifications actually move a purchasing decision, what they really cost, "
                 "how to verify the scope covers your product, and how to weight them in a supplier scorecard."),
        "keywords": ("ribbon certification cost analysis, ribbon certification scope verification, OEKO-TEX "
                     "ribbon certificate, FSC chain of custody ribbon, BSCI SMETA ribbon supplier, ISO 9001 "
                     "ribbon factory, GRS recycled content ribbon certificate, ribbon supplier scorecard "
                     "certification weighting, ribbon compliance ROI, private label ribbon certification, "
                     "certification expiry tracking, ribbon supplier due diligence, B2B ribbon procurement "
                     "certification guide, ribbon testing report requirement"),
        "body": Path("/tmp/rb353_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb353_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Certification Is a Cost, and It Is Also a Decision",
            "The Cost Side of Certification: What You Are Actually Buying",
            "Which Certifications Actually Move a Decision",
            "Reading a Certificate Properly: A Practical Procedure",
            "How Certification Enters a Supplier Selection Scorecard",
            "Cost Analysis: What Certification Adds to a Ribbon Programme",
            "Selecting a Supplier on Capability, Not on Paperwork",
            "Making Certification Practical Inside a Buying Organisation",
            "When Certification Is Not the Answer",
            "What Good Looks Like in Practice",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions procurement managers, category buyers and compliance leads most "
                      "often ask us about ribbon certification — scope, expiry, cost and how to weight it in "
                      "supplier evaluation. If your question is not here, ask us directly."),
        "cat": "B2B Compliance",
        "accent": "#0b6e4f",
        "accent2": "#159f7e",
        "read": "17 min read",
        "kpi": [
            ("5", "components of the real cost of certification"),
            ("10 min", "to verify holder, scope, site, expiry and number"),
            ("3", "tiers: mandatory, risk-reducing, and not worth weight"),
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
        "wordCount": 3200,
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

    if a["no"] == 352:
        cta_second = (
            'Whether you need a programme structure built from the specification up, an artwork ownership '
            'position agreed before sampling, a decoration method matched to your volume and target price, a '
            'sample ladder that prevents approving the wrong sample, or a written agreement that settles '
            'tooling and reorder terms, send us the details and we will tell you plainly what is required '
            'and what it costs.'
        )
    else:
        cta_second = (
            'Whether you need a certificate scope checked against your specific article and colour, a '
            'certification register set up with expiry tracking, a requirement list written for a supplier '
            'tender, or a decision on which certifications are worth the weight and which are not, send us '
            'the details and we will tell you plainly what is required and what it costs.'
        )

    cta_body = (
        'Smith Ribbon has been manufacturing ribbon, bows, tassels and decorative trim in Xiamen since 2004, '
        'with our own 15,000 m&sup2; factory, more than 200 employees, daily output of 100,000 metres, and '
        'certification including OEKO-TEX, FSC, BSCI, SEDEX/SMETA and ISO 9001. We ship to more than 50 countries '
        'and support OEM and ODM customisation from 1,000 metres, with small-batch runs from 500 metres.'
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
        <p class="meta">By Xiamen Smith Ribbon&amp;Bow Co., Ltd. | Published November 4, 2026 | Category: {a["cat"]} | Article #{a["no"]}</p>
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
