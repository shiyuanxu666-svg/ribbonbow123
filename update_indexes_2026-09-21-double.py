#!/usr/bin/env python3
"""Update en-blog.html, blog.html and sitemap.xml with articles 186-AM + 187-PM — 2026-09-21 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-21"

ART186 = {
    "file": "blog-ribbon-oem-b2b-186-module-mill-side-q1-2027-tariff-engineering-country-of-origin-diversification-fta-utilization-drawback-ftz-bonded-warehouse-architecture-b2b-oem-program-resilience-2026-09-21-am.html",
    "title": "Ribbon OEM B2B 186-Module Mill-Side Q1-2027 Tariff-Engineering Country-of-Origin Diversification FTA Utilization Drawback FTZ Bonded-Warehouse Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Tariff-Engineering Country-of-Origin Diversification FTA Utilization Drawback FTZ Bonded-Warehouse Architecture",
    "date": TODAY,
    "desc": "186-module mill-side Q1-2027 tariff-engineering country-of-origin diversification FTA-utilization drawback FTZ bonded-warehouse architecture (22-origin country-diversification heat-map, 19-stage FTA-preference qualification workflow, 17-stage Section-301 List-4A/4B-era tariff-engineering playbook, 15-stage duty-drawback recovery sprint, 13-stage FTZ activation ladder, 11-stage bonded-warehouse utilization map, 9-stage country-of-origin marking sprint, 7-stage transshipment audit, 5-stage FX-hedging ladder, 3-stage tariff-monitoring radar) for global brand procurement and Q1-2027 trade-compliance teams. End: 21-38% tariff-cost compression, 14-26pp FTA-utilization lift, 9-18% COGS-protection stabilization.",
}
ART187 = {
    "file": "blog-ribbon-oem-b2b-187-module-mill-side-q1-2027-carbon-adjusted-tco-procurement-decarbonization-scope-3-espr-cbam-csrd-dpp-architecture-b2b-oem-program-resilience-2026-09-21-pm.html",
    "title": "Ribbon OEM B2B 187-Module Mill-Side Q1-2027 Carbon-Adjusted TCO Procurement Decarbonization Scope-3 ESPR/CBAM/CSRD/DPP Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Carbon-Adjusted TCO Procurement Decarbonization Scope-3 ESPR/CBAM/CSRD/DPP Architecture",
    "date": TODAY,
    "desc": "187-module mill-side Q1-2027 carbon-adjusted TCO procurement decarbonization Scope-3 ESPR/CBAM/CSRD/DPP architecture (24-component carbon-adjusted TCO model, 19-stage Scope-3 LCA-boundary methodology, 17-stage CBAM compliance workflow, 15-stage ESPR Digital Product Passport build, 13-stage CSRD/ESRS-E1 disclosure sprint, 11-stage verified-PCF substantiation, 9-stage mill-side decarbonization roadmap, 7-stage retailer-green-premium pricing pass-through, 5-stage supplier-cascade KPI chain, 3-stage annual-disclosure cadence) for global brand procurement and Q1-2027 ESG controllers. End: 26-44% Scope-1+2 absolute reduction, 19-32pp retailer-green-premium capture, 14-22% carbon-adjusted-TCO compression.",
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
        f'<article class="blog-post-card" data-category="{art["cat"]}">\n'
        f'  <a href="{art["file"]}" class="blog-post-thumb" style="background:linear-gradient(135deg,#1a5276,{emoji});" aria-label="{art["title"][:60]}"></a>\n'
        f'  <div class="blog-post-content">\n'
        f'    <span class="blog-post-category">{art["cat"]}</span>\n'
        f'    <h3 class="blog-post-title"><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'    <div class="blog-post-meta">📅 {art["date"]} · ⏱ 26 min read</div>\n'
        f'    <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'    <a href="{art["file"]}" class="blog-post-link">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


def insert_after_grid(html, new_cards):
    pattern = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m = pattern.search(html)
    if m:
        return html[:m.end()] + "\n" + new_cards + html[m.end():]
    pat2 = re.compile(r'(<ul\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
    m2 = pat2.search(html)
    if m2:
        return html[:m2.end()] + "\n" + new_cards + html[m2.end():]
    pat3 = re.compile(r'(<div\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
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
        new_html = insert_after_grid(html, "\n".join(cards_to_add))
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
        new_html = insert_after_grid(html, "\n".join(cards_to_add))
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
    arts = [ART186, ART187]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)