#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 271-AM + 272-PM — 2026-10-17 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-17"

ART271 = {
    "file": "blog-ribbon-oem-b2b-271-module-mill-side-q1-2027-oem-private-label-supplier-onboarding-22-stage-ramp-up-welcome-kit-7-stage-knowledge-transfer-runway-tracker-architecture-b2b-oem-program-resilience-2026-10-17-am.html",
    "title": "Ribbon OEM B2B 271-Module Mill-Side Q1-2027 22-Stage OEM Private-Label Custom Branded Ribbon Onboarding Ramp-Up Welcome-Kit 7-Stage Knowledge-Transfer Runway-Tracker Architecture for Brand Buyers and Procurement Managers",
    "cat": "Q1-2027 22 Stage OEM Private Label Custom Branded Ribbon Onboarding Ramp Up Welcome Kit 7 Stage Knowledge Transfer Runway Tracker Architecture",
    "date": TODAY,
    "desc": "271-module mill-side Q1-2027 22-stage OEM private-label custom branded ribbon supplier onboarding ramp-up welcome-kit 7-stage knowledge-transfer runway-tracker architecture for global brand owners and Q1 2027 finance controllers. Lift: 18-38 percent supplier-shortlist compression, 14-32 day first-PO-cycle compression, 56k-248k USD avoidable-cost recovery.",
}
ART272 = {
    "file": "blog-ribbon-oem-b2b-272-module-mill-side-q1-2027-oem-cost-engineering-22-component-should-cost-19-component-tariff-aware-landed-cost-multi-currency-fx-hedging-architecture-b2b-oem-program-resilience-2026-10-17-pm.html",
    "title": "Ribbon OEM B2B 272-Module Mill-Side Q1-2027 OEM Cost-Engineering 22-Component Should-Cost 19-Component Tariff-Aware Landed-Cost Multi-Currency FX-Hedging Architecture for Brand Buyers and Finance Controllers",
    "cat": "Q1-2027 OEM Cost Engineering 22 Component Should Cost 19 Component Tariff Aware Landed Cost Multi Currency FX Hedging Architecture",
    "date": TODAY,
    "desc": "272-module mill-side Q1-2027 OEM cost-engineering 22-component should-cost 19-component tariff-aware landed-cost multi-currency FX-hedging architecture for global brand owners and Q1 2027 finance controllers. Lift: 4-11 percent landed-cost savings, 38-64 percent supplier-quote decoder transparency lift, 32k-88k USD FX-hedge recovery.",
}


def card_en(art, emoji_color):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji_color});">{emoji_color.replace("#","")}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 26 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def card_blog(art):
    return (
        f'<article class="blog-card">\n'
        f'  <span class="blog-tag">{art["cat"]}</span>\n'
        f'  <h3><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="blog-meta">{art["date"]} &middot; 26 min read</div>\n'
        f'</article>\n\n'
    )


def insert_at_top(html, cards_text, marker_regex):
    m = re.search(marker_regex, html, flags=re.IGNORECASE)
    if not m:
        m = re.search(r"</header\s*>", html, flags=re.IGNORECASE)
    if not m:
        return html + "\n" + cards_text
    end = m.end()
    return html[:end] + "\n" + cards_text + html[end:]


def update_en_blog(arts):
    path = os.path.join(WORK, "en-blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    cards_to_add = []
    changed = False
    for art in arts:
        if art["file"] in html:
            print(f"  EN-BLOG: {art['file']} already present")
            continue
        emoji_color = "#1abc9c" if "am" in art["file"] else "#7b2cbf"
        cards_to_add.append(card_en(art, emoji_color))
        changed = True
    if changed:
        new_cards_text = "".join(cards_to_add)
        updated = insert_at_top(html, new_cards_text, r'<div\s+class\s*=\s*["\']blog-grid["\']')
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED en-blog.html with {len(cards_to_add)} new card(s)")


def update_blog(arts):
    path = os.path.join(WORK, "blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    cards_to_add = []
    changed = False
    for art in arts:
        if art["file"] in html:
            print(f"  BLOG: {art['file']} already present")
            continue
        cards_to_add.append(card_blog(art))
        changed = True
    if changed:
        new_cards_text = "".join(cards_to_add)
        updated = insert_at_top(html, new_cards_text, r'<div\s+class\s*=\s*["\']blog-list["\']')
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED blog.html with {len(cards_to_add)} new card(s)")


def update_sitemap(arts):
    path = os.path.join(WORK, "sitemap.xml")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        xml = f.read()
    new_entries = []
    for art in arts:
        if art["file"] in xml:
            print(f"  SITEMAP: {art['file']} already in sitemap.xml")
            continue
        entry = (
            f"  <url>\n"
            f"    <loc>{BASE}/{art['file']}</loc>\n"
            f"    <lastmod>{TODAY}</lastmod>\n"
            f"    <changefreq>weekly</changefreq>\n"
            f"    <priority>0.85</priority>\n"
            f"  </url>\n"
        )
        new_entries.append(entry)
    if new_entries:
        closing = "</urlset>"
        idx = xml.rfind(closing)
        if idx == -1:
            print("  SITEMAP: </urlset> closing tag not found, appending at end")
            updated = xml + "\n".join(new_entries)
        else:
            updated = xml[:idx] + "".join(new_entries) + xml[idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED sitemap.xml with {len(new_entries)} new URL(s)")


if __name__ == "__main__":
    print("--- Updating en-blog.html ---")
    update_en_blog([ART271, ART272])
    print("--- Updating blog.html ---")
    update_blog([ART271, ART272])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART271, ART272])
    print("Done.")