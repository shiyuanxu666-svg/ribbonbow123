#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 193-AM + 194-PM — 2026-09-23 double (v2)."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-23"

ART193 = {
    "file": "blog-ribbon-oem-b2b-193-module-mill-side-q1-2027-private-label-oem-onboarding-90-day-npi-speed-to-market-7-stage-architecture-b2b-oem-program-resilience-2026-09-23-am.html",
    "title": "Ribbon OEM B2B 193-Module Mill-Side Q1-2027 Private-Label OEM Onboarding 90-Day NPI Speed-to-Market 7-Stage Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Private-Label OEM Onboarding 90-Day NPI Speed-to-Market 7-Stage Architecture",
    "date": TODAY,
    "desc": "193-module mill-side Q1-2027 private-label OEM onboarding 90-day NPI speed-to-market 7-stage architecture (welcome kit + confidentiality rider, artwork rider + print-ready handoff, color stewardship + Delta-E closed loop, sample parallel-track + pre-production run, PPAP + pre-shipment FAT, EDI/CPQ/VMI integration + flow-down launch checklist, brand-exit protocol + continuity-of-supply) for global brand procurement and Q1-2027 NPI program managers. Lift: 60-75% calendar compression, 38-64% retailer-onboarding-cycle compression, 4-11% program-lifetime-margin-lift per year.",
}
ART194 = {
    "file": "blog-ribbon-oem-b2b-194-module-mill-side-q1-2027-should-cost-reverse-engineering-22-component-quote-decoder-tariff-aware-carbon-adjusted-tco-architecture-b2b-oem-program-resilience-2026-09-23-pm.html",
    "title": "Ribbon OEM B2B 194-Module Mill-Side Q1-2027 Should-Cost Reverse-Engineering 22-Component Quote-Decoder Tariff-Aware Carbon-Adjusted TCO Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Should-Cost Reverse-Engineering 22-Component Quote-Decoder Tariff-Aware Carbon-Adjusted TCO Architecture",
    "date": TODAY,
    "desc": "194-module mill-side Q1-2027 should-cost reverse-engineering 22-component quote-decoder tariff-aware carbon-adjusted TCO architecture (yarn-forward variable-cost decomposition, dye/print/finish process-cost layer, overhead & mill-substrate allocation engine, packaging/labeling/retailer-compliance cost, freight/duty/tariff/Incoterm layer, FX-hedging/working-capital/payment-term layer, carbon-adjusted TCO + Scope-3 layer) for global brand procurement and Q1-2027 finance controllers. Lift: 4-11% landed-cost savings, 32K-88K USD FX-hedge recovery per year, 4-11% program-lifetime-margin-lift per year.",
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
    arts = [ART193, ART194]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)