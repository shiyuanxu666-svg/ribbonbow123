#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #341 (AM) and #342 (PM) — 2026-11-03 cron.

#341 AM: Private label ribbon programme — spec, colour, sample ladder, supplier evidence, reorder
#342 PM: Certification verification — reading scopes, evidence beyond certificate, claims substantiation

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, KPI strip, CTA, footer. Matches house template from #330-#340.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-03"

ARTICLES = [
    {
        "no": 341,
        "slot": "am",
        "pubtime": "2026-11-03T08:00:00+08:00",
        "slug": ("blog-private-label-ribbon-programme-guide-specification-colour-standard-sample-ladder-"
                 "supplier-evidence-reorder-protection-brand-buyers-guide-2026-11-03-am"),
        "title": ("Private Label Ribbon Programme Guide &mdash; Specification, Colour Standards, Sample Ladder, "
                  "Supplier Evidence and Reorder Protection for Brand Buyers (2026)"),
        "desc": ("A practical guide to running a private label ribbon programme: writing a buildable specification, "
                 "capturing colour as a number, designing the sample ladder and securing the reorder."),
        "keywords": ("private label ribbon programme, ribbon specification guide, custom ribbon specification, "
                     "ribbon colour standard, delta E ribbon tolerance, ribbon sample ladder, "
                     "ribbon supplier evaluation, OEM ribbon procurement, ribbon reorder protection, "
                     "private label ribbon guide, B2B ribbon buying guide, ribbon lab dip approval, "
                     "ribbon strike off, custom ribbon MOQ, ribbon packaging trim programme, "
                     "brand owner ribbon sourcing, ribbon quote terms, ribbon quality specification"),
        "body": Path("/tmp/rb341_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb341_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Private Label Ribbon Is a Programme, Not a Purchase Order",
            "Step One: Define What the Ribbon Has to Do",
            "Step Two: Write a Specification a Factory Cannot Misread",
            "Step Three: Capture Colour as a Number, Not a Sample",
            "Step Four: Design the Sample Ladder Around Decisions",
            "Step Five: Judge the Supplier on Evidence, Not on Presentation",
            "Step Six: Agree the Commercial Terms Before the First Order",
            "Step Seven: Make the Reorder Predictable",
            "The Mistakes That Cost the Most",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, packaging designers and procurement managers most often "
                      "ask us about private label ribbon programmes. If your question is not here, ask us directly."),
        "cat": "B2B Branding",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
        "read": "21 min read",
        "kpi": [
            ("7", "steps from brief to a reorderable programme"),
            ("4", "samples, each proving a specific decision"),
            ("12", "months, typical reorder price protection window"),
        ],
    },
    {
        "no": 342,
        "slot": "pm",
        "pubtime": "2026-11-03T13:00:00+08:00",
        "slug": ("blog-ribbon-certification-verification-scope-expiry-evidence-claims-substantiation-"
                 "supplier-compliance-audit-b2b-brand-procurement-2026-11-03-pm"),
        "title": ("Ribbon Certification Verification Guide &mdash; Scope, Expiry, Evidence and Claim "
                  "Substantiation for Brand Procurement Teams (2026)"),
        "desc": ("How to verify ribbon supplier certifications: reading scopes, tracking expiry, requesting evidence "
                 "beyond the certificate, and substantiating your own on-pack compliance claims."),
        "keywords": ("ribbon certification verification, OEKO-TEX ribbon certificate, FSC chain of custody ribbon, "
                     "BSCI audit verification, SMETA SEDEX audit, ISO 9001 ribbon supplier, "
                     "certificate scope checking, supplier compliance audit, recycled content claim substantiation, "
                     "RPET claim substantiation, ribbon supplier compliance, B2B ribbon procurement compliance, "
                     "certificate expiry tracking, compliance claims register, ribbon factory compliance, "
                     "private label compliance evidence, brand procurement audit"),
        "body": Path("/tmp/rb342_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb342_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "A Certificate Is a Document, Not an Outcome",
            "Why Verification Fails in the Easy Cases",
            "Reading a Certificate: The Fields That Matter",
            "What to Ask For Beyond the Certificate",
            "A Verification Routine That Scales",
            "Handling the Awkward Cases",
            "Making Your Own Compliance Defensible",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, category buyers and compliance managers most often ask "
                      "us about ribbon certification and supplier compliance evidence. If your question is not here, "
                      "ask us directly."),
        "cat": "B2B Compliance",
        "accent": "#7d3c98",
        "accent2": "#a569bd",
        "read": "19 min read",
        "kpi": [
            ("4", "qualifiers that make a certificate meaningful"),
            ("90", "days, when renewal alerts should fire"),
            ("1", "step that tests the goods rather than the file"),
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
        "wordCount": 3900,
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

    cta_block = (
        '\n<hr>\n'
        '<h2>Talk to Us About Your Programme</h2>\n'
        '<p>Smith Ribbon has been manufacturing ribbon, bows, tassels and decorative trim in Xiamen since 2004, '
        'with our own 15,000 m&sup2; factory, more than 200 employees, daily output of 100,000 metres, and '
        'certification including OEKO-TEX, FSC, BSCI, SEDEX/SMETA and ISO 9001. We ship to more than 50 countries '
        'and support OEM and ODM customisation from 1,000 metres, with small-batch runs from 500 metres.</p>\n'
        '<p>Whether you need a feasibility check on your specification before you commit, a landed cost model at three '
        'quantities, a sample ladder designed around your approval process, or current in-scope certificates for your '
        'compliance file, send us the details and we will tell you plainly what is required and what it costs.</p>\n'
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
