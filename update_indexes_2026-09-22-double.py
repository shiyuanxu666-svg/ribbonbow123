#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 188-AM + 189-PM — 2026-09-22 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-22"

ART188 = {
    "file": "blog-ribbon-oem-b2b-188-module-mill-side-q1-2027-private-label-oem-onboarding-22-stage-welcome-kit-architecture-b2b-oem-program-resilience-2026-09-22-am.html",
    "title": "Ribbon OEM B2B 188-Module Mill-Side Q1-2027 Private-Label OEM Onboarding 22-Stage Welcome-Kit Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Private-Label OEM Onboarding 22-Stage Welcome-Kit Architecture",
    "date": TODAY,
    "desc": "188-module mill-side Q1-2027 private-label OEM onboarding 22-stage welcome-kit architecture (22-stage welcome-kit onboarding ladder, 19-stage quality-manual handover build, 17-stage social-audit dossier architecture, 15-stage ESG-dossier architecture, 13-stage color-management onboarding build, 11-stage AQL and inspection-standard handover, 9-stage artwork-and-print-pipeline onboarding, 7-stage logistics-and-documents package, 5-stage QBR and continuous-improvement cadence) for global brand procurement and Q1-2027 private-label merchandising controllers. Lift: 21-38% chargeback-compression, 14-26 days first-PO compression, 4-11% program-lifetime-margin-lift per year.",
}
ART189 = {
    "file": "blog-ribbon-oem-b2b-189-module-mill-side-q1-2027-supplier-financial-health-tier-2-tier-3-rating-monitoring-procurement-resilience-architecture-b2b-oem-program-resilience-2026-09-22-pm.html",
    "title": "Ribbon OEM B2B 189-Module Mill-Side Q1-2027 Supplier-Financial-Health Tier-2 Tier-3 Rating Monitoring Procurement-Resilience Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Supplier-Financial-Health Tier-2 Tier-3 Rating Monitoring Procurement-Resilience Architecture",
    "date": TODAY,
    "desc": "189-module mill-side Q1-2027 supplier-financial-health tier-2/tier-3/tier-4 rating monitoring procurement-resilience architecture (22-supplier financial-health tier-1/2/3/4 rating map, 19-stage Altman-Z plus custom-composite financial-health rating, 17-stage tier-2/3 cascade-disruption early-warning system, 15-stage tier-2/3 supplier-pool diversification ladder, 13-stage working-capital rescue sprint, 11-stage audit-grade cascade monitor, 9-stage capacity-utilization anomaly watch, 7-stage geopolitical-and-climate-event cascade map, 5-stage quarterly rating refresh) for global brand procurement and Q1-2027 finance controllers. End-state: 38-64% single-supplier-collapse-exposure compression, 100% Q4-fill rate, 4-11% program-lifetime-margin-lift per year.",
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
    """Find best insertion point - the most recent blog-card article block."""
    # Pattern A: Insert before the first existing blog-card article
    pattern = re.compile(r'(<article\s+class="blog-card">)', re.IGNORECASE)
    matches = list(pattern.finditer(html))
    if matches:
        # Insert at the FIRST article (newest content goes on top)
        first = matches[0]
        return html[:first.start()] + new_cards + html[first.start():]

    # Pattern B: posts-grid
    pattern2 = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m2 = pattern2.search(html)
    if m2:
        return html[:m2.end()] + "\n" + new_cards + html[m2.end():]

    # Pattern C: blog-list ul/div
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
    arts = [ART188, ART189]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)
