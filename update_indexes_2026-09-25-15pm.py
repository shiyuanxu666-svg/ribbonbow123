#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 203-AM + 204-PM — 2026-09-25 15pm."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-25"

ART203 = {
    "file": "blog-ribbon-oem-b2b-203-module-mill-side-q1-2027-yield-improvement-pareto-engine-defect-stream-oee-energy-water-carbon-productivity-architecture-b2b-oem-program-resilience-2026-09-25-am.html",
    "title": "Ribbon OEM B2B 203-Module Mill-Side Q1-2027 Yield-Improvement Pareto-Engine Defect-Stream OEE-Energy-Water-Carbon-Productivity Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Yield-Improvement Pareto-Engine Defect-Stream OEE-Energy-Water-Carbon-Productivity Architecture",
    "date": TODAY,
    "desc": "203-module mill-side Q1-2027 yield-improvement pareto-engine defect-stream OEE-energy-water-carbon-productivity architecture (Stages 1-4 pareto-engine defect-stream ingest defect-code library FPY baselining substrate-drift mapping, Stages 5-9 OEE-dashboard energy-water-carbon metering pareto-chart auto-generation countermeasure-loop confirmation, Stages 10-14 inline-AOI vision defect library substrate-shift tuning color-drift auto-compensation edge-defect cascade print-register drift loop, Stages 15-19 energy-recovery heat-exchanger water-reclaim ZLD membrane-reclaim carbon-LCA boundary carbon-adjusted yield-productivity Scope-3 brand-buyer disclosure package, Stages 20-23 QBR-cadence kaizen-stand-up countermeasure-archive architecture refresh; 220-380 defect-codes, 24-cell OEE-matrix 30-minute refresh, Ecoinvent IPCC emission-factor library, ZLD 86-94 percent water-reclaim, kaizen daily-shift countermeasure loop) for global brand procurement and Q1-2027 plant-operation controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART204 = {
    "file": "blog-ribbon-oem-b2b-204-module-mill-side-q1-2027-sustainable-material-sourcing-grs-rpet-fsc-paper-bio-yarn-closed-loop-material-recovery-esg-lca-disclosure-architecture-b2b-oem-program-resilience-2026-09-25-pm.html",
    "title": "Ribbon OEM B2B 204-Module Mill-Side Q1-2027 Sustainable-Material Sourcing GRS-RPET FSC-Paper Bio-Yarn Closed-Loop Material-Recovery ESG-LCA Disclosure Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Sustainable-Material Sourcing GRS-RPET FSC-Paper Bio-Yarn Closed-Loop Material-Recovery ESG-LCA Disclosure Architecture",
    "date": TODAY,
    "desc": "204-module mill-side Q1-2027 sustainable-material sourcing GRS-RPET FSC-paper bio-yarn closed-loop material-recovery ESG-LCA disclosure architecture (Stages 1-4 GRS-RPET yarn provenance FSC-paper traceability bio-yarn substitution recycled-content substantiation, Stages 5-9 closed-loop take-back recommerce-channel mill-side material-reclamation re-use re-spun yarn customer-disclosure, Stages 10-14 ESG-LCA boundary Scope-3 brand-buyer disclosure EU-CBAM carbon-adjusted cost CSRD-ESRS reporting DPP-digital-product-passport, Stages 15-18 recycled-claim-substantiation anti-greenwashing retailer-tender verification third-party coordination, Stages 19-21 brand-buyer circular-economy co-design Q1-2027 ESG-roadmap refresh architecture outcome; 6-tier mass-balance chain-of-custody, FSC-C FSC-CW certificate, 4-8 bio-yarn substrate-trial matrix, Ecoinvent IPCC cradle-to-gate boundary, CSRD ESRS-E1 ESRS-E5 ESRS-S1 templates, EU-anti-greenwashing directive) for global brand procurement and Q1-2027 circular-economy program owners. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}


def card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 26 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def card_blog(art, emoji):
    return (
        f'<article class="blog-card">\n'
        f'  <span class="blog-tag">{art["cat"]}</span>\n'
        f'  <h3><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="blog-meta">{art["date"]} &middot; 26 min read</div>\n'
        f'</article>\n\n'
    )


def insert_at_top(html, new_cards):
    pattern = re.compile(r'(<article\s+class="blog-card">)', re.IGNORECASE)
    matches = list(pattern.finditer(html))
    if matches:
        first = matches[0]
        return html[:first.start()] + new_cards + html[first.start():]

    pattern2 = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m2 = pattern2.search(html)
    if m2:
        return html[:m2.end()] + new_cards + html[m2.end():]

    return html + new_cards


def update_index_page(file_path, card_html, art):
    if not os.path.exists(file_path):
        print(f"{file_path}: not found")
        return
    with open(file_path, encoding="utf-8") as f:
        html = f.read()
    if art["file"] in html:
        print(f"{art['file']} already in {file_path} — skipping")
        return
    new_html = insert_at_top(html, card_html)
    if new_html == html:
        print(f"{file_path}: no anchor found, appending")
        new_html = html + card_html
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"{file_path}: updated with {art['file']}")


def update_sitemap(sitemap_path, art):
    if not os.path.exists(sitemap_path):
        print(f"{sitemap_path}: not found")
        return
    with open(sitemap_path, encoding="utf-8") as f:
        s = f.read()
    url_full = f"{BASE}/{art['file']}"
    if url_full in s:
        print(f"{art['file']} already in {sitemap_path} — skipping")
        return
    block = (
        "  <url>\n"
        f"    <loc>{url_full}</loc>\n"
        f"    <lastmod>{art['date']}</lastmod>\n"
        "    <changefreq>weekly</changefreq>\n"
        "    <priority>0.85</priority>\n"
        "  </url>\n"
    )
    s = s.replace("</urlset>", block + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(s)
    print(f"sitemap.xml: appended {art['file']}")


emoji_203 = "#1abc9c"
emoji_204 = "#27ae60"

en_203 = card_en(ART203, emoji_203)
en_204 = card_en(ART204, emoji_204)
blog_203 = card_blog(ART203, "📊")
blog_204 = card_blog(ART204, "♻️")

update_index_page(os.path.join(WORK, "en-blog.html"), en_203 + en_204, ART203)
update_index_page(os.path.join(WORK, "en-blog.html"), en_203 + en_204, ART204)
update_index_page(os.path.join(WORK, "blog.html"), blog_203 + blog_204, ART203)
update_index_page(os.path.join(WORK, "blog.html"), blog_203 + blog_204, ART204)
update_sitemap(os.path.join(WORK, "sitemap.xml"), ART203)
update_sitemap(os.path.join(WORK, "sitemap.xml"), ART204)
