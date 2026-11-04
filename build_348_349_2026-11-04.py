#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #348 (AM) and #349 (PM) — 2026-11-04 cron.

#348 AM: OEM development brief -> production -> shipment (spec, BOM, artwork, compliance instruction)
#349 PM: Certification scope, expiry and evidence decoding for retail/brand procurement

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, KPI strip, CTA, footer. Matches house template from #330-#347.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-04"

ARTICLES = [
    {
        "no": 348,
        "slot": "am",
        "pubtime": "2026-11-04T08:00:00+08:00",
        "slug": ("blog-oem-custom-ribbon-development-brief-to-production-to-shipment-specification-"
                 "bill-of-materials-artwork-compliance-instruction-private-label-buyers-guide-2026-11-04-am"),
        "title": ("OEM Custom Ribbon Development Brief to Production to Shipment &mdash; Specification, Bill of "
                  "Materials, Artwork and Compliance Instruction for Private Label Buyers (2026)"),
        "desc": ("How to run an OEM custom ribbon programme from development brief to shipment: the four documents "
                 "that remove ambiguity, the eight-stage production sequence, and the packaging details buyers "
                 "usually leave to the mill."),
        "keywords": ("OEM custom ribbon development brief, ribbon production process, ribbon bill of materials, "
                     "ribbon artwork instruction, ribbon specification tolerance, pre-production sample approval, "
                     "ribbon MOQ first production run, ribbon winding format specification, ribbon compliance "
                     "instruction, ribbon OEM production sequence, private label ribbon launch timeline, "
                     "ribbon sample approval types, B2B ribbon OEM buyer guide, ribbon packaging specification, "
                     "custom ribbon order process brand owner"),
        "body": Path("/tmp/rb348_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb348_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Why the Brief Is the Programme",
            "The Four Documents That Make Up a Complete Brief",
            "From Brief to Production: The Sequence That Prevents the Expensive Errors",
            "Four Places Programmes Usually Go Wrong",
            "Planning the Launch: A Sequence That Works",
            "What Makes the Difference in Practice",
            "What a Useful Shipping Document Set Contains",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, category buyers and procurement managers most often ask "
                      "us about OEM ribbon development briefs, production sequences and shipping documentation. "
                      "If your question is not here, ask us directly."),
        "cat": "B2B Sourcing",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
        "read": "19 min read",
        "kpi": [
            ("4", "documents that make up a complete OEM ribbon brief"),
            ("8", "stages from specification review to dispatch"),
            ("~12", "weeks to plan for a first custom production cycle"),
        ],
    },
    {
        "no": 349,
        "slot": "pm",
        "pubtime": "2026-11-04T13:00:00+08:00",
        "slug": ("blog-ribbon-certification-scope-expiry-evidence-file-renewal-calendar-retailer-brand-"
                 "procurement-verification-guide-2026-11-04-pm"),
        "title": ("Ribbon Certification Scope, Expiry and Evidence &mdash; A Verification Method for Retailer and "
                  "Brand Procurement Teams (2026)"),
        "desc": ("A practical method for verifying ribbon supplier certifications: how to read certificate scope, "
                 "licence holder and expiry, how to keep a file that survives an audit, and how to stop packaging "
                 "outliving its own evidence."),
        "keywords": ("ribbon certification verification, OEKO-TEX STANDARD 100 scope, FSC chain of custody ribbon, "
                     "BSCI social compliance audit, SMETA four-pillar audit, ISO 9001 ribbon factory, GRS recycled "
                     "ribbon transaction certificate, certificate expiry renewal calendar, supplier compliance "
                     "evidence file, private label packaging compliance audit, recycled content claim substantiation, "
                     "certificate scope check product class, B2B ribbon supplier compliance verification, "
                     "retailer supplier compliance documentation"),
        "body": Path("/tmp/rb349_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb349_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "The First Question Is Not \u201cDo You Have It\u201d but \u201cWhat Does It Cover\u201d",
            "Reading a Certificate Properly: Nine Fields",
            "Why Expiry Matters More Than Buyers Expect",
            "Building a Verification File That Survives an Audit",
            "What to Ask a Supplier \u2014 and What Their Answer Tells You",
            "Cost, Timing and Where Certification Actually Delays a Programme",
            "Building a Verification Routine",
            "How We Handle Certification at the Mill",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, category buyers, quality managers and procurement "
                      "specialists most often ask us about ribbon supplier certification, scope, expiry and "
                      "evidence. If your question is not here, ask us directly."),
        "cat": "B2B Compliance",
        "accent": "#7d3c98",
        "accent2": "#a569bd",
        "read": "18 min read",
        "kpi": [
            ("9", "fields to check on any ribbon supplier certificate"),
            ("5", "certification families and what each one actually covers"),
            ("60", "days, minimum supplier notice before a certificate expires"),
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

    if a["no"] == 348:
        cta_second = (
            'Whether you need a development brief written so that both sides measure the same thing, a bill of '
            'materials that includes the packaging and winding format, an artwork and compliance instruction set '
            'with a named owner, a pre-production sample plan built around your approval process, or a shipping '
            'document set assembled to survive a customs hold, send us the details and we will tell you plainly '
            'what is required and what it costs.'
        )
    else:
        cta_second = (
            'Whether you need the certificate numbers and scope lines for your product mapped in writing, a '
            'verification file assembled for your own compliance team, a renewal calendar set up across your '
            'supplier base, a recycled-content chain-of-custody arrangement with transaction certificates, or a '
            'scope extension timeline for a new construction, send us the details and we will tell you plainly '
            'what is required and what it costs.'
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
