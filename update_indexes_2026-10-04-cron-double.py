#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 232-AM + 233-PM — 2026-10-04 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-04"

ART232 = {
    "file": "blog-ribbon-oem-b2b-232-module-mill-side-q1-2027-22-stage-private-label-ribbon-oem-brand-launch-playbook-23-step-concept-to-shelf-speed-to-market-npi-architecture-b2b-oem-program-resilience-2026-10-04-am.html",
    "title": "Ribbon OEM B2B 232-Module Mill-Side Q1-2027 22-Stage Private-Label Ribbon OEM Brand-Launch Playbook 23-Step Concept-to-Shelf Speed-to-Market NPI Architecture for Brand Owners and Retailers",
    "cat": "Q1-2027 22-Stage Private Label Ribbon OEM Brand Launch Playbook Concept To Shelf Speed To Market Npi Architecture",
    "date": TODAY,
    "desc": "232-module mill-side Q1-2027 22-stage private-label ribbon OEM brand-launch playbook 23-step concept-to-shelf speed-to-market NPI architecture (7-pillar cognitive fabric Smart-Specimen Co-Design Portal AI-Visual-Library + AI-Augmented Color-Stewardship Pantone-FHI Translation-Engine + AI-Vision Inline-Defect-Detection Closed-Loop Yield Recovery Pareto-Engine + Cross-Border Tariff-Engineering Country-of-Origin + Hidden-Landed-Cost Reverse-Engineering 19-Component Quote-Decoder + Supplier-Certification-Compliance Decoder + Supplier-Relationship-Management SRM Tiered-QBR-Cadence, brief-to-artwork handoff decoder 9-brief-type 23-artwork-file-type 14-print-technology, artwork-to-color-management handoff decoder Pantone-Coated Uncoated FHI Delta-E<1, color-management-to-print-tooling handoff decoder 14-print-technology 9-finish-type 19-plate-type, print-tooling-to-sampling handoff decoder 19-sample-type 5-sample-round 9-sample-approval-tier, sampling-to-PPAP handoff decoder 23-PPAP-component 14-station on-site AQL-1.0, PPAP-to-shipment handoff decoder 19-Incoterm-2020 9-country 5-carrier-class, shipment-to-shelf handoff decoder 14-distribution-center 9-retail-channel 19-cartonization-spec, smart-specimen co-design portal 9-stage digital-twin brand-standard library, AI-augmented color-stewardship digital-twin Delta-E<1 lot-to-lot continuity, AI-vision inline-defect-detection 25-stage AOI auto-reject edge-AI Jetson-AGX-Orin) for global brand owners and Q1 2027 controllers. Lift: 38-64% time-to-shelf compression, 4-11% speed-to-market lift per launch, 4-11% program-lifetime-margin-lift.",
}
ART233 = {
    "file": "blog-ribbon-oem-b2b-233-module-mill-side-q1-2027-24-stage-oem-cost-analysis-supplier-selection-25-signal-12-kpi-framework-architecture-b2b-oem-program-resilience-2026-10-04-pm.html",
    "title": "Ribbon OEM B2B 233-Module Mill-Side Q1-2027 24-Stage OEM Cost-Analysis Supplier-Selection 25-Signal 12-KPI Framework Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 24-Stage OEM Cost Analysis Supplier Selection 25 Signal 12 KPI Framework Architecture",
    "date": TODAY,
    "desc": "233-module mill-side Q1-2027 24-stage OEM cost-analysis supplier-selection 25-signal 12-KPI framework architecture (7-pillar cognitive fabric Should-Cost Quote-Decoder + Hidden-Cost Radar Variable-Cost Modeling + Supplier-Selection Framework 12-KPI + Supplier-Certification-Compliance Decoder + Cross-Border Tariff-Engineering Multi-Country-Manufacturing + Carbon-Adjusted-TCO Overlay + Supplier-Risk-Tiering Multi-Source, 23-component should-cost quote-decoder yarn-dye-weave-finish-conversion-overhead-tariff-freight-FX-insurance-demurrage-broker-finance-carbon-R&D-EHS-lab-carton-packaging-printing-sustainability-duty, 9-substrate polyester-satin taffeta organza voile grosgrain velvet jacquard printed yarn baseline, 5-dye-class acid-disperse reactive VAT pigment azo-free OEKO-TEX Standard-100 baseline, 9-substrate 14-finish-type 5-conversion-type weave-finish-conversion baseline, supplier-selection 25-signal 12-KPI capacity OEE productivity AQL-1.0 scorecard, 24-credential supplier-certification-compliance decoder BSCI SEDEX SMETA OEKO-TEX FSC GRS GOTS tender-RFP RFI-RFQ onboarding, 24-component cross-border tariff-engineering Section-301 list-4a/4b EU-CBAM phase-2 ASEAN FTA cascade, Scope-3 LCA cradle-to-gate ESPR DPP CBAM-phase-2 SBTi CSRD ESRS-E1 carbon-adjusted-TCO overlay, FX-hedging forward-NDF-knock-out 6-currency carbon-adjusted-TCO natural-hedge, supplier-risk-tiering multi-source Tier-1 Tier-2 Tier-3 bridge-order migration 9-multi-country-diversification, AI-augmented hidden-cost radar 19-component AI-augmented bid-comparator 14-supplier-bid-spread) for global brand owners and Q1 2027 controllers. Lift: 38-64% should-cost quote-decoder compression, 4-11% landed-cost savings lift per year, 4-11% program-lifetime-margin-lift.",
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
    update_en_blog([ART232, ART233])
    print("--- Updating blog.html ---")
    update_blog([ART232, ART233])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART232, ART233])
    print("Done.")
