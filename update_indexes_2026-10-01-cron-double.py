#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 224-AM + 225-PM — 2026-10-01 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-01"

ART224 = {
    "file": "blog-ribbon-oem-b2b-224-module-mill-side-q1-2027-22-stage-digital-trade-intelligence-supply-chain-command-center-architecture-b2b-oem-program-resilience-2026-10-01-am.html",
    "title": "Ribbon OEM B2B 224-Module Mill-Side Q1-2027 22-Stage Digital Trade-Intelligence Supply-Chain Command-Center Architecture for Global Brand Owners",
    "cat": "Q1-2027 22-Stage Digital Trade-Intelligence Supply-Chain Command-Center Architecture",
    "date": TODAY,
    "desc": "224-module mill-side Q1-2027 22-stage digital trade-intelligence supply-chain command-center architecture (6-pillar cognitive fabric UDL + Event-Bus + Identity-Plane + Policy-Engine + Cost-Engine + Insight-Plane, 24-stage HS-code sub-classification + 9-FTA eligibility screening, 19 USC 1313(j) drawback + FTZ 81a + bonded-warehouse 1551, 9-scenario Monte-Carlo supplier-mix Tier-1/2/3 bridge-order migration, 6-currency FX-hedging forward-NDF-knock-out carbon-adjusted-TCO, 23-component should-cost hidden-cost radar, 12-signal supplier-financial-health tier-2/tier-3 early-warning-radar, 19-stage 8D-report CAPA-NCR closed-loop, 7-pillar compounding digital-trade-intelligence margin asset) for global brand owners and Q1 2027 controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART225 = {
    "file": "blog-ribbon-oem-b2b-225-module-mill-side-q1-2027-23-stage-ai-augmented-color-stewardship-digital-twin-architecture-b2b-oem-program-resilience-2026-10-01-pm.html",
    "title": "Ribbon OEM B2B 225-Module Mill-Side Q1-2027 23-Stage AI-Augmented Color-Stewardship Digital-Twin Architecture for Global Brand Owners",
    "cat": "Q1-2027 23-Stage AI-Augmented Color-Stewardship Digital-Twin Architecture",
    "date": TODAY,
    "desc": "225-module mill-side Q1-2027 23-stage AI-augmented color-stewardship digital-twin architecture (7-pillar mill-side cognitive fabric inline-spectrophotometry + dye-recipe-versioning + inline-AOI-auto-reject + 9-light-source metamerism check + Pantone-FHI translation-engine + dual-sourcing color-divergence reconciler + DPP-ESPR-compliance color-disclosure, 9-substrate-and-finish recipe-robustness, 19-second L*a*b* stream AI-augmented dye-bath auto-adjustment, 9-light-source D65/D50/A/TL84/CWF/horizon/incandescent/LED-3000K/LED-4000K metamerism check, dual-sourcing Tier-1/Tier-2 color-divergence reconciliation bridge-order migration, DPP-QR-code + DPP-NFC-tag + DPP-blockchain-record ESRS-E1/CSRD/CBAM-phase-2, smart-specimen co-design portal 19-second virtual color-simulation, inline-AOI edge-AI Jetson-AGX-Orin Pareto-engine defect-stream, 19-batch lot-to-lot color-continuity recipe-versioning, 9-point brand-standard library Delta-E tolerance-band enforcer, 7-pillar compounding color-stewardship margin asset) for global brand owners and Q1 2027 controllers. Lift: 38-64% metamerism-recall-risk compression, 4-11% on-shelf color-consistency, 4-11% program-lifetime-margin-lift per year.",
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
    update_en_blog([ART224, ART225])
    print("--- Updating blog.html ---")
    update_blog([ART224, ART225])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART224, ART225])
    print("Done.")