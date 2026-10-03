#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 230-AM + 231-PM — 2026-10-03 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-03"

ART230 = {
    "file": "blog-ribbon-oem-b2b-230-module-mill-side-q1-2027-24-stage-hidden-landed-cost-reverse-engineering-19-component-quote-decoder-ai-augmented-hidden-cost-radar-tariff-aware-multi-currency-fx-hedging-architecture-b2b-oem-program-resilience-2026-10-03-am.html",
    "title": "Ribbon OEM B2B 230-Module Mill-Side Q1-2027 24-Stage Hidden-Landed-Cost Reverse-Engineering 19-Component Quote-Decoder AI-Augmented Hidden-Cost Radar Tariff-Aware Multi-Currency FX-Hedging Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 24-Stage Hidden Landed Cost Reverse Engineering Architecture",
    "date": TODAY,
    "desc": "230-module mill-side Q1-2027 24-stage hidden-landed-cost reverse-engineering 19-component quote-decoder AI-augmented hidden-cost radar tariff-aware multi-currency FX-hedging architecture (7-pillar cognitive fabric Yarn-Cost Pass-Through Decoder + Dye-Cost Pass-Through Decoder + Weave-Cost Conversion-Cost Finish-Cost Print-Cost Decoder + Packaging-Cost Cartonization-Cost Lab-Cost R&D-Cost EHS-Cost Sustainability-Cost Decoder + Overhead-Cost Duty-Cost Tariff-Cost Decoder + Freight-Cost Insurance-Cost Demurrage-Cost Customs-Broker-Cost Decoder + FX-Cost Finance-Cost Decoder + Tariff-Aware Multi-Currency FX-Hedging Architecture + Carbon-Adjusted-TCO Decoder + AI-Augmented Hidden-Cost Radar Variable-Cost Modeling Architecture, 9-substrate polyester-satin taffeta organza voile grosgrain velvet jacquard printed baseline, 5-dye-class acid-disperse reactive VAT pigment azo-free OEKO-TEX Standard-100 baseline, 9-substrate 5-dye-class 14-finish-type 9-print-technology baseline, 19-cost component decision point, 9-country 5-FTA 19-FTA-utilization Section-301 EU-CBAM phase-2 baseline, 9-Incoterm-2020 19-country 5-carrier-class baseline, multi-currency forward-contract FX-option natural-hedge architecture, carbon-adjusted-tco Scope-3 LCA cradle-to-gate ESPR DPP CBAM-phase-2 SBTi, AI-augmented hidden-cost radar 19-outlier-cost 14-supplier-bid-spread single-pane executive view) for global brand owners and Q1 2027 controllers. Lift: 38-64% hidden-landed-cost-leakage compression, 4-11% landed-cost savings lift per year, 4-11% program-lifetime-margin-lift.",
}
ART231 = {
    "file": "blog-ribbon-oem-b2b-231-module-mill-side-q1-2027-23-stage-supplier-certification-compliance-decoder-25-credential-roi-tender-bsci-sedex-smeta-oeko-tex-fsc-grs-gots-sbti-cdp-csrd-architecture-b2b-oem-program-resilience-2026-10-03-pm.html",
    "title": "Ribbon OEM B2B 231-Module Mill-Side Q1-2027 23-Stage Supplier-Certification Compliance Decoder 25-Credential ROI Tender-RFP RFI-RFQ BSCI-SEDEX-SMETA OEKO-TEX FSC GRS GOTS SBTi CDP CSRD ESRS-E1 Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 23-Stage Supplier Certification Compliance Decoder Architecture",
    "date": TODAY,
    "desc": "231-module mill-side Q1-2027 23-stage supplier-certification compliance decoder 25-credential ROI tender-RFP RFI-RFQ BSCI-SEDEX-SMETA OEKO-TEX FSC GRS GOTS SBTi CDP CSRD ESRS-E1 architecture (7-pillar cognitive fabric BSCI amfori-BSCI SMETA 4-Pillar SEDEX Social-Audit Decoder + OEKO-TEX Standard-100 OEKO-TEX STeP Sustainability Decoder + FSC Chain-of-Custody GRS Global-Recycled-Standard GOTS Global-Organic-Textile-Standard Sustainability Decoder + ISO-9001 ISO-14001 ISO-45001 Quality-Environmental-OHS Management Decoder + WRAP RBA ICS C2C-Gold ZDHC Higg-FEM Retailer-Tender Decoder + Tender-RFP RFI-RFQ Onboarding Architecture + SBTi CDP CSRD ESRS-E1 ESG-Disclosure-Compliance Decoder + Cross-Border Tariff-Engineering Multi-Country-Manufacturing Diversification Decoder + Supplier-Financial-Health Tier-2 Tier-3 Early-Warning-Radar Architecture + Supplier-Relationship-Management SRM Tiered-QBR-Cadence Vendor-Lifecycle Governance Architecture, 14-station on-site social-compliance audit 18-signal gap-closure plan, 19-substance 14-station on-site chemistry audit 18-signal chem-outlier detection, 19-substrate 5-recycled-content 9-organic-fiber chain-of-custody audit, 14-station 5-process 9-document 18-signal compliance audit, 19-credential 14-station 18-signal compliance gap-closure plan, 24-component compliance-quote-decoder smart-factory capacity-readiness, 19-signal disclosure-grade inventory Scope-3 LCA cradle-to-gate CBAM-Phase-2 DPP-ESPR, Section-301-Era List-4a-4b EU-CBAM Phase-2 ASEAN FTA Cascade compliance-origin, 12-signal working-capital rating-watch telemetry, 22-stage QBR 18-stage JSC 14-stage supplier-incentive alignment) for global brand owners and Q1 2027 controllers. Lift: 38-64% supplier-certification compliance-decoding compression, 4-11% retailer-tender-onboarding pass-rate lift per year, 4-11% program-lifetime-margin-lift.",
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
    update_en_blog([ART230, ART231])
    print("--- Updating blog.html ---")
    update_blog([ART230, ART231])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART230, ART231])
    print("Done.")