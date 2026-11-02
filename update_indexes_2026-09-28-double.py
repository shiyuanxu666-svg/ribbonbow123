#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 209-AM + 210-PM — 2026-09-28 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-28"

ART209 = {
    "file": "blog-ribbon-oem-b2b-209-module-mill-side-q1-2027-sku-rationalization-volume-mix-portfolio-engineering-private-label-brand-owner-architecture-b2b-oem-program-resilience-2026-09-28-am.html",
    "title": "Ribbon OEM B2B 209-Module Mill-Side Q1-2027 AI-Augmented SKU-Rationalization Volume-Mix Portfolio-Engineering Private-Label Brand-Owner Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 SKU-Rationalization Volume-Mix Portfolio-Engineering Private-Label Brand-Owner Architecture",
    "date": TODAY,
    "desc": "209-module mill-side Q1-2027 SKU-rationalization volume-mix portfolio-engineering architecture (14-signal margin-leakage diagnostic, 10,000-trial Monte Carlo SKU mix optimizer, 7-tier mill-side MOQ negotiation bundle, SMED 38-to-6-minute changeover program, 12-stage dynamic-replenishment inventory buffer engine, 18-stage SKU retirement / consolidation workflow with cross-program art-work re-use) for global brand procurement and Q1 2027 finance controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART210 = {
    "file": "blog-ribbon-oem-b2b-210-module-mill-side-q1-2027-brand-buyer-private-label-concept-to-shelf-speed-to-market-90-day-npi-architecture-b2b-oem-program-resilience-2026-09-28-pm.html",
    "title": "Ribbon OEM B2B 210-Module Mill-Side Q1-2027 Brand-Buyer Private-Label Concept-to-Shelf Speed-to-Market 90-Day NPI Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Brand-Buyer Private-Label Concept-to-Shelf Speed-to-Market 90-Day NPI Architecture",
    "date": TODAY,
    "desc": "210-module mill-side Q1-2027 brand-buyer private-label concept-to-shelf speed-to-market 90-day NPI architecture (22-stage brief-to-shelf workflow decoder, 4-stream parallel-track art-work and color-approval compression, 9-stage bulk-production cycle compression with SMED changeover, 7-stage pre-shipment QA and DPP generation, 18-KPI Q1 launch readiness scorecard, 22-stage RACI implementation workflow) for global brand procurement and Q1 2027 merchandising controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
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
    for art, em in zip(arts, emojis):
        if art["file"] in html:
            print(f"  en-blog already has {art['file']}")
            continue
        cards_to_add.append(card_en(art, em))
        changed = True
    if not changed:
        return
    new_cards = "\n".join(cards_to_add) + "\n"
    html = insert_at_top(html, new_cards)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"updated {path}")


def update_blog(arts):
    path = os.path.join(WORK, "blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    emojis = ["#1abc9c", "#d4367c"]
    changed = False
    cards_to_add = []
    for art, em in zip(arts, emojis):
        if art["file"] in html:
            print(f"  blog.html already has {art['file']}")
            continue
        cards_to_add.append(card_blog(art, em))
        changed = True
    if not changed:
        return
    new_cards = "".join(cards_to_add)
    html = insert_at_top(html, new_cards)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"updated {path}")


def update_sitemap(arts):
    path = os.path.join(WORK, "sitemap.xml")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        xml = f.read()
    changed = False
    for art in arts:
        url = f"{BASE}/{art['file']}"
        if url in xml:
            print(f"  sitemap already has {url}")
            continue
        # Insert before </urlset>
        entry = (
            f"  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <lastmod>{art['date']}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.8</priority>\n"
            f"  </url>\n"
        )
        xml = xml.replace("</urlset>", entry + "</urlset>")
        changed = True
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(xml)
        print(f"updated {path}")


if __name__ == "__main__":
    arts = [ART209, ART210]
    update_en_blog(arts)
    update_blog(arts)
    update_sitemap(arts)
    print("done")