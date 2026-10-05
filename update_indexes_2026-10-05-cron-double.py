#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 234-AM + 235-PM — 2026-10-05 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-05"

ART234 = {
    "file": "blog-ribbon-oem-b2b-234-module-mill-side-q1-2027-23-stage-custom-branded-ribbon-oem-concept-to-label-brand-launch-custom-packaging-specification-engineering-19-layer-bill-of-materials-architecture-b2b-oem-program-resilience-2026-10-05-am.html",
    "title": "Ribbon OEM B2B 234-Module Mill-Side Q1-2027 23-Stage Custom-Branded Ribbon OEM Concept-to-Label Brand-Launch Custom-Packaging Specification-Engineering 19-Layer Bill-of-Materials Architecture for Brand Owners and Retailers",
    "cat": "Q1-2027 23-Stage Custom Branded Ribbon OEM Concept To Label Brand Launch Custom Packaging Specification Engineering 19 Layer Bill Of Materials Architecture",
    "date": TODAY,
    "desc": "234-module mill-side Q1-2027 23-stage custom-branded ribbon OEM concept-to-label brand-launch custom-packaging specification-engineering 19-layer bill-of-materials architecture (7-pillar cognitive fabric Smart-Specimen Co-Design Portal AI-Visual-Library + AI-Augmented Color-Stewardship Pantone-FHI Translation-Engine + AI-Vision Inline-Defect-Detection Closed-Loop Yield Recovery Pareto-Engine + Cross-Border Tariff-Engineering Country-of-Origin + Hidden-Landed-Cost Reverse-Engineering 19-Component Quote-Decoder + Supplier-Certification-Compliance Decoder + Supplier-Relationship-Management SRM Tiered-QBR-Cadence, brief-to-brand-identity handoff decoder 9-brand-identity-type 23-artwork-file-type 14-print-technology, brand-identity-to-artwork handoff decoder Pantone-Coated Uncoated FHI Delta-E<1, artwork-to-spec handoff decoder 19-layer bill-of-materials 14-finish-type 9-plate-type, spec-to-print-tooling handoff decoder 14-print-technology 5-sample-round 9-sample-approval-tier, print-tooling-to-color handoff decoder Pantone-Coated Uncoated FHI Delta-E<1 14-station on-site, color-to-finish handoff decoder 19-Incoterm-2020 9-country 5-carrier-class, finish-to-sampling handoff decoder 14-distribution-center 9-retail-channel 19-cartonization-spec, smart-specimen co-design portal 9-stage digital-twin brand-standard library, AI-augmented color-stewardship digital-twin Delta-E<1 lot-to-lot continuity, AI-vision inline-defect-detection 25-stage AOI auto-reject edge-AI Jetson-AGX-Orin) for global brand owners and Q1 2027 controllers. Lift: 38-64% time-to-shelf compression, 4-11% speed-to-market lift per launch, 4-11% program-lifetime-margin-lift.",
}
ART235 = {
    "file": "blog-ribbon-oem-b2b-235-module-mill-side-q1-2027-24-stage-ribbon-oem-sustainability-compliance-decoder-esg-lca-scope-3-cradle-to-gate-disclosure-grade-architecture-b2b-oem-program-resilience-2026-10-05-pm.html",
    "title": "Ribbon OEM B2B 235-Module Mill-Side Q1-2027 24-Stage Ribbon OEM Sustainability Compliance Decoder ESG-LCA Scope-3 Cradle-to-Gate Disclosure-Grade Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 24-Stage Ribbon OEM Sustainability Compliance Decoder ESG LCA Scope 3 Cradle To Gate Disclosure Grade Architecture",
    "date": TODAY,
    "desc": "235-module mill-side Q1-2027 24-stage ribbon OEM sustainability compliance decoder ESG-LCA Scope-3 cradle-to-gate disclosure-grade architecture (7-pillar cognitive fabric Scope-3 LCA Cradle-to-Gate Plane + ESG Scorecard 19-Signal Decoder + GRS-RPET-FSC-GOTS Claim-Substantiation + ESPR Digital Product Passport Plane + CBAM Phase-2 Carbon-Adjusted-TCO + SBTi Aligned Target Validation + CSRD-ESRS-E1 Alignment, 24-component Scope-3 cradle-to-gate LCA decoder cradle-to-gate Gate-to-Grave boundary-setting allocation-method disaggregation, 9-substrate polyester-satin taffeta organza voile grosgrain velvet jacquard printed cradle-to-gate boundary-setting baseline, 5-allocation-method mass-based economic-based energy-based cradle-to-gate ISO-14064 baseline, 14-photo-evidence retrofit stack Smart-Mill IIoT Edge-AI energy-water-carbon-productivity, ESG scorecard 19-signal decoder carbon water waste Higg-FEM ZDHC CDP SBTi CSRD-ESRS-HR labor-member-privacy, 19-credential GRS RPET FSC GOTS OEKO-TEX cradle-to-gate claim tender-RFP RFI-RFQ onboarding, 24-Component ESPR Digital Product Passport DPP EU-2030 DPP-Readiness multi-country-manufacturing, 24-Component CBAM Phase-2 carbon-adjusted-TCO multi-country-manufacturing, 24-Component SBTi-aligned SBTi-validated Scope-3 decarbonization, 24-Component CSRD-ESRS-E1 disclosure-grade multi-country, supplier-relationship-management SRM tiered-QBR-cadence vendor-lifecycle ESG-governance) for global brand owners and Q1 2027 controllers. Lift: 38-64% scope-3 cradle-to-gate LCA compression, 4-11% disclosure-grade pass-rate lift per year, 4-11% program-lifetime-margin-lift.",
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
    update_en_blog([ART234, ART235])
    print("--- Updating blog.html ---")
    update_blog([ART234, ART235])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART234, ART235])
    print("Done.")