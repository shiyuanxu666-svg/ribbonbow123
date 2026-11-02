#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 207-AM + 208-PM — 2026-09-27 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-27"

ART207 = {
    "file": "blog-ribbon-oem-b2b-207-module-mill-side-q1-2027-cross-border-tariff-engineering-country-of-origin-fta-utilization-hs-code-digitization-dpp-traceability-architecture-b2b-oem-program-resilience-2026-09-27-am.html",
    "title": "Ribbon OEM B2B 207-Module Mill-Side Q1-2027 Cross-Border Tariff-Engineering Country-of-Origin FTA-Utilization HS-Code-Digitization DPP-Traceability Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Cross-Border Tariff-Engineering Country-of-Origin FTA-Utilization HS-Code-Digitization DPP-Traceability Architecture",
    "date": TODAY,
    "desc": "207-module mill-side Q1-2027 cross-border tariff-engineering country-of-origin FTA-utilization HS-code-digitization DPP-traceability architecture (7-node origin decision engine, 14-bilateral FTA pathway mapping, 19-digit HS-code classifier, 25-field Digital Product Passport, 7-lever tariff-engineering ROI decoder, 14-stage RACI workflow, 18-KPI scorecard) for global brand procurement and Q1 2027 landed-cost controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART208 = {
    "file": "blog-ribbon-oem-b2b-208-module-mill-side-q1-2027-ai-augmented-color-management-pantone-delta-e-closed-loop-batch-consistency-architecture-b2b-oem-program-resilience-2026-09-27-pm.html",
    "title": "Ribbon OEM B2B 208-Module Mill-Side Q1-2027 AI-Augmented Color-Management Pantone Delta-E Closed-Loop Batch-Consistency Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 AI-Augmented Color-Management Pantone Delta-E Closed-Loop Batch-Consistency Architecture",
    "date": TODAY,
    "desc": "208-module mill-side Q1-2027 AI-augmented color-management Pantone Delta-E closed-loop batch-consistency architecture (4,200-color Pantone FHI library, CMC/CIEDE2000/DIN99o tolerancer bank, 18-stage spectrophotometer-to-cloud pipeline, 7-module AI color-stewardship co-pilot, 9-destination-market shade-translation engine, 18-KPI scorecard, 4-quarter rolling improvement) for global brand procurement and Q1 2027 merchandising controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
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
    arts = [ART207, ART208]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)