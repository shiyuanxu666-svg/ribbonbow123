#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ribbonbow123 B2B articles #339 (AM) and #340 (PM) — 2026-11-02 cron.

#339 AM: Branded ribbon design — decoration methods, artwork prep, colour, sample ladder, spec
#340 PM: Ribbon MOQ & small-batch order economics

Full meta + OG + Twitter, Article + BlogPosting + FAQPage + BreadcrumbList JSON-LD,
visible FAQ block, TOC, KPI strip, CTA, footer. Matches house template from #330-#338.
"""
from pathlib import Path
import json
import re

ROOT = Path("/workspace/ribbonbow123")
BASE = "https://ribbonbow123.com"
DATE = "2026-11-02"

ARTICLES = [
    {
        "no": 339,
        "slot": "am",
        "pubtime": "2026-11-02T08:00:00+08:00",
        "slug": ("blog-branded-ribbon-design-guide-decoration-methods-screen-print-foil-heat-transfer-jacquard-"
                 "artwork-colour-approval-sample-ladder-private-label-buyers-guide-2026-11-02-am"),
        "title": ("Branded Ribbon Design Guide &mdash; Screen Print, Foil, Heat Transfer or Jacquard: "
                  "Choosing a Decoration Method, Preparing Artwork and Approving Colour for Private Label "
                  "Ribbon (2026)"),
        "desc": ("A guide to branding ribbon: comparing screen print, foil, heat transfer and jacquard, "
                 "preparing artwork, matching Pantone colour and running the sample ladder."),
        "keywords": ("branded ribbon design, custom printed ribbon, screen printed ribbon, hot foil ribbon, "
                     "heat transfer ribbon, jacquard ribbon branding, ribbon artwork preparation, "
                     "ribbon Pantone colour matching, ribbon sample approval, ribbon branding guide, "
                     "custom ribbon logo printing, ribbon decoration method, private label ribbon design, "
                     "B2B ribbon procurement guide, ribbon print registration, ribbon brand identity, "
                     "grosgrain satin velvet ribbon printing"),
        "body": Path("/tmp/rb339_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb339_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Branding on Ribbon Is a Different Design Problem",
            "The Four Decoration Methods, and When Each One Wins",
            "Choosing the Right Method: A Practical Decision Sequence",
            "Preparing Artwork That a Factory Can Actually Produce",
            "Colour: How the Same Pantone Behaves Across Methods",
            "The Sample Ladder: Approving the Right Thing at the Right Moment",
            "Specification: The Document That Prevents the Next Dispute",
            "Common Mistakes, and What They Cost",
            "A Branded Ribbon Programme That Works",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, packaging designers and procurement managers most "
                      "often ask us about branding custom ribbon. If your question is not here, ask us directly."),
        "cat": "B2B Branding",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
        "read": "22 min read",
        "kpi": [
            ("4", "decoration methods, and where each one works"),
            ("4", "sample stages, and what each one proves"),
            ("0.3", "mm, the practical minimum feature size"),
        ],
    },
    {
        "no": 340,
        "slot": "pm",
        "pubtime": "2026-11-02T13:00:00+08:00",
        "slug": ("blog-ribbon-moq-small-batch-order-economics-guide-landed-cost-reorder-terms-private-label-"
                 "buyers-guide-2026-11-02-pm"),
        "title": ("Ribbon MOQ &amp; Small-Batch Order Economics Guide &mdash; Why Minimums Exist, How to "
                  "Get Below Them, and How to Read a Quotation Without Losing Money (2026)"),
        "desc": ("A buyer's guide to ribbon minimum order quantities: what drives a minimum, how to get "
                 "below it, reading quotations, and why landed cost really matters."),
        "keywords": ("ribbon MOQ guide, minimum order quantity ribbon, small batch ribbon order, "
                     "ribbon order economics, how to read a ribbon quotation, ribbon landed cost, "
                     "ribbon cost breakdown, custom ribbon pricing, private label ribbon buying guide, "
                     "B2B ribbon procurement guide, ribbon reorder terms, ribbon wholesale minimum, "
                     "ribbon inventory risk, OEM ribbon purchasing, ribbon factory price negotiation"),
        "body": Path("/tmp/rb340_body.html").read_text(encoding="utf-8"),
        "faq": json.loads(Path("/tmp/rb340_faq.json").read_text(encoding="utf-8")),
        "toc": [
            "Why the Minimum Order Quantity Feels Arbitrary",
            "What Actually Sets the Minimum",
            "The Order Quantity Decision: A Working Method",
            "Strategies for Getting Below the Minimum",
            "What the Per-Metre Price Is Actually Made Of",
            "Total Landed Cost: The Number That Actually Matters",
            "Small-Batch Strategy: Building Volume Without Building Inventory",
            "Reading a Quotation So You Can Negotiate It",
            "A Working Approach to Minimum Order Quantities",
        ],
        "faq_heading": "Frequently Asked Questions",
        "faq_intro": ("These are the questions brand owners, category buyers and procurement managers most often "
                      "ask us about ribbon minimums, quotations and order economics. If your question is not here, "
                      "ask us directly."),
        "cat": "B2B Procurement",
        "accent": "#7d3c98",
        "accent2": "#a569bd",
        "read": "21 min read",
        "kpi": [
            ("6", "ways to legitimately get below a minimum"),
            ("9", "components inside a real ribbon quotation"),
            ("15-30", "% typical unit price fall between minimum and 5x volume"),
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
        "wordCount": 4100,
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
        '<p>Whether you need a feasibility check on your artwork before you commit, a landed cost model at three '
        'quantities, or a sample ladder designed around your approval process, send us the details and we will '
        'tell you plainly what is required and what it costs.</p>\n'
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
        <p class="meta">By Xiamen Smith Ribbon&amp;Bow Co., Ltd. | Published November 2, 2026 | Category: {a["cat"]} | Article #{a["no"]}</p>
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
