#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 195-AM + 196-PM — 2026-09-24 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-24"

ART195 = {
    "file": "blog-ribbon-oem-b2b-195-module-mill-side-q1-2027-supplier-financial-health-monitoring-tier-2-tier-3-sub-supplier-12-signal-architecture-b2b-oem-program-resilience-2026-09-24-am.html",
    "title": "Ribbon OEM B2B 195-Module Mill-Side Q1-2027 Supplier-Financial-Health Monitoring Tier-2 Tier-3 Sub-Supplier 12-Signal Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Supplier-Financial-Health Monitoring Tier-2 Tier-3 Sub-Supplier 12-Signal Architecture",
    "date": TODAY,
    "desc": "195-module mill-side Q1-2027 supplier-financial-health monitoring tier-2 tier-3 sub-supplier 12-signal architecture (DSO, DPO, current/quick ratio, debt-to-equity, working-capital cycle, EBITDA margin, capex intensity, FX exposure, customer-concentration, refinancing calendar, ESG-bond readiness; plus refinancing-window 14-stage inventory buffer, dual-sourcing bridge-order 9-stage migration, 6-scenario Monte Carlo probability, Euler-Hermes Atradius Coface 14-country trade-credit matrix, 18-tier real-time heat-map, 11-stage parallel-track qualification, working-capital trade-finance engineering 19-country, 4-Q refinancing-calendar stress-test, 12-stage brand-exit protocol custody transfer, 60-day tier-2/tier-3 onboarding) for global brand procurement and Q1-2027 finance controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART196 = {
    "file": "blog-ribbon-oem-b2b-196-module-mill-side-q1-2027-supply-chain-finance-engineering-reverse-factoring-receivables-discounting-forfaiting-esg-linked-working-capital-architecture-b2b-oem-program-resilience-2026-09-24-pm.html",
    "title": "Ribbon OEM B2B 196-Module Mill-Side Q1-2027 Supply-Chain-Finance Engineering Reverse-Factoring Receivables-Discounting Forfaiting ESG-Linked Working-Capital Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Supply-Chain-Finance Engineering Reverse-Factoring Receivables-Discounting Forfaiting ESG-Linked Working-Capital Architecture",
    "date": TODAY,
    "desc": "196-module mill-side Q1-2027 supply-chain-finance engineering reverse-factoring receivables-discounting forfeiting ESG-linked working-capital architecture (14-country reverse-factoring envelopes, 9-country export-factor, 180- to 720-day forfeiting tenor, ESG-linked 6-milestone margin ratchet, dynamic-discounting pilot, 14-currency FX-hedging matrix, VMI 2.0 4-DC floor-plan, 9-lever cost-of-funds arbitrage ROI, tier-3 14-country sub-supplier factoring, 90-day cross-functional onboarding) for global brand procurement and Q1-2027 treasury controllers. Lift: 18-32% working-capital cycle compression, 32K-88K USD per-incident cost-recovery, 4-11% program-lifetime-margin-lift per year.",
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
    arts = [ART195, ART196]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)
