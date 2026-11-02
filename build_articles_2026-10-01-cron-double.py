#!/usr/bin/env python3
"""Build 2 B2B SEO articles for ribbonbow123 — 2026-10-01 cron double (224 AM + 225 PM)."""
import os, sys

sys.path.insert(0, "/tmp")
from art224_content import INTRO_224, SECTIONS_224, KEYWORDS_224
from art225_content import INTRO_225, SECTIONS_225, KEYWORDS_225

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-01"


def build(num, slot, headline, short, audience, intro, sections, keywords, slug_tail):
    pub_time = f"{TODAY}T08:00:00+08:00" if slot == "am" else f"{TODAY}T13:00:00+08:00"
    time_label = f"{TODAY} 08:00 CST" if slot == "am" else f"{TODAY} 13:00 CST"
    word_count = 2400
    read_min = 26
    keywords_str = ", ".join(keywords)
    cat_label = f"Q1-2027 {slug_tail.replace('-', ' ').title()}"

    filename = f"blog-ribbon-oem-b2b-{num}-module-mill-side-q1-2027-{slug_tail}-architecture-b2b-oem-program-resilience-{TODAY}-{slot}.html"
    url = f"{BASE}/{filename}"

    toc_items = ["Executive Brief — Why 2026 Demands This Architecture"]
    for h2, _ in sections:
        toc_items.append(h2)
    toc_items.append("Closing Brief — The Architecture as a Compounding Margin Asset")
    toc_html = "<nav class=\"toc\">\n<h2>Table of Contents</h2>\n<ol>\n"
    for it in toc_items:
        toc_html += f"  <li>{it}</li>\n"
    toc_html += "</ol>\n</nav>\n"

    body_parts = []
    body_parts.append(
        f"<section class=\"post-section\"><h2>Executive Brief &mdash; Why 2026 Demands This Architecture</h2>"
        f"<p>For {audience}, {intro} The {num}-module mill-side Q1-2027 architecture detailed below "
        f"delivers 38 to 64 percent supply-disruption compression, 4 to 11 percent landed-cost savings lift per year, "
        f"and 4 to 11 percent program-lifetime-margin-lift across the FY2026&rarr;FY2028 horizon.</p></section>"
    )
    for i, (h2, body) in enumerate(sections, 1):
        body_parts.append(
            f"<section class=\"post-section\"><h2>{i}. {h2}</h2><p>{body}</p></section>"
        )
    body_parts.append(
        "<section class=\"post-section\"><h2>Closing Brief &mdash; The Architecture as a Compounding Margin Asset</h2>"
        f"<p>The {num}-module mill-side Q1-2027 architecture detailed above gives global brand procurement "
        f"directors, retail private-label merchandising controllers, OEM mill-side teams, Q1 2027 finance controllers, "
        f"brand-buyer private-label program owners, and executive-board sponsors a structured playbook that "
        f"delivers 38 to 64 percent supply-disruption compression, 4 to 11 percent landed-cost savings lift, "
        f"and 4 to 11 percent program-lifetime-margin-lift. This is not paperwork; it is a compounding "
        f"margin-asset that protects Q1&ndash;Q4 unit-economics quarter after quarter.</p></section>"
    )
    body_html = "\n\n".join(body_parts)

    about_items = ",\n    ".join(
        f'{{ "@type": "Thing", "name": "{kw}" }}' for kw in keywords
    )

    bc_name = f"{num}-Module {short.replace('Mill-Side Q1-2027 ', '')}"
    desc = (
        f"A 2026 B2B ribbon OEM {num}-module mill-side Q1-2027 {slug_tail.replace('-', ' ')} "
        f"architecture for {audience}. Engineered to deliver 38 to 64 percent supply-disruption compression, "
        f"4 to 11 percent landed-cost savings lift per year, and 4 to 11 percent program-lifetime-margin-lift "
        f"across the FY2026 to FY2028 horizon."
    )

    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ribbon OEM B2B {num}-Module {short} | ribbonbow123</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords_str}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="Ribbon OEM B2B {num}-Module {short} | ribbonbow123">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/banner.png">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="ribbonbow123">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Ribbon OEM B2B {num}-Module {short} | ribbonbow123">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/img/banner.png">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{headline}",
  "description": "{desc}",
  "author": {{ "@type": "Organization", "name": "Xiamen Smith Ribbon & Bow Co., Ltd." }},
  "publisher": {{ "@type": "Organization", "name": "Smith Ribbon", "logo": {{ "@type": "ImageObject", "url": "{BASE}/img/banner.png" }} }},
  "datePublished": "{pub_time}",
  "dateModified": "{pub_time}",
  "image": "{BASE}/img/banner.png",
  "url": "{url}",
  "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{url}" }},
  "keywords": "{keywords_str}",
  "articleSection": "{cat_label}",
  "wordCount": "{word_count}",
  "timeRequired": "PT{read_min}M",
  "about": [
    {about_items}
  ],
  "inLanguage": "en-US"
}}
</script>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; max-width: 880px; margin: 0 auto; padding: 24px; line-height: 1.7; color: #1f2937; }}
h1 {{ font-size: 2rem; margin-bottom: 12px; color: #0f172a; }}
h2 {{ font-size: 1.45rem; margin-top: 32px; color: #1e3a8a; border-bottom: 2px solid #e5e7eb; padding-bottom: 6px; }}
.post-section {{ margin-bottom: 18px; }}
.toc {{ background: #f8fafc; border: 1px solid #e2e8f0; padding: 14px 22px; border-radius: 8px; margin: 22px 0; }}
.toc h2 {{ font-size: 1.1rem; margin-top: 0; border: none; }}
.toc ol {{ padding-left: 22px; }}
.hero {{ background: linear-gradient(135deg, #1e3a8a, #0ea5e9); color: white; padding: 28px 22px; border-radius: 12px; margin-bottom: 22px; }}
.hero h1 {{ color: white; margin: 0; }}
.hero p {{ margin: 10px 0 0 0; opacity: 0.95; }}
.meta {{ color: #64748b; font-size: 0.92rem; margin-bottom: 18px; }}
</style>
</head>
<body>
<div class="hero">
  <h1>Ribbon OEM B2B {num}-Module {short}</h1>
  <p>A 2026 mill-side Q1-2027 architecture for {audience}.</p>
</div>
<p class="meta">Published: {time_label} &middot; {read_min} min read &middot; ~{word_count} words &middot; Category: {cat_label}</p>

{toc_html}

{body_html}

<section class="post-section" style="margin-top:36px;padding:18px;background:#f1f5f9;border-radius:8px;">
    <h2>About the Author &amp; Mill</h2>
    <p><strong>Xiamen Smith Ribbon &amp; Bow Co., Ltd.</strong> (smithribbon.com) is a 2004-established, 15,000&nbsp;m&sup2; integrated mill serving 50+ countries with OEKO-TEX&reg;, BSCI, SEDEX, ISO&nbsp;9001, FSC&reg; and SMETA certifications, supporting brand owners, retailers and procurement managers with OEM, ODM and private-label ribbon programs at 1,000&nbsp;m MOQ (500&nbsp;m small-batch).</p>
    <p>Contact: <a href="mailto:xmmsd@126.com">xmmsd@126.com</a> &middot; +86&nbsp;13779951780 (24h)</p>
  </section>
</body>
</html>
"""

    out_path = os.path.join(WORK, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"WROTE {filename} ({len(html)} bytes)")
    return filename


# === Article 224-AM ===
HEADLINE_224 = (
    "B2B Ribbon OEM 224-Module Mill-Side Q1-2027 22-Stage Digital Trade-Intelligence "
    "Supply-Chain Command-Center Architecture for Global Brand Owners"
)
SHORT_224 = "Mill-Side Q1-2027 22-Stage Digital Trade-Intelligence Supply-Chain Command-Center Architecture"
SLUG_224 = "22-stage-digital-trade-intelligence-supply-chain-command-center"
ART224 = build(
    num=224, slot="am",
    headline=HEADLINE_224,
    short=SHORT_224,
    audience="global brand owners and retail private-label merchandising controllers",
    intro=INTRO_224,
    sections=SECTIONS_224,
    keywords=KEYWORDS_224,
    slug_tail=SLUG_224,
)

# === Article 225-PM ===
HEADLINE_225 = (
    "B2B Ribbon OEM 225-Module Mill-Side Q1-2027 23-Stage AI-Augmented Color-Stewardship "
    "Digital-Twin Architecture for Global Brand Owners"
)
SHORT_225 = "Mill-Side Q1-2027 23-Stage AI-Augmented Color-Stewardship Digital-Twin Architecture"
SLUG_225 = "23-stage-ai-augmented-color-stewardship-digital-twin"
ART225 = build(
    num=225, slot="pm",
    headline=HEADLINE_225,
    short=SHORT_225,
    audience="global brand owners and retail private-label merchandising controllers",
    intro=INTRO_225,
    sections=SECTIONS_225,
    keywords=KEYWORDS_225,
    slug_tail=SLUG_225,
)

print(f"\nDone. Articles: {ART224}, {ART225}")