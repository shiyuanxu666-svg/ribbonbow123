#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 228-AM + 229-PM — 2026-10-02 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-02"

ART228 = {
    "file": "blog-ribbon-oem-b2b-228-module-mill-side-q1-2027-22-stage-factory-procurement-guide-14-station-on-site-qualification-18-signal-cert-compliance-rfi-rfp-rfq-onboarding-architecture-b2b-oem-program-resilience-2026-10-02-am.html",
    "title": "Ribbon OEM B2B 228-Module Mill-Side Q1-2027 22-Stage Factory Procurement Guide Architecture for Brand Owners Retailers and Sourcing Managers",
    "cat": "Q1-2027 22-Stage Factory Procurement Guide Architecture",
    "date": TODAY,
    "desc": "228-module mill-side Q1-2027 22-stage factory procurement guide architecture (7-pillar cognitive fabric Mill-Side Smart-Factory IIoT Edge-AI + Supplier-Financial-Health Tier-2 Tier-3 + HS-Code FTA-Utilization + Cross-Border Tariff-Engineering + Supplier-Certification-Compliance + Hidden-Landed-Cost Reverse-Engineering + Supplier-Relationship-Management, 14-station on-site factory qualification capacity-readiness, 18-signal BSCI SEDEX SMETA OEKO-TEX FSC GRS GOTS ISO-9001 14001 45001 cert-compliance decoder, 22-stage RFI RFP RFQ 24-component quote-decoder, 19-batch sample-approval parallel-track AI-vision AOI auto-reject, 12-signal supplier-financial-health early-warning-radar, 9-FTA eligibility 19 USC 1313(j) drawback FTZ 81a bonded-warehouse 1551, 24-component hidden-cost reverse-engineering, 25-stage OEE yield energy-water-carbon productivity smart-factory IIoT, 22-stage SRM tiered-QBR-cadence vendor-lifecycle governance, AI-vision edge-AI Jetson-AGX-Orin Pareto-engine defect-stream, cross-border Section-301-era list-4a-4b EU-CBAM phase-2 ASEAN FTA cascade, 7-pillar compounding factory procurement margin asset) for global brand owners and Q1 2027 controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART229 = {
    "file": "blog-ribbon-oem-b2b-229-module-mill-side-q1-2027-25-stage-oem-cost-analysis-supplier-selection-23-component-should-cost-quote-decoder-25-signal-framework-architecture-b2b-oem-program-resilience-2026-10-02-pm.html",
    "title": "Ribbon OEM B2B 229-Module Mill-Side Q1-2027 25-Stage OEM Cost Analysis and Supplier Selection Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 25-Stage OEM Cost Analysis and Supplier Selection Architecture",
    "date": TODAY,
    "desc": "229-module mill-side Q1-2027 25-stage OEM cost-analysis supplier-selection architecture (7-pillar cognitive fabric Should-Cost Quote-Decoder + Hidden-Cost Radar + Supplier-Selection Framework + Supplier-Certification-Compliance Decoder + Cross-Border Tariff-Engineering + Carbon-Adjusted-TCO Overlay + Supplier-Risk-Tiering Multi-Source, 23-component should-cost quote-decoder yarn-dye-weave-finish-conversion-overhead-tariff-freight, 19-component hidden-cost radar AI-augmented cost-driver visualisation, 25-signal 12-KPI supplier-selection framework capacity OEE productivity AQL-1.0 scorecard, 24-credential supplier-certification-compliance decoder BSCI SEDEX SMETA OEKO-TEX FSC GRS GOTS tender-RFP-RFI-RFQ, supplier-risk-tiering multi-source Tier-1 Tier-2 Tier-3 bridge-order migration 9-multi-country-diversification, cross-border tariff-engineering Section-301 list-4a-4b EU-CBAM phase-2 ASEAN FTA cascade, FX-hedging forward-NDF-knock-out 6-currency carbon-adjusted-TCO, CBAM phase-2 ESRS-E1 CSRD DPP-ESPR-compliance disclosure-grade-inventory, 12-signal supplier-financial-health early-warning-radar, 9-condition smart-specimen co-design portal AI-augmented brand-standard, 19-component AI-augmented hidden-cost radar tariff-aware FX-hedging, 7-pillar compounding cost-analysis margin asset) for global brand owners and Q1 2027 controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
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
    update_en_blog([ART228, ART229])
    print("--- Updating blog.html ---")
    update_blog([ART228, ART229])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART228, ART229])
    print("Done.")