#!/usr/bin/env python3
"""Build 2 B2B SEO articles for ribbonbow123 — 2026-09-25 15:00 cron slot (203 AM + 204 PM)."""
import os, sys

sys.path.insert(0, "/tmp")
from art203_content import INTRO_203, SECTIONS_203, KEYWORDS_203
from art204_content import INTRO_204, SECTIONS_204, KEYWORDS_204

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-25"


def build(num, slot, headline, short, audience, intro, sections, keywords, slug_tail):
    pub_time = f"{TODAY}T08:00:00+08:00" if slot == "am" else f"{TODAY}T15:00:00+08:00"
    time_label = f"{TODAY} 08:00 CST" if slot == "am" else f"{TODAY} 15:00 CST"
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
        f"and 4 to 11 percent program-lifetime-margin-lift across the FY2026&rsaquo;FY2028 horizon.</p></section>"
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
  "publisher": {{
    "@type": "Organization",
    "name": "ribbonbow123",
    "logo": {{ "@type": "ImageObject", "url": "{BASE}/img/banner.png" }}
  }},
  "datePublished": "{pub_time}",
  "dateModified": "{pub_time}",
  "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{url}" }},
  "image": "{BASE}/img/banner.png",
  "articleSection": "{cat_label}",
  "wordCount": {word_count},
  "about": [
    {about_items}
  ],
  "mentions": [
    {{ "@type": "Thing", "name": "Global Brand Procurement" }},
    {{ "@type": "Thing", "name": "Private Label Program" }},
    {{ "@type": "Thing", "name": "Ribbon OEM B2B" }},
    {{ "@type": "Thing", "name": "Mill-Side Q1-2027" }}
  ],
  "isPartOf": {{
    "@type": "Blog",
    "name": "Ribbonbow123 B2B OEM Insights",
    "url": "{BASE}/blog.html"
  }}
}}
</script>
<meta name="publish-date" content="{time_label}">
<meta name="content-language" content="en-US">
<meta name="audience" content="{audience}">
<meta name="category" content="{cat_label}">
<meta name="word-count" content="{word_count}">
<meta name="read-time" content="{read_min} min">
</head>
<body>
<main>
<article>
<header>
<h1>{headline}</h1>
<p class="post-meta">Published {time_label} &middot; {read_min} min read &middot; {word_count} words &middot; {cat_label}</p>
</header>

{toc_html}

{body_html}

<aside class="internal-links">
<h2>Continue Reading &mdash; Related ribbon OEM Architecture Modules</h2>
<ul>
<li><a href="{BASE}/blog.html">Browse all ribbon OEM B2B architecture modules</a></li>
<li><a href="{BASE}/oem-services.html">Explore ribbonbow123 OEM services</a></li>
<li><a href="{BASE}/factory-tour.html">See our 15,000 m&sup2; Xiamen production facility</a></li>
<li><a href="{BASE}/contact.html">Contact a ribbon OEM program architect</a></li>
</ul>
</aside>
</article>
</main>
</body>
</html>
"""
    path = os.path.join(WORK, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return filename


# Article 203 (AM) — Yield-Improvement Pareto-Engine Defect-Stream Architecture
headline_203 = "Ribbon OEM B2B 203-Module Mill-Side Q1-2027 Yield-Improvement Pareto-Engine Defect-Stream Architecture"
short_203 = "Mill-Side Q1-2027 Yield-Improvement Pareto-Engine Defect-Stream"
audience_203 = "mill-side production directors, plant-operation controllers, OEM program owners, and brand-buyer private-label sourcing leads"
slug_203 = "yield-improvement-pareto-engine-defect-stream-oee-energy-water-carbon-productivity"

# Article 204 (PM) — Sustainable-Material Sourcing Architecture
headline_204 = "Ribbon OEM B2B 204-Module Mill-Side Q1-2027 Sustainable-Material Sourcing Architecture"
short_204 = "Mill-Side Q1-2027 Sustainable-Material Sourcing"
audience_204 = "mill-side sustainability directors, GRS-RPET sourcing controllers, B2B brand-buyer ESG procurement leads, and brand-owner circular-economy program owners"
slug_204 = "sustainable-material-sourcing-grs-rpet-fsc-paper-bio-yarn-closed-loop-material-recovery-esg-lca-disclosure"

f1 = build(203, "am", headline_203, short_203, audience_203, INTRO_203, SECTIONS_203, KEYWORDS_203, slug_203)
print(f"wrote {WORK}/{f1}")
f2 = build(204, "pm", headline_204, short_204, audience_204, INTRO_204, SECTIONS_204, KEYWORDS_204, slug_204)
print(f"wrote {WORK}/{f2}")
