#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 205-AM + 206-PM — 2026-09-26 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-26"

ART205 = {
    "file": "blog-ribbon-oem-b2b-205-module-mill-side-q1-2027-brand-buyer-private-label-ribbon-oem-tco-decoder-25-component-quote-reverse-engineering-architecture-b2b-oem-program-resilience-2026-09-26-am.html",
    "title": "Ribbon OEM B2B 205-Module Mill-Side Q1-2027 Brand-Buyer Private-Label Ribbon-OEM Total-Cost-of-Ownership TCO-Decoder 25-Component Quote-Reverse-Engineering Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Brand-Buyer Private-Label Ribbon-OEM Total-Cost-of-Ownership TCO-Decoder 25-Component Quote-Reverse-Engineering Architecture",
    "date": TODAY,
    "desc": "205-module mill-side Q1-2027 brand-buyer private-label ribbon-OEM total-cost-of-ownership TCO-decoder 25-component quote-reverse-engineering architecture (25-component quote anatomy, 19 hidden-cost-radar cost-drivers, 6-stage reverse-engineering sequence, 12 brand-buyer negotiation-leverage points, 5-step Q1 2027 hidden-cost-radar rollout, 18-KPI scorecard, multi-year supply-agreement framework) for global brand procurement and Q1 2027 merchandising controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART206 = {
    "file": "blog-ribbon-oem-b2b-206-module-mill-side-q1-2027-supplier-financial-health-tier-2-tier-3-sub-supplier-rating-monitoring-srm-resilience-early-warning-architecture-b2b-oem-program-resilience-2026-09-26-pm.html",
    "title": "Ribbon OEM B2B 206-Module Mill-Side Q1-2027 Supplier-Financial-Health Tier-2-Tier-3 Sub-Supplier Rating Monitoring SRM-Resilience Early-Warning Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Supplier-Financial-Health Tier-2-Tier-3 Sub-Supplier Rating Monitoring SRM-Resilience Early-Warning Architecture",
    "date": TODAY,
    "desc": "206-module mill-side Q1-2027 supplier-financial-health tier-2-tier-3 sub-supplier rating monitoring SRM-resilience early-warning architecture (12-signal sub-supplier financial-health decoder, 8 early-warning triggers, 6 monitoring cadences, Playbook A dual-sourcing bridge qualification, Playbook B bridge-order migration, Playbook C emergency qualification, Playbook D tier-1-mill substitution, 18-KPI SRM scorecard) for global brand procurement and Q1 2027 finance controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
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
    arts = [ART205, ART206]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)