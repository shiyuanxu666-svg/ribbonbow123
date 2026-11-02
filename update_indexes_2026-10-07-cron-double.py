#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 243-AM + 244-PM — 2026-10-07 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-07"

ART243 = {
    "file": "blog-ribbon-oem-b2b-243-module-mill-side-q1-2027-oem-custom-branded-ribbon-concept-to-shelf-21-stage-brief-to-shipment-workflow-architecture-b2b-oem-program-resilience-2026-10-07-am.html",
    "title": "Ribbon OEM B2B 243-Module Mill-Side Q1-2027 21-Stage OEM Custom-Branded Ribbon Concept-to-Shelf Brief-to-Shipment Workflow Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 21-Stage OEM Custom Branded Ribbon Concept to Shelf Brief to Shipment Workflow Architecture",
    "date": TODAY,
    "desc": "243-module mill-side Q1-2027 21-stage OEM custom-branded ribbon concept-to-shelf brief-to-shipment workflow architecture (21-stage brand-brief artwork-pre-press color-library sample-parallel-track inline-yield-tooling PPAP-pre-production AI-vision-AQL cartonization DC-routing pre-shipment-AQL brand-launch-activation launch-runway brand-exit-protocol decoder, 23-component should-cost quote-decoder, 25-signal supplier-selection framework alignment, AI-augmented Pantone-FHI color-stewardship Delta-E lot-to-lot continuity, Jetson-AGX-Orin edge-AI inline defect-detection closed-loop yield-recovery) for global brand owners and Q1 2027 launch-readiness controllers. Lift: 32-58% speed-to-market compression, 6-12% landed-cost savings lift, 4-9% program-lifetime-margin-lift.",
}
ART244 = {
    "file": "blog-ribbon-oem-b2b-244-module-mill-side-q1-2027-oem-supplier-selection-cost-analysis-25-signal-12-kpi-framework-architecture-b2b-oem-program-resilience-2026-10-07-pm.html",
    "title": "Ribbon OEM B2B 244-Module Mill-Side Q1-2027 25-Signal 12-KPI OEM Supplier-Selection Cost-Analysis Framework Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 25 Signal 12 KPI OEM Supplier Selection Cost Analysis Framework Architecture",
    "date": TODAY,
    "desc": "244-module mill-side Q1-2027 25-signal 12-KPI OEM supplier-selection cost-analysis framework architecture (25-signal framework covering 14-station on-site qualification, 18-signal cert compliance BSCI-SEDEX-SMETA-OEKO-TEX-FSC-GRS-GOTS-ISO-9001-14001-45001, 12-signal financial-health D&B-rating working-capital quick-ratio, 23-component should-cost quote-decoder, multi-currency FX-hedging, tariff-aware cost architecture Section-301-list-4A-4B EU-CBAM FTA-utilization, 12-KPI framework OEE greater-than-85% defect-rate-less-than-0.4% energy-productivity-less-than-4.2-kWh/m3 water-productivity-less-than-38-L/kg carbon-productivity-less-than-3.8-kgCO2e/kg color-delta-E-less-than-1.0 on-time-delivery-greater-than-96% compliance-coverage IP-protection brand-exit-protocol QBR-cadence) for global brand owners and Q1 2027 finance controllers. Lift: 36-62% should-cost leak compression, 5-11% margin lift per supplier, 4-10% program-lifetime-margin-lift.",
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
    update_en_blog([ART243, ART244])
    print("--- Updating blog.html ---")
    update_blog([ART243, ART244])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART243, ART244])
    print("Done.")