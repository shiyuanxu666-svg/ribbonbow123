#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 221-AM + 222-PM — 2026-09-30 cron double (v2)."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-30"

ART221 = {
    "file": "blog-ribbon-oem-b2b-221-module-mill-side-q1-2027-22-stage-tier-1-2-3-supplier-resilience-q4-2026-holiday-peak-pre-booking-multi-country-diversification-bridge-migration-architecture-b2b-oem-program-resilience-2026-09-30-am.html",
    "title": "Ribbon OEM B2B 221-Module Mill-Side Q1-2027 22-Stage Tier 1 2 3 Supplier Resilience Architecture Q4 2026 Holiday Peak Capacity Pre-Booking Multi-Country Manufacturing Diversification Bridge-Order Migration B2B OEM Program Resilience",
    "cat": "Q1-2027 22-Stage Tier 1 2 3 Supplier Resilience Q4 2026 Holiday Peak Pre-Booking Multi-Country Diversification Bridge Migration Architecture",
    "date": TODAY,
    "desc": "221-module mill-side Q1-2027 22-stage tier-1-2-3 supplier-resilience architecture (Q4-2026 holiday-peak capacity pre-booking 60% China-mill + 25% Vietnam/Indonesia/Cambodia/Bangladesh bridge-factory + 15% Mexico/DR/Honduras near-shore backup, dual-sourcing split-order-allocation with 14-day bridge-order migration, 6-dimension AI-driven capacity-risk-radar monitoring capacity / financial-health / geopolitical / climate / FX / tariff risk, USMCA / CAFTA-DR / RCEP / CPTPP / EVFTA / VKFTA FTA-eligibility, 7-pillar compounding capacity-resilience margin asset) for global brand procurement and Q1 2027 supply-chain controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART222 = {
    "file": "blog-ribbon-oem-b2b-222-module-mill-side-q1-2027-24-stage-tariff-engineering-country-of-origin-diversification-fta-hs-code-drawback-ftz-bonded-warehouse-dpp-architecture-b2b-oem-program-resilience-2026-09-30-pm.html",
    "title": "Ribbon OEM B2B 222-Module Mill-Side Q1-2027 24-Stage Tariff Engineering Country-of-Origin Diversification FTA Utilization HS Code Digitization Drawback FTZ Bonded Warehouse DPP Traceability Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 24-Stage Tariff Engineering Country-of-Origin Diversification FTA HS-Code Drawback FTZ Bonded-Warehouse DPP Architecture",
    "date": TODAY,
    "desc": "222-module mill-side Q1-2027 24-stage tariff-engineering architecture (5806/5807/5808 textile-ribbon HS-code sub-classification with material/width/print/finish granularity, 9-FTA RCEP/CPTPP/EVFTA/VKFTA/USMCA/CAFTA-DR/ASEAN/China-Korea/China-Japan-Korea eligibility screening, Section-301 drawback 1313(j) 19 USC, FTZ 81a, bonded-warehouse 1551, 6-component multi-currency tariff-pass-through negotiation with FX-hedging, Digital Product Passport DPP ESPR-compliance DPP-QR-code DPP-NFC-tag DPP-blockchain-record, 7-pillar compounding country-of-origin-diversification margin asset) for global brand procurement and Q1 2027 finance controllers. Lift: 4-11% landed-cost savings, 28-64% Section-301-list-4a-4b-tariff-exposure compression, 4-11% program-lifetime-margin-lift per year.",
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
    """Insert cards_text right after the first match of marker_regex."""
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
    update_en_blog([ART221, ART222])
    print("--- Updating blog.html ---")
    update_blog([ART221, ART222])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART221, ART222])
    print("Done.")
