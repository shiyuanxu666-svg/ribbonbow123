#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 241-AM + 242-PM — 2026-10-07 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-07"

ART241 = {
    "file": "blog-ribbon-oem-b2b-241-module-mill-side-q1-2027-24-stage-oem-custom-branded-ribbon-concept-to-label-brand-launch-oem-process-engineering-architecture-b2b-oem-program-resilience-2026-10-07-am.html",
    "title": "Ribbon OEM B2B 241-Module Mill-Side Q1-2027 24-Stage OEM Custom-Branded-Ribbon Concept-to-Label Brand-Launch OEM Process-Engineering Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 24-Stage OEM Custom Branded Ribbon Concept to Label Brand Launch OEM Process Engineering Architecture",
    "date": TODAY,
    "desc": "241-module mill-side Q1-2027 24-stage OEM custom-branded-ribbon concept-to-label brand-launch OEM process-engineering architecture (7-pillar cognitive fabric Mill-Side 19-Layer BOM Specification-Engineering Plane + AI-Augmented Pantone-FHI Color-Stewardship Plane + Tier-1-Tier-2-Tier-3 Brand-Launch Dual-Sourcing Bridge-Order-Migration Plane + Cross-Border Tariff-Engineering Country-of-Origin Plane + 14-Stage On-Site Brand-Launch Qualification Plane + Hidden-Landed-Cost Reverse-Engineering 19-Component Quote-Decoder Plane + Smart-Mill IIoT Edge-AI 14-Photo-Evidence Brand-Launch Plane, 24-stage brief-to-shelf concept-to-label brand-launch cognitive-fabric artwork-rider sample-approval PPAP pre-shipment-AQL brand-exit-protocol, 24-stage Pantone-co-design lab-dip print-test wash-rub-light-crocking-perspiration fastness decoder, AI-augmented Pantone-FHI color-stewardship Delta-E lot-to-lot continuity) for global brand owners and Q1 2027 launch-readiness controllers. Lift: 38-64% concept-to-shelf cycle-time compression, 4-11% NPI-speed lift per program, 4-11% program-lifetime-margin-lift.",
}
ART242 = {
    "file": "blog-ribbon-oem-b2b-242-module-mill-side-q1-2027-24-stage-oem-supplier-selection-cost-analysis-hidden-landed-cost-reverse-engineering-architecture-b2b-oem-program-resilience-2026-10-07-pm.html",
    "title": "Ribbon OEM B2B 242-Module Mill-Side Q1-2027 24-Stage OEM Supplier-Selection Cost-Analysis Hidden-Landed-Cost Reverse-Engineering Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 24-Stage OEM Supplier Selection Cost Analysis Hidden Landed Cost Reverse Engineering Architecture",
    "date": TODAY,
    "desc": "242-module mill-side Q1-2027 24-stage OEM supplier-selection cost-analysis hidden-landed-cost reverse-engineering architecture (7-pillar cognitive fabric Mill-Side 19-Component Quote-Decoder Plane + AI-Augmented Hidden-Cost-Radar Plane + Tier-1-Tier-2-Tier-3 Supplier-Resilience Dual-Sourcing Bridge-Order-Migration Plane + Cross-Border Tariff-Engineering Country-of-Origin FTA-HS-Code-Drawback-FTZ-Bonded-Warehouse Plane + 14-Station On-Site Supplier-Qualification Plane + AI-Augmented Supplier-Scorecard 20-KPI Plane + Smart-Mill IIoT Edge-AI 14-Photo-Evidence Cost-Audit Plane, 24-stage yarn-dye-weave-finish conversion overhead tariff freight DDP compliance quality packaging warehouse risk working-capital MOQ volume-mix tier-supplier dual-sourcing lead-time capex-amortization margin-reconciliation cost-decoder, AI-augmented hidden-cost-radar variable-cost-modeling supplier-relationship-management SRM tiered-QBR-cadence) for global brand owners and Q1 2027 finance controllers. Lift: 38-64% should-cost leak compression, 4-11% margin lift per supplier, 4-11% program-lifetime-margin-lift.",
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
    update_en_blog([ART241, ART242])
    print("--- Updating blog.html ---")
    update_blog([ART241, ART242])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART241, ART242])
    print("Done.")