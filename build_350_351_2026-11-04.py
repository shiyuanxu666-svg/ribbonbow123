#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #350 (AM) and #351 (PM) — 2026-11-04 cron.

#350 AM: Ribbon factory assessment / due diligence — capability, evidence, behaviour
#351 PM: Landed cost & total cost of ownership for private label ribbon programmes

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, KPI strip, CTA, footer. Matches house template from #330-#349.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-04"

ARTICLES = [
    {
        "no": 350,
        "slot": "am",
        "pubtime": "2026-11-04T08:00:00+08:00",
        "slug": ("blog-ribbon-factory-assessment-due-diligence-capability-evidence-behaviour-"
                 "supplier-evaluation-verification-brand-procurement-guide-2026-11-04-am"),
        "title": ("Ribbon Factory Assessment and Due Diligence &mdash; Capability, Evidence and Behaviour "
                  "for Brand Procurement Teams (2026)"),
        "desc": ("How to assess a ribbon factory before you commit: questions that reveal capability, "
                 "how to verify certificates, and what a factory visit should look at."),
        "keywords": ("ribbon factory assessment, ribbon supplier due diligence, ribbon factory audit, ribbon "
                     "manufacturer verification, ribbon OEM supplier evaluation, ribbon factory capacity check, "
                     "ribbon supplier certification verification, ribbon factory visit checklist, private label "
                     "ribbon supplier selection, ribbon quality claim handling, ribbon supply agreement tooling "
                     "ownership, B2B ribbon sourcing guide, ribbon supplier risk assessment, ribbon mill "
                     "qualification"),
        "body": Path("/tmp/rb350_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb350_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "The Assessment Is Not an Audit",
            "Twelve Things to Establish Before You Commit",
            "Turning the Answers Into a Decision",
            "The Questions to Ask on a Factory Visit",
            "What to Do When the First Order Goes Wrong",
            "Building an Ongoing Relationship",
            "What Good Looks Like in Practice",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, category buyers and procurement managers most often ask "
                      "us about assessing a ribbon factory, verifying supplier certificates and handling quality "
                      "claims. If your question is not here, ask us directly."),
        "cat": "B2B Sourcing",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
        "read": "18 min read",
        "kpi": [
            ("12", "questions to establish before committing to a factory"),
            ("3", "layers to assess: capability, evidence and behaviour"),
            ("8", "things to check on a factory visit, in the right order"),
        ],
    },
    {
        "no": 351,
        "slot": "pm",
        "pubtime": "2026-11-04T13:00:00+08:00",
        "slug": ("blog-ribbon-landed-cost-total-cost-of-ownership-economics-quote-comparison-model-"
                 "private-label-buyers-guide-2026-11-04-pm"),
        "title": ("Ribbon Landed Cost and Total Cost of Ownership &mdash; A Working Model for Comparing "
                  "Private Label Quotes (2026)"),
        "desc": ("How to build a landed cost model that makes two ribbon quotes comparable: the costs outside "
                 "the unit price, and how to normalise quotes before comparing them."),
        "keywords": ("ribbon landed cost, ribbon total cost of ownership, ribbon quote comparison, ribbon cost "
                     "model, custom ribbon pricing breakdown, ribbon development cost amortisation, ribbon "
                     "freight cost per metre, ribbon payment terms cost, ribbon defect cost, private label ribbon "
                     "cost analysis, ribbon supplier negotiation landed cost, ribbon carton packaging optimisation, "
                     "B2B ribbon procurement economics, ribbon should cost model, ribbon cost per order analysis"),
        "body": Path("/tmp/rb351_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb351_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Why the Quoted Price Is the Least Interesting Number",
            "The Cost Components That Sit Outside the Quote",
            "Building the Model",
            "Reading a Quote Properly",
            "What the Model Changes About the Decision",
            "Where Buyers Get It Wrong",
            "Making It Routine",
            "The Number Worth Trusting",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions procurement managers, finance reviewers and brand owners most often "
                      "ask us about ribbon landed cost, quote comparison and total cost of ownership. If your "
                      "question is not here, ask us directly."),
        "cat": "B2B Cost",
        "accent": "#117a65",
        "accent2": "#16a085",
        "read": "17 min read",
        "kpi": [
            ("6", "cost blocks in a working landed cost model"),
            ("55-75%", "share of programme cost typically set by unit price alone"),
            ("3", "quotes to normalise before any comparison is meaningful"),
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

    if a["no"] == 350:
        cta_second = (
            'Whether you need an assessment framework for a factory you have not yet visited, a checklist for '
            'verifying certificate scope and expiry, a factory visit plan that shows you the production floor '
            'rather than the showroom, a written remedy ladder for quality claims, or a supply agreement that '
            'settles tooling ownership, send us the details and we will tell you plainly what is required and '
            'what it costs.'
        )
    else:
        cta_second = (
            'Whether you need a quote normalised to landed cost, a carton and packaging configuration that reduces '
            'freight per metre, development cost separated from unit price, a defect allowance written into the '
            'commercial terms, or a cost model your finance team can sign off on, send us the details and we will '
            'tell you plainly what is required and what it costs.'
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
