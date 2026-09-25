#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 199-AM + 200-PM — 2026-09-25 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-25"

ART199 = {
    "file": "blog-ribbon-oem-b2b-199-module-mill-side-q1-2027-oem-custom-packaging-specification-engineering-19-layer-bill-of-materials-architecture-b2b-oem-program-resilience-2026-09-25-am.html",
    "title": "Ribbon OEM B2B 199-Module Mill-Side Q1-2027 OEM-Custom-Packaging-Specification-Engineering 19-Layer Bill-of-Materials Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 OEM-Custom-Packaging-Specification-Engineering 19-Layer Bill-of-Materials Architecture",
    "date": TODAY,
    "desc": "199-module mill-side Q1-2027 OEM-custom-packaging-specification-engineering 19-layer bill-of-materials architecture (Layer 1-4 substrate-backing-lamination-edge-treatment, Layer 5-8 print-stack-color-profile-finish-cascade-sublimation-channel, Layer 9-12 colorant-chemistry-dye-class-fixation-wash-fastness, Layer 13-16 sustainability-claim recycled-content bio-substrate certification-chain, Layer 17-19 conversion-tolerance-pack-specification-compliance-labeling; PFSS print-finish specification sheet, ISO 105-C06 AATCC 8 AATCC 16 wash-fastness, ESPR CSRD DPP digital-product-passport, EN-13402 ISO 3758 textile-care-labeling) for global brand procurement and Q1-2027 merchandising controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART200 = {
    "file": "blog-ribbon-oem-b2b-200-module-mill-side-q1-2027-smart-specimen-co-design-portal-ai-visual-library-ai-augmented-color-stewardship-architecture-b2b-oem-program-resilience-2026-09-25-pm.html",
    "title": "Ribbon OEM B2B 200-Module Mill-Side Q1-2027 Smart-Specimen-Co-Design-Portal AI-Visual-Library AI-Augmented Color-Stewardship Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Smart-Specimen-Co-Design-Portal AI-Visual-Library AI-Augmented Color-Stewardship Architecture",
    "date": TODAY,
    "desc": "200-module mill-side Q1-2027 smart-specimen-co-design-portal AI-visual-library AI-augmented color-stewardship architecture (Stage 1-3 brief-ingest asset-normalization color-intent-translation, Stage 4-6 virtual-swatch-render AI-visual-library substrate-aware delta-E-prediction, Stage 7-9 mill-side-swatch-fabrication co-design-review approval-lock; AI-visual-library 14000-19000 records, Pantone-FHI translation-engine 9400-14000 translations, delta-E less than 1.0 substrate-aware, light-source-compensation D65 D50 A F11, 38-64 substrate-library indexing, 14-day color-stewardship review cadence) for global brand procurement and Q1-2027 merchandising design leads. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
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
        return html[:m2.end()] + "\n" + new_cards + html[m2.end():]

    pat3 = re.compile(r'(<ul\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
    m3 = pat3.search(html)
    if m3:
        return html[:m3.end()] + "\n" + new_cards + html[m3.end():]

    return html.replace("</body>", new_cards + "\n</body>")


def update_en_blog(arts):
    path = os.path.join(WORK, "en-blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    emojis = ["#1abc9c", "#d4367c"]
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        if art["file"] in html:
            print(f"{art['file']} already in en-blog.html — skipping")
            continue
        cards_to_add.append(card_en(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_at_top(html, "\n".join(cards_to_add))
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"UPDATED {path} ({len(cards_to_add)} cards)")
    elif not changed:
        print(f"en-blog.html: no changes")


def update_blog_html(arts):
    path = os.path.join(WORK, "blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    emojis = ["#1abc9c", "#d4367c"]
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        if art["file"] in html:
            print(f"{art['file']} already in blog.html — skipping")
            continue
        cards_to_add.append(card_blog(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_at_top(html, "\n".join(cards_to_add))
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"UPDATED {path} ({len(cards_to_add)} cards)")
    elif not changed:
        print(f"blog.html: no changes")


def update_sitemap(arts):
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        sm = f.read()
    changed = False
    for art in arts:
        if art["file"] in sm:
            print(f"{art['file']} already in sitemap.xml — skipping")
            continue
        block = (
            "  <url>\n"
            f"    <loc>{BASE}/{art['file']}</loc>\n"
            f"    <lastmod>{art['date']}</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.85</priority>\n"
            "  </url>\n"
        )
        sm = sm.replace("</urlset>", block + "</urlset>")
        changed = True
        print(f"INSERTED {art['file']} into sitemap.xml")
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(sm)


if __name__ == "__main__":
    arts = [ART199, ART200]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)