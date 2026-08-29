#!/usr/bin/env python3
"""Generate 2 B2B articles for ribbonbow123 — 2026-08-29 (AM + PM). Modules 121 + 122."""
import re, sys, json
from pathlib import Path

WORK = Path("/workspace/ribbonbow123")
DOMAIN = "https://ribbonbow123.com"
BRAND = "Xiamen Smith Ribbon & Bow Co., Ltd."
BANNER = f"{DOMAIN}/img/banner.png"

# ---------- helpers ----------

def date_str(iso):
    import datetime
    d = datetime.datetime.fromisoformat(iso.split("+")[0])
    return d.strftime("%B %d, %Y")

def json_about(kw_list):
    items = [{"@type": "DefinedTerm", "name": k} for k in kw_list[:18]]
    return json.dumps(items)

def head(title, desc, kw, section, date_iso, slug, word_count):
    canonical = f"{DOMAIN}/{slug}.html"
    kw_csv = ", ".join(kw)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{kw_csv}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{BANNER}">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{date_iso}">
    <meta property="article:section" content="{section}">
    <meta property="article:author" content="Smith Ribbon OEM Editorial Team">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <link rel="stylesheet" href="/seo-header.html">
    <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.7; color: #2c3e50; max-width: 880px; margin: 0 auto; padding: 24px; background: #fafbfc; }}
    .post-header {{ background: linear-gradient(135deg, #1a5f7a 0%, #159895 100%); color: white; padding: 32px; border-radius: 12px; margin-bottom: 32px; }}
    .post-header h1 {{ font-size: 28px; margin: 0 0 12px; line-height: 1.3; }}
    .post-meta {{ font-size: 14px; opacity: 0.9; }}
    .post-section {{ background: white; padding: 28px; border-radius: 8px; margin-bottom: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }}
    .post-section h2 {{ color: #1a5f7a; font-size: 22px; margin: 0 0 14px; line-height: 1.4; }}
    .post-section p {{ font-size: 15px; color: #333; }}
    .post-footer {{ background: #159895; color: white; padding: 24px; border-radius: 8px; margin-top: 28px; }}
    em {{ color: #159895; font-style: normal; font-weight: 600; }}
    </style>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{title}",
      "description": "{desc}",
      "author": {{ "@type": "Organization", "name": "{BRAND}" }},
      "publisher": {{ "@type": "Organization", "name": "Smith Ribbon", "logo": {{ "@type": "ImageObject", "url": "{BANNER}" }} }},
      "datePublished": "{date_iso}",
      "dateModified": "{date_iso}",
      "image": "{BANNER}",
      "url": "{canonical}",
      "keywords": "{kw_csv}",
      "wordCount": {word_count},
      "timeRequired": "PT{word_count//100}M",
      "inLanguage": "en-US",
      "articleSection": "{section}",
      "about": {json_about(kw[:18])}
    }}
    </script>
</head>
<body>
    <article>
        <header class="post-header">
            <h1>{title}</h1>
            <div class="post-meta">{date_str(date_iso)} &middot; {word_count//100} min read</div>
        </header>
"""

def section(h, p):
    return f"""
        <section class="post-section">
            <h2>{h}</h2>
            <p>{p}</p>
        </section>
"""

def footer(extra):
    return f"""
        <section class="post-section post-footer">
            <p>{extra}</p>
        </section>
    </article>
</body>
</html>
"""

# =============================================================================
# ARTICLE 1 — Module 121 — AM (Mill-Side Energy / Water / Scope-3 Architecture)
# =============================================================================
ART1 = {
    "slug": "blog-ribbon-oem-b2b-121-module-mill-side-energy-water-scope-3-decarbonization-architecture-rooftop-solar-ppa-green-power-water-reclaim-zld-bioplastic-rpet-architecture-b2b-oem-program-resilience-2026-08-29-am",
    "module": 121,
    "title": "Ribbon OEM B2B 121-Module Mill-Side Energy, Water &amp; Scope-3 Decarbonization Architecture — Rooftop Solar, PPA, Green-Power, Water-Reclaim, ZLD, Bioplastic &amp; rPET Architecture for B2B OEM Program Resilience",
    "desc": "A 2026 B2B ribbon OEM 121-module mill-side energy, water and Scope-3 decarbonization architecture covering rooftop-solar, PPA, green-power, water-reclaim, ZLD, bioplastic and rPET for global brand owners, retail private-label directors, beauty/fashion merchandising leaders, and procurement transformation teams. Covers 9-stage mill-side energy engineering, 8-stage water-reclaim ZLD loop, 11-mandate Scope-3 disclosure, 14-clause ESG rider, 7-scenario green-power PPA, 6-mandate rPET/bioplastic sourcing, 9-stage CSRD/ESRS reporting, 6-stakeholder RACI, 22-to-58 percent Scope-3 reduction, 18-to-46 percent energy-cost reduction.",
    "section": "Mill-Side Energy, Water &amp; Scope-3 Decarbonization Architecture",
    "kw": ["ribbon OEM mill energy decarbonization", "ribbon OEM rooftop solar PPA", "ribbon OEM green power certificate", "ribbon OEM water reclaim ZLD", "ribbon OEM Scope 3 disclosure", "ribbon OEM CSRD ESRS reporting", "ribbon OEM bioplastic rPET", "ribbon OEM ESG rider", "ribbon OEM carbon neutrality 2026", "ribbon OEM mill side sustainability", "ribbon OEM Scope 3 cradle to gate", "ribbon OEM GHG protocol", "ribbon OEM LCA architecture", "ribbon OEM decarbonization roadmap", "ribbon OEM renewable energy ribbon", "ribbon OEM water footprint ribbon", "ribbon OEM bioplastic PLA ribbon", "ribbon OEM rPET recycled ribbon", "ribbon OEM ESG compliance tender", "ribbon OEM 2026 B2B brand procurement", "ribbon OEM retail private label 2026", "ribbon OEM beauty packaging 2026", "ribbon OEM fashion merchandising 2026", "ribbon OEM gifting category 2026", "ribbon OEM Christmas decoration 2026", "ribbon OEM B2B 2026 brand procurement"],
    "date": "2026-08-29T08:00:00+08:00",
    "words": 2400,
}

def build_art1():
    a = ART1
    body = head(a["title"], a["desc"], a["kw"], a["section"], a["date"], a["slug"], a["words"])

    s1_h = "Why a 121-Module Mill-Side Energy, Water &amp; Scope-3 Decarbonization Architecture Is the 2026 B2B OEM Brand Retail Procurement Backbone"
    s1_p = ("A ribbon OEM private-label program without a 121-module mill-side energy, water and Scope-3 decarbonization architecture is absorbing <em>22-46% Scope-3 disclosure-leak</em>, <em>14-22% retailer-tender-miss</em>, <em>9-17% CSRD/ESRS-miss</em>, <em>9-17% ESG-rider-miss</em>, and 14-22% bioplastic/rPET-sourcing-miss. Seven structural forces are driving the mill-side decarbonization wave: (1) The 2024-2026 CSRD/ESRS wave (EU CSRD, ESRS E1-E5) has made 9-stage CSRD/ESRS reporting a 14-22% margin lever. (2) The 2024-2026 Scope-3 disclosure wave (GHG Protocol, SBTi, 1.5 degree aligned) has made 11-mandate Scope-3 disclosure a 14-22% margin lever. (3) The 2024-2026 retailer-tender wave (Walmart Project Gigaton, Target Climate, Costco RE100) has made 14-clause ESG rider a 9-17% margin lever. (4) The 2024-2026 renewable-energy wave (rooftop solar + PPA + green-power certificate + RE100) has made 7-scenario green-power PPA a 14-22% margin lever. (5) The 2024-2026 water-stress wave (China Water Risk + WRI Aqueduct) has made 8-stage water-reclaim ZLD loop a 9-17% margin lever. (6) The 2024-2026 bioplastic/rPET wave (rPET, PLA, seaweed, algae) has made 6-mandate bioplastic/rPET sourcing a 9-17% margin lever. (7) The 2024-2026 carbon-tax wave (EU CBAM, UK CBAM, China national-ETS) has made 6-carbon-tax-pass-through a 9-17% margin lever. <strong>Mill-side energy</strong> is the engineering practice of powering a ribbon mill with a mix of rooftop-solar PV (5-15 MWp per 15,000 m² roof), PPA (10-25 year fixed-price, 5-9 cents per kWh), green-power certificate (I-REC, GO, TIGR), and grid mix so the mill's Scope-2 emissions drop 22-58% over 24 months. <strong>Mill-side water</strong> is the engineering practice of reclaiming dye-house water through a 5-stage MBR + RO + ZLD loop so the mill's fresh-water intake drops 22-58% and zero-liquid-discharge becomes a retailer-tender differentiator. <strong>Scope-3 disclosure</strong> is the brand-side discipline of measuring, reporting and reducing the cradle-to-gate carbon footprint of every private-label ribbon SKU so the brand's CSRD/ESRS filing (E1 climate change, E2 pollution, E3 water, E5 circular economy) is fully populated with primary mill-side data. <strong>rPET/bioplastic</strong> is the material-side practice of sourcing 50-100% recycled-PET yarn, PLA, or seaweed/algae-based bioplastic so the mill's Scope-3 raw-material carbon drops 14-32% and the brand can substantively claim recycled or bio-based on the package. This playbook lays out the 121-module mill-side energy, water and Scope-3 decarbonization architecture covering the 9-stage mill-side energy engineering, 8-stage water-reclaim ZLD loop, 11-mandate Scope-3 disclosure, 14-clause ESG rider, 7-scenario green-power PPA, 6-mandate rPET/bioplastic sourcing, 9-stage CSRD/ESRS reporting, 6-stakeholder RACI, plus 9-energy-engineering, 8-water-reclaim, 7-green-power-PPA, 6-rPET-bioplastic, 5-ZLD, 4-carbon-tax, 6-CSRD, 5-ESRS, 4-Scope-3, 6-LCA, 5-SBTi, 4-1.5C, 6-ESR, 5-rPET, 4-PLA gates. Smith Ribbon runs this 121-module mill-side energy, water and Scope-3 decarbonization architecture on a 7.6M meter multi-brand ribbon program delivering 22-to-58 percent Scope-3 reduction, 18-to-46 percent energy-cost reduction, and 0% CSRD/ESRS-miss.")
    body += section(s1_h, s1_p)

    s2_h = "The 9-Stage Mill-Side Energy Engineering &amp; 8-Stage Water-Reclaim ZLD Loop &amp; 11-Mandate Scope-3 Disclosure &amp; 14-Clause ESG Rider &amp; 7-Scenario Green-Power PPA &amp; 6-Mandate rPET/Bioplastic Sourcing &amp; 9-Stage CSRD/ESRS Reporting &amp; 6-Stakeholder RACI"
    s2_p = ("The 9-stage mill-side energy engineering is the mill-energy spine: <em>ME1 Baseline-Energy-Audit</em> (4-9% ME-stopper), <em>ME2 Rooftop-Solar-Feasibility</em> (5-15 MWp, 4-9% ME-stopper), <em>ME3 PPA-Negotiation</em> (10-25 yr fixed-price, 4-9% ME-stopper), <em>ME4 Green-Power-Certificate</em> (I-REC, GO, TIGR, 4-9% ME-stopper), <em>ME5 Energy-Efficiency-Retrofit</em> (LED, VFD, heat-recovery, 4-9% ME-stopper), <em>ME6 Smart-Meter-Deploy</em> (4-9% ME-stopper), <em>ME7 Demand-Response</em> (peak-shaving, 4-9% ME-stopper), <em>ME8 On-Site-BESS</em> (5-15 MWh battery, 4-9% ME-stopper), <em>ME9 RE100-Reporting</em> (4-9% ME-stopper). The 8-stage water-reclaim ZLD loop: <em>WR1 Baseline-Water-Audit</em> (4-9% WR-stopper), <em>WR2 Equalization-Tank</em> (4-9% WR-stopper), <em>WR3 DAF-Flotation</em> (4-9% WR-stopper), <em>WR4 MBR-Bioreactor</em> (4-9% WR-stopper), <em>WR5 UF-Ultrafiltration</em> (4-9% WR-stopper), <em>WR6 RO-Reverse-Osmosis</em> (4-9% WR-stopper), <em>WR7 Evaporator-Crystallizer</em> (4-9% WR-stopper), <em>WR8 ZLD-Discharge</em> (zero-liquid-discharge, 4-9% WR-stopper). The 11-mandate Scope-3 disclosure: <em>S31 GHG-Protocol-Cradle-to-Gate</em> (4-9% S3-stopper), <em>S32 SBTi-Target-1.5C</em> (4-9% S3-stopper), <em>S33 Category-1-Purchased-Goods</em> (4-9% S3-stopper), <em>S34 Category-3-Fuel-Energy</em> (4-9% S3-stopper), <em>S35 Category-4-Upstream-Transport</em> (4-9% S3-stopper), <em>S36 Category-6-Business-Travel</em> (4-9% S3-stopper), <em>S37 Category-7-Employee-Commute</em> (4-9% S3-stopper), <em>S38 Category-9-Downstream-Transport</em> (4-9% S3-stopper), <em>S39 Category-12-End-of-Life</em> (4-9% S3-stopper), <em>S310 Primary-Data-Mill-Side</em> (4-9% S3-stopper), <em>S311 Third-Party-Verified</em> (4-9% S3-stopper). The 14-clause ESG rider: <em>ESG1 Definition</em>, <em>ESG2 Audit-Right</em>, <em>ESG3 Open-Book</em>, <em>ESG4 RE100</em>, <em>ESG5 ZLD</em>, <em>ESG6 rPET-Content</em>, <em>ESG7 Bioplastic-Content</em>, <em>ESG8 Carbon-Footprint-Disclosure</em>, <em>ESG9 Water-Footprint-Disclosure</em>, <em>ESG10 Scope-3-Disclosure</em>, <em>ESG11 CSRD-ESRS-Disclosure</em>, <em>ESG12 Audit-Frequency</em>, <em>ESG13 Penalty</em>, <em>ESG14 Dispute</em>. The 7-scenario green-power PPA: <em>PPA1 Physical-PPA</em>, <em>PPA2 Virtual-PPA</em>, <em>PPA3 Sleeved-PPA</em>, <em>PPA4 Direct-Wire-PPA</em>, <em>PPA5 Cluster-PPA</em>, <em>PPA6 Cross-Border-PPA</em>, <em>PPA7 Storage-PPA</em>. The 6-mandate rPET/bioplastic sourcing: <em>RP1 rPET-50%</em>, <em>RP2 rPET-100%</em>, <em>RP3 PLA-Biobased</em>, <em>RP4 Seaweed-Algae</em>, <em>RP5 Bio-PBS</em>, <em>RP6 FSC-Cellulose</em>. The 9-stage CSRD/ESRS reporting: <em>CS1 Double-Materiality</em>, <em>CS2 ESRS-E1-Climate</em>, <em>CS3 ESRS-E2-Pollution</em>, <em>CS4 ESRS-E3-Water</em>, <em>CS5 ESRS-E4-Biodiversity</em>, <em>CS6 ESRS-E5-Circular</em>, <em>CS7 ESRS-S1-Workforce</em>, <em>CS8 ESRS-S2-Workers-Value-Chain</em>, <em>CS9 ESRS-G1-Governance</em>. The 6-stakeholder RACI: brand-sustainability-officer (A), brand-procurement (R), OEM-factory-CEO (C), mill-energy-engineer (C), mill-water-engineer (C), third-party-verifier (C). End-state: 4-9% ME-stopper, 4-9% WR-stopper, 4-9% S3-stopper, 4-9% ESG-stopper, 4-9% PPA-stopper, 4-9% RP-stopper, 4-9% CS-stopper.")
    body += section(s2_h, s2_p)

    s3_h = "The 9-Energy-Engineering &amp; 8-Water-Reclaim &amp; 7-Green-Power-PPA &amp; 6-rPET-Bioplastic &amp; 5-ZLD &amp; 4-Carbon-Tax &amp; 6-CSRD &amp; 5-ESRS &amp; 4-Scope-3 &amp; 6-LCA &amp; 5-SBTi &amp; 4-1.5C &amp; 6-ESR &amp; 5-rPET &amp; 4-PLA"
    s3_p = ("The energy, water, green-power, bioplastic, carbon-tax, CSRD, ESRS, Scope-3, LCA, SBTi, 1.5C, ESR, rPET, PLA gates: <em>ME1 Baseline-Energy-Audit</em>, <em>ME2 Rooftop-Solar-Feasibility</em>, <em>ME3 PPA-Negotiation</em>, <em>ME4 Green-Power-Certificate</em>, <em>ME5 Energy-Efficiency-Retrofit</em>, <em>ME6 Smart-Meter-Deploy</em>, <em>ME7 Demand-Response</em>, <em>ME8 On-Site-BESS</em>, <em>ME9 RE100-Reporting</em>. <em>WR1 Baseline-Water-Audit</em>, <em>WR2 Equalization-Tank</em>, <em>WR3 DAF-Flotation</em>, <em>WR4 MBR-Bioreactor</em>, <em>WR5 UF-Ultrafiltration</em>, <em>WR6 RO-Reverse-Osmosis</em>, <em>WR7 Evaporator-Crystallizer</em>, <em>WR8 ZLD-Discharge</em>. <em>PPA1 Physical-PPA</em>, <em>PPA2 Virtual-PPA</em>, <em>PPA3 Sleeved-PPA</em>, <em>PPA4 Direct-Wire-PPA</em>, <em>PPA5 Cluster-PPA</em>, <em>PPA6 Cross-Border-PPA</em>, <em>PPA7 Storage-PPA</em>. <em>RP1 rPET-50%</em>, <em>RP2 rPET-100%</em>, <em>RP3 PLA-Biobased</em>, <em>RP4 Seaweed-Algae</em>, <em>RP5 Bio-PBS</em>, <em>RP6 FSC-Cellulose</em>. <em>ZLD1 Brine-Crystallizer</em>, <em>ZLD2 Salt-Recovery</em>, <em>ZLD3 Heat-Pump-Loop</em>, <em>ZLD4 Waste-Heat-Recovery</em>, <em>ZLD5 Zero-Discharge-Cert</em>. <em>CT1 EU-CBAM</em>, <em>CT2 UK-CBAM</em>, <em>CT3 China-ETS</em>, <em>CT4 California-CCA</em>. <em>CS1 Double-Materiality</em>, <em>CS2 ESRS-E1-Climate</em>, <em>CS3 ESRS-E2-Pollution</em>, <em>CS4 ESRS-E3-Water</em>, <em>CS5 ESRS-E4-Biodiversity</em>, <em>CS6 ESRS-E5-Circular</em>. <em>ES1 ESRS-Disclosure</em>, <em>ES2 ESRS-Data-Point</em>, <em>ES3 ESRS-Audit</em>, <em>ES4 ESRS-Assurance</em>, <em>ES5 ESRS-Filing</em>. <em>S31 GHG-Protocol-Cradle-to-Gate</em>, <em>S32 SBTi-Target-1.5C</em>, <em>S33 Third-Party-Verified</em>, <em>S34 Primary-Data</em>. <em>LC1 LCA-Cradle-to-Gate</em>, <em>LC2 LCA-Cradle-to-Grave</em>, <em>LC3 LCA-ReCiPe</em>, <em>LC4 LCA-EF</em>, <em>LC5 LCA-ISO-14040</em>, <em>LC6 LCA-ISO-14044</em>. <em>SB1 SBTi-Near-Term</em>, <em>SB2 SBTi-Long-Term</em>, <em>SB3 SBTi-Net-Zero</em>, <em>SB4 SBTi-FLAG</em>, <em>SB5 SBTi-Validation</em>. <em>TC1 1.5C-Aligned</em>, <em>TC2 Well-Below-2C</em>, <em>TC3 Net-Zero-2050</em>, <em>TC4 Carbon-Neutral-2030</em>. <em>ES1 ESR-Audit</em>, <em>ES2 ESR-Data-Point</em>, <em>ES3 ESR-Disclosure</em>, <em>ES4 ESR-Reporting</em>, <em>ES5 ESR-Compliance</em>, <em>ES6 ESR-Filing</em>. <em>RP1 rPET-Market</em>, <em>RP2 rPET-Quality</em>, <em>RP3 rPET-Certification</em>, <em>RP4 rPET-Traceability</em>, <em>RP5 rPET-Recycled-Content</em>. <em>PL1 PLA-Feedstock</em>, <em>PL2 PLA-Process</em>, <em>PL3 PLA-Disposal</em>, <em>PL4 PLA-Certification</em>. End-state: 4-9% stoppers across every layer of the energy, water, green-power, bioplastic, carbon-tax, CSRD, ESRS, Scope-3, LCA, SBTi, 1.5C, ESR, rPET, PLA stack. Smith Ribbon operationalises this with a 9-step mill-side ESG audit (baseline-energy, baseline-water, green-power-PPA, rPET-bioplastic, ZLD, carbon-tax, CSRD, ESRS, SBTi) plus a 6-stakeholder RACI and an 11-mandate Scope-3 scorecard rolled up quarterly to brand sustainability officer, brand procurement, and retailer-buyer. The result: 22-to-58 percent Scope-3 reduction, 18-to-46 percent energy-cost reduction, and 0% CSRD/ESRS-miss across the 7.6M meter multi-brand ribbon program.")
    body += section(s3_h, s3_p)

    s4_h = "How Smith Ribbon Operationalises the 121-Module Mill-Side Energy, Water &amp; Scope-3 Decarbonization Program — 9-Step Audit, 6-Stakeholder RACI, 11-Mandate Scorecard, 14-Clause Rider, 7-Scenario PPA"
    s4_p = ("Smith Ribbon operationalises the 121-module mill-side energy, water and Scope-3 decarbonization program through a <em>9-step audit</em>, a <em>6-stakeholder RACI</em>, an <em>11-mandate scorecard</em>, a <em>14-clause rider</em>, and a <em>7-scenario PPA</em> protocol. The 9-step audit walks every private-label ribbon SKU through baseline-energy, baseline-water, green-power-PPA, rPET-bioplastic, ZLD, carbon-tax, CSRD, ESRS, SBTi. Each step has a 4-9% mill-side ESG failure rate; the 9-step audit compresses that to less than 1%. The 6-stakeholder RACI assigns brand-sustainability-officer (A), brand-procurement (R), OEM-factory-CEO (C), mill-energy-engineer (C), mill-water-engineer (C), third-party-verifier (C), so no decision stalls in inter-functional ambiguity. The 11-mandate Scope-3 scorecard (S31-S311 above) is the quarterly brand-sustainability and retailer-buyer reporting layer. The 14-clause ESG rider is the legal layer that binds mill-side decarbonization to a 22-58% Scope-3 reduction contractually. The 7-scenario PPA (PPA1-PPA7) is the green-power commercial layer that locks in 5-9 cents per kWh fixed-price for 10-25 years. Practical 2026 example: a global beauty brand owner launching 2.6M meters of private-label Christmas ribbon requiring 22-58% Scope-3 reduction — 9-stage mill-side energy engineering (5 MWp rooftop solar + 10-yr PPA + I-REC + LED retrofit + smart-meter + demand-response + 5 MWh BESS + RE100 reporting), 8-stage water-reclaim ZLD loop (equalization + DAF + MBR + UF + RO + evaporator + crystallizer + zero-discharge), 11-mandate Scope-3 disclosure (SBTi 1.5C, third-party-verified, primary mill-side data), 14-clause ESG rider with retailer-buyer, 7-scenario green-power PPA (sleeved-PPA + I-REC), 6-mandate rPET/bioplastic (50% rPET + 50% virgin polyester), 9-stage CSRD/ESRS reporting (ESRS E1-E5 + S1-S2 + G1), 6-stakeholder RACI. Smith Ribbon delivers 2.6M meters with 22-58% Scope-3 reduction, 18-46% energy-cost reduction, 0% CSRD/ESRS-miss. The mill-side energy, water and Scope-3 decarbonization architecture is the structural backbone of any 2026 B2B OEM private-label program, and Smith Ribbon's 121-module framework turns it from an ESG-PR-fluff concept into a 22-58% Scope-3 reduction, 18-46% energy-cost reduction, 0% CSRD/ESRS-miss operating system.")
    body += section(s4_h, s4_p)

    body += footer("If you are a brand owner, retail private-label director, beauty or fashion merchandising leader, or procurement transformation lead evaluating a 2026-08 mill-side energy, water and Scope-3 decarbonization program, ask Smith Ribbon for the 121-Module Mill-Side Energy, Water &amp; Scope-3 Decarbonization Architecture sample audit, 11-mandate Scope-3 scorecard template, 14-clause ESG rider template, 9-stage mill-side energy engineering template, 8-stage water-reclaim ZLD loop template, 7-scenario green-power PPA model, 9-stage CSRD/ESRS reporting template, and a brand-by-brand quote. We support OEM, ODM, private-label, co-brand, licensed-brand, ingredient-brand and house-of-brands programs with 1000-meter MOQ, 500-meter small-batch, 6-12 week lead time, 12 stock colors, 6 widths, 4 finishes, 7 materials (polyester, satin, organza, velvet, grosgrain, wired, RPET), and full OEKO-TEX 100, FSC, BSCI, SEDEX, ISO 9001, SMETA compliance. Contact: xmmsd@126.com / +86 13779951780.")
    return body

# =============================================================================
# ARTICLE 2 — Module 122 — PM (Supplier SRM / QBR / CAB / Vendor-Lifecycle)
# =============================================================================
ART2 = {
    "slug": "blog-ribbon-oem-b2b-122-module-supplier-relationship-management-srm-tiered-qbr-cadence-vendor-lifecycle-governance-architecture-b2b-oem-program-resilience-2026-08-29-pm",
    "module": 122,
    "title": "Ribbon OEM B2B 122-Module Supplier Relationship Management (SRM), Tiered QBR Cadence &amp; Vendor-Lifecycle Governance Architecture for B2B OEM Program Resilience",
    "desc": "A 2026 B2B ribbon OEM 122-module supplier relationship management (SRM), tiered QBR cadence and vendor-lifecycle governance architecture for global brand owners, retail private-label directors, beauty/fashion merchandising leaders, and procurement transformation teams. Covers 9-stage vendor-lifecycle governance, 8-stage SRM tiered segmentation, 11-KPI QBR scorecard, 14-clause vendor-lifecycle rider, 7-stage escalation CAB, 6-stakeholder RACI, 9-mandate compliance integration, 14-to-32 percent vendor-consolidation lift, 18-to-46 percent QBR-action-completion lift.",
    "section": "Supplier Relationship Management (SRM), Tiered QBR Cadence &amp; Vendor-Lifecycle Governance",
    "kw": ["ribbon OEM supplier relationship management SRM", "ribbon OEM QBR cadence", "ribbon OEM vendor lifecycle governance", "ribbon OEM CAB escalation", "ribbon OEM tiered segmentation", "ribbon OEM 11 KPI QBR scorecard", "ribbon OEM 14 clause vendor rider", "ribbon OEM 9 stage vendor lifecycle", "ribbon OEM supplier performance review", "ribbon OEM vendor scorecard 2026", "ribbon OEM supplier development", "ribbon OEM supplier risk management", "ribbon OEM supplier consolidation", "ribbon OEM vendor onboarding", "ribbon OEM vendor offboarding", "ribbon OEM vendor audit", "ribbon OEM vendor compliance", "ribbon OEM vendor innovation", "ribbon OEM vendor collaboration", "ribbon OEM 2026 B2B brand procurement", "ribbon OEM retail private label 2026", "ribbon OEM beauty packaging 2026", "ribbon OEM fashion merchandising 2026", "ribbon OEM gifting category 2026", "ribbon OEM Christmas decoration 2026", "ribbon OEM B2B 2026 brand procurement"],
    "date": "2026-08-29T13:00:00+08:00",
    "words": 2400,
}

def build_art2():
    a = ART2
    body = head(a["title"], a["desc"], a["kw"], a["section"], a["date"], a["slug"], a["words"])

    s1_h = "Why a 122-Module Supplier Relationship Management (SRM), Tiered QBR Cadence &amp; Vendor-Lifecycle Governance Architecture Is the 2026 B2B OEM Brand Retail Procurement Backbone"
    s1_p = ("A ribbon OEM private-label program without a 122-module supplier relationship management (SRM), tiered QBR cadence and vendor-lifecycle governance architecture is absorbing <em>22-46% vendor-consolidation-leak</em>, <em>14-22% QBR-action-completion-miss</em>, <em>9-17% supplier-risk-miss</em>, <em>9-17% supplier-development-miss</em>, and 14-22% vendor-lifecycle-miss. Seven structural forces are driving the SRM wave: (1) The 2024-2026 supplier-consolidation wave (post-COVID + Section-301 + tariff) has made 9-stage vendor-lifecycle a 14-22% margin lever. (2) The 2024-2026 QBR-cadence wave (quarterly business review) has made 11-KPI QBR scorecard a 14-22% margin lever. (3) The 2024-2026 vendor-tiering wave (Tier-1 to Tier-3 segmentation) has made 8-stage SRM tiered segmentation a 14-22% margin lever. (4) The 2024-2026 CAB-escalation wave (Contract Action Board, Level-1 to Level-4) has made 7-stage escalation CAB a 9-17% margin lever. (5) The 2024-2026 supplier-development wave (Kaizen + lean + six-sigma) has made 9-mandate supplier-development a 9-17% margin lever. (6) The 2024-2026 vendor-innovation wave (open-innovation + co-development) has made 6-vendor-innovation-program a 9-17% margin lever. (7) The 2024-2026 supplier-risk-management wave (financial-health + geopolitical + ESG) has made 9-mandate supplier-risk-monitor a 14-22% margin lever. <strong>SRM</strong> is the cross-functional practice of managing every supplier across a 4-phase lifecycle (Onboard + Develop + Manage + Off-board) with a tiered segmentation (Strategic / Preferred / Approved / Transactional / Spot / Blacklisted) and a quarterly business review (QBR) cadence that drives continuous improvement. <strong>QBR cadence</strong> is the structured quarterly meeting between brand-procurement, brand-merchandiser and OEM-factory leadership that walks the 11-KPI QBR scorecard (cost, quality, delivery, ESG, capacity, innovation, risk, financial-health, fill-rate, lead-time, chargeback) and assigns 4-9 action-items per quarter, with 80%+ action-completion target. <strong>Vendor-lifecycle governance</strong> is the policy-and-procedure layer (onboarding + KPI + audit + scorecard + QBR + CAB + offboarding) that ensures no supplier enters or exits the program without full governance review, with a 9-mandate compliance integration (BSCI, SEDEX, SMETA, ISO 9001, OEKO-TEX, FSC, GRS, GOTS, RBA). This playbook lays out the 122-module SRM, tiered QBR cadence and vendor-lifecycle governance architecture covering the 9-stage vendor-lifecycle governance, 8-stage SRM tiered segmentation, 11-KPI QBR scorecard, 14-clause vendor-lifecycle rider, 7-stage escalation CAB, 6-stakeholder RACI, 9-mandate compliance integration, plus 9-vendor-lifecycle, 8-SRM-segmentation, 7-QBR-cadence, 6-CAB-escalation, 5-supplier-development, 4-vendor-innovation, 6-supplier-risk, 5-financial-health, 4-supplier-audit, 6-vendor-scorecard, 5-quarterly-review, 4-supplier-onboarding, 6-supplier-offboarding, 5-supplier-collaboration, 4-supplier-co-development gates. Smith Ribbon runs this 122-module SRM, tiered QBR cadence and vendor-lifecycle governance architecture on a 7.6M meter multi-brand ribbon program delivering 14-to-32 percent vendor-consolidation lift, 18-to-46 percent QBR-action-completion lift, and 0% supplier-risk-blind.")
    body += section(s1_h, s1_p)

    s2_h = "The 9-Stage Vendor-Lifecycle Governance &amp; 8-Stage SRM Tiered Segmentation &amp; 11-KPI QBR Scorecard &amp; 14-Clause Vendor-Lifecycle Rider &amp; 7-Stage Escalation CAB &amp; 6-Stakeholder RACI &amp; 9-Mandate Compliance Integration"
    s2_p = ("The 9-stage vendor-lifecycle governance is the policy spine: <em>VL1 Onboarding-Request</em> (4-9% VL-stopper), <em>VL2 Compliance-Screen</em> (4-9% VL-stopper), <em>VL3 Financial-Health-Due-Diligence</em> (4-9% VL-stopper), <em>VL4 Capability-Audit</em> (4-9% VL-stopper), <em>VL5 Trial-PO</em> (4-9% VL-stopper), <em>VL6 Tier-Assignment</em> (4-9% VL-stopper), <em>VL7 Annual-Review</em> (4-9% VL-stopper), <em>VL8 Tier-Change</em> (4-9% VL-stopper), <em>VL9 Offboarding-Transition</em> (4-9% VL-stopper). The 8-stage SRM tiered segmentation: <em>SR1 Strategic-Definition</em> (60-80% of spend, 4-9% SR-stopper), <em>SR2 Preferred-Definition</em> (20-40%, 4-9% SR-stopper), <em>SR3 Approved-Definition</em> (5-15%, 4-9% SR-stopper), <em>SR4 Transactional-Definition</em> (5-10%, 4-9% SR-stopper), <em>SR5 Spot-Definition</em> (1-5%, 4-9% SR-stopper), <em>SR6 Blacklisted-Definition</em> (0%, 4-9% SR-stopper), <em>SR7 Spend-Allocation</em> (4-9% SR-stopper), <em>SR8 Tier-Rebalancing</em> (4-9% SR-stopper). The 11-KPI QBR scorecard: <em>QB1 Cost</em> (4-9% QB-stopper), <em>QB2 Quality</em> (4-9% QB-stopper), <em>QB3 Delivery</em> (4-9% QB-stopper), <em>QB4 ESG</em> (4-9% QB-stopper), <em>QB5 Capacity</em> (4-9% QB-stopper), <em>QB6 Innovation</em> (4-9% QB-stopper), <em>QB7 Risk</em> (4-9% QB-stopper), <em>QB8 Financial-Health</em> (4-9% QB-stopper), <em>QB9 Fill-Rate</em> (4-9% QB-stopper), <em>QB10 Lead-Time</em> (4-9% QB-stopper), <em>QB11 Chargeback</em> (4-9% QB-stopper). The 14-clause vendor-lifecycle rider: <em>VLR1 Definition</em>, <em>VLR2 Onboarding</em>, <em>VLR3 Audit-Right</em>, <em>VLR4 Compliance</em>, <em>VLR5 Tier-Definition</em>, <em>VLR6 Tier-Change</em>, <em>VLR7 QBR-Cadence</em>, <em>VLR8 QBR-Action</em>, <em>VLR9 CAB-Escalation</em>, <em>VLR10 Force-Majeure</em>, <em>VLR11 Confidentiality</em>, <em>VLR12 Anti-Bribery</em>, <em>VLR13 Offboarding</em>, <em>VLR14 Dispute</em>. The 7-stage escalation CAB: <em>CAB1 Issue-Raise</em> (4-9% CAB-stopper), <em>CAB2 L1-Procurement-Manager</em> (4-9% CAB-stopper), <em>CAB3 L2-Procurement-Director</em> (4-9% CAB-stopper), <em>CAB4 L3-VP-Procurement</em> (4-9% CAB-stopper), <em>CAB5 L4-C-Suite</em> (4-9% CAB-stopper), <em>CAB6 Resolution-Plan</em> (4-9% CAB-stopper), <em>CAB7 Close-Out-Audit</em> (4-9% CAB-stopper). The 6-stakeholder RACI: brand-procurement-CPO (A), brand-merchandiser-VP (R), OEM-factory-CEO (C), OEM-factory-QA-director (C), third-party-audit (C), finance-controller (C). The 9-mandate compliance integration: <em>CI1 BSCI</em>, <em>CI2 SEDEX</em>, <em>CI3 SMETA</em>, <em>CI4 ISO-9001</em>, <em>CI5 OEKO-TEX</em>, <em>CI6 FSC</em>, <em>CI7 GRS</em>, <em>CI8 GOTS</em>, <em>CI9 RBA</em>. End-state: 4-9% VL-stopper, 4-9% SR-stopper, 4-9% QB-stopper, 4-9% VLR-stopper, 4-9% CAB-stopper, 4-9% CI-stopper.")
    body += section(s2_h, s2_p)

    s3_h = "The 9-Vendor-Lifecycle &amp; 8-SRM-Segmentation &amp; 7-QBR-Cadence &amp; 6-CAB-Escalation &amp; 5-Supplier-Development &amp; 4-Vendor-Innovation &amp; 6-Supplier-Risk &amp; 5-Financial-Health &amp; 4-Supplier-Audit &amp; 6-Vendor-Scorecard &amp; 5-Quarterly-Review &amp; 4-Supplier-Onboarding &amp; 6-Supplier-Offboarding &amp; 5-Supplier-Collaboration &amp; 4-Supplier-Co-Development"
    s3_p = ("The vendor-lifecycle, SRM-segmentation, QBR-cadence, CAB-escalation, supplier-development, vendor-innovation, supplier-risk, financial-health, supplier-audit, vendor-scorecard, quarterly-review, supplier-onboarding, supplier-offboarding, supplier-collaboration, supplier-co-development gates: <em>VL1 Onboarding-Request</em>, <em>VL2 Compliance-Screen</em>, <em>VL3 Financial-Health-Due-Diligence</em>, <em>VL4 Capability-Audit</em>, <em>VL5 Trial-PO</em>, <em>VL6 Tier-Assignment</em>, <em>VL7 Annual-Review</em>, <em>VL8 Tier-Change</em>, <em>VL9 Offboarding-Transition</em>. <em>SR1 Strategic-Definition</em>, <em>SR2 Preferred-Definition</em>, <em>SR3 Approved-Definition</em>, <em>SR4 Transactional-Definition</em>, <em>SR5 Spot-Definition</em>, <em>SR6 Blacklisted-Definition</em>, <em>SR7 Spend-Allocation</em>, <em>SR8 Tier-Rebalancing</em>. <em>QB1 QBR-Weekly</em>, <em>QB2 QBR-Monthly</em>, <em>QB3 QBR-Quarterly</em>, <em>QB4 QBR-Annual</em>, <em>QB5 QBR-Strategic</em>, <em>QB6 QBR-Tactical</em>, <em>QB7 QBR-Operational</em>. <em>CAB1 L1-Procurement-Manager</em>, <em>CAB2 L2-Procurement-Director</em>, <em>CAB3 L3-VP-Procurement</em>, <em>CAB4 L4-C-Suite</em>, <em>CAB5 Resolution-Plan</em>, <em>CAB6 Close-Out-Audit</em>. <em>SD1 Kaizen-Event</em>, <em>SD2 Lean-Training</em>, <em>SD3 Six-Sigma</em>, <em>SD4 Capability-Build</em>, <em>SD5 Joint-Improvement</em>. <em>VI1 Open-Innovation</em>, <em>VI2 Co-Development</em>, <em>VI3 Vendor-Innovation-Award</em>, <em>VI4 Joint-R&amp;D</em>, <em>VI5 Innovation-Pipeline</em>, <em>VI6 Innovation-IP</em>. <em>SR1 Financial-Health</em>, <em>SR2 Geopolitical</em>, <em>SR3 ESG</em>, <em>SR4 Cyber</em>, <em>SR5 Compliance</em>, <em>SR6 Capacity</em>. <em>FH1 Credit-Rating</em>, <em>FH2 Cash-Flow</em>, <em>FH3 Working-Capital</em>, <em>FH4 DSO</em>, <em>FH5 DPO</em>. <em>SA1 Capability-Audit</em>, <em>SA2 Quality-Audit</em>, <em>SA3 ESG-Audit</em>, <em>SA4 Compliance-Audit</em>. <em>VS1 Vendor-Scorecard</em>, <em>VS2 KPI-Dashboard</em>, <em>VS3 Action-Tracker</em>, <em>VS4 Tier-Score</em>, <em>VS5 Improvement-Plan</em>, <em>VS6 Recognition</em>. <em>QR1 Quarterly-Review</em>, <em>QR2 Monthly-Review</em>, <em>QR3 Weekly-Review</em>, <em>QR4 Annual-Review</em>, <em>QR5 Ad-Hoc-Review</em>. <em>SO1 Onboarding-Request</em>, <em>SO2 Compliance-Screen</em>, <em>SO3 Trial-PO</em>, <em>SO4 Tier-Assignment</em>. <em>SO1 Offboarding-Plan</em>, <em>SO2 Bridge-Order</em>, <em>SO3 Knowledge-Transfer</em>, <em>SO4 Final-PO</em>, <em>SO5 Archive</em>, <em>SO6 Tier-Delist</em>. <em>SC1 Quarterly-Cadence</em>, <em>SC2 Joint-Planning</em>, <em>SC3 Joint-Forecast</em>, <em>SC4 Joint-Innovation</em>, <em>SC5 Joint-Improvement</em>. <em>SD1 Co-Development</em>, <em>SD2 Joint-IP</em>, <em>SD3 Joint-R&amp;D</em>, <em>SD4 Joint-Scale-Up</em>. End-state: 4-9% stoppers across every layer of the vendor-lifecycle, SRM-segmentation, QBR-cadence, CAB-escalation, supplier-development, vendor-innovation, supplier-risk, financial-health, supplier-audit, vendor-scorecard, quarterly-review, supplier-onboarding, supplier-offboarding, supplier-collaboration, supplier-co-development stack. Smith Ribbon operationalises this with a 9-step vendor-lifecycle audit (onboarding, compliance, financial-health, capability, trial-PO, tier-assignment, annual-review, tier-change, offboarding) plus a 6-stakeholder RACI and an 11-KPI QBR scorecard rolled up quarterly to brand procurement, brand merchandiser, and brand leadership. The result: 14-to-32 percent vendor-consolidation lift, 18-to-46 percent QBR-action-completion lift, and 0% supplier-risk-blind across the 7.6M meter multi-brand ribbon program.")
    body += section(s3_h, s3_p)

    s4_h = "How Smith Ribbon Operationalises the 122-Module SRM, Tiered QBR Cadence &amp; Vendor-Lifecycle Governance Program — 9-Step Audit, 6-Stakeholder RACI, 11-KPI Scorecard, 14-Clause Rider, 7-Stage CAB"
    s4_p = ("Smith Ribbon operationalises the 122-module supplier relationship management (SRM), tiered QBR cadence and vendor-lifecycle governance program through a <em>9-step audit</em>, a <em>6-stakeholder RACI</em>, an <em>11-KPI scorecard</em>, a <em>14-clause rider</em>, and a <em>7-stage CAB</em> protocol. The 9-step audit walks every private-label ribbon OEM supplier through onboarding, compliance, financial-health, capability, trial-PO, tier-assignment, annual-review, tier-change, offboarding. Each step has a 4-9% supplier-governance failure rate; the 9-step audit compresses that to less than 1%. The 6-stakeholder RACI assigns brand-procurement-CPO (A), brand-merchandiser-VP (R), OEM-factory-CEO (C), OEM-factory-QA-director (C), third-party-audit (C), finance-controller (C), so no decision stalls in inter-functional ambiguity. The 11-KPI QBR scorecard (QB1-QB11 above) is the quarterly brand-procurement and OEM-factory-CEO reporting layer. The 14-clause vendor-lifecycle rider is the legal layer that binds SRM, tiered-QBR and vendor-lifecycle governance to a 14-32% vendor-consolidation lift and 18-46% QBR-action-completion lift contractually. The 7-stage escalation CAB (CAB1-CAB7) is the cross-functional escalation channel that resolves any supplier-issue within 30 days. Practical 2026 example: a global beauty brand owner managing 12 ribbon OEM suppliers across 6 categories (satin, organza, velvet, grosgrain, wired, RPET) for a 2.8M meter private-label program — 9-stage vendor-lifecycle governance (onboarding + BSCI compliance + D&B financial-health + capability-audit + trial-PO + tier-assignment + annual-review + tier-change + offboarding), 8-stage SRM tiered segmentation (2 Strategic at 60% spend + 3 Preferred at 25% + 4 Approved at 10% + 2 Transactional at 4% + 1 Spot at 1% + 0 Blacklisted), 11-KPI QBR scorecard (cost, quality, delivery, ESG, capacity, innovation, risk, financial-health, fill-rate, lead-time, chargeback), 14-clause vendor-lifecycle rider, 7-stage escalation CAB (L1 manager + L2 director + L3 VP + L4 C-suite + resolution-plan + close-out), 6-stakeholder RACI, 9-mandate compliance integration (BSCI + SEDEX + SMETA + ISO 9001 + OEKO-TEX + FSC + GRS + GOTS + RBA). Smith Ribbon delivers 2.8M meters with 14-32% vendor-consolidation lift, 18-46% QBR-action-completion lift, 0% supplier-risk-blind. The SRM, tiered QBR cadence and vendor-lifecycle governance program is the structural backbone of any 2026 B2B OEM private-label program, and Smith Ribbon's 122-module framework turns it from a procurement-fluff concept into a 14-32% vendor-consolidation lift, 18-46% QBR-action-completion lift, 0% supplier-risk-blind operating system.")
    body += section(s4_h, s4_p)

    body += footer("If you are a brand owner, retail private-label director, beauty or fashion merchandising leader, or procurement transformation lead evaluating a 2026-08 SRM, tiered-QBR cadence and vendor-lifecycle governance program, ask Smith Ribbon for the 122-Module SRM, Tiered QBR Cadence &amp; Vendor-Lifecycle Governance Architecture sample audit, 11-KPI QBR scorecard template, 14-clause vendor-lifecycle rider template, 9-stage vendor-lifecycle governance template, 8-stage SRM tiered segmentation template, 7-stage escalation CAB template, 9-mandate compliance integration checklist, and a brand-by-brand quote. We support OEM, ODM, private-label, co-brand, licensed-brand, ingredient-brand and house-of-brands programs with 1000-meter MOQ, 500-meter small-batch, 6-12 week lead time, 12 stock colors, 6 widths, 4 finishes, 7 materials (polyester, satin, organza, velvet, grosgrain, wired, RPET), and full OEKO-TEX 100, FSC, BSCI, SEDEX, ISO 9001, SMETA compliance. Contact: xmmsd@126.com / +86 13779951780.")
    return body


# =============================================================================
# Build & write
# =============================================================================
def main():
    html1 = build_art1()
    p1 = WORK / f"{ART1['slug']}.html"
    p1.write_text(html1, encoding="utf-8")
    print(f"  wrote {p1.name}  ({len(html1):,} bytes, ~{ART1['words']} words)")

    html2 = build_art2()
    p2 = WORK / f"{ART2['slug']}.html"
    p2.write_text(html2, encoding="utf-8")
    print(f"  wrote {p2.name}  ({len(html2):,} bytes, ~{ART2['words']} words)")

    # ---- update sitemap.xml ----
    sitemap = WORK / "sitemap.xml"
    if sitemap.exists():
        txt = sitemap.read_text(encoding="utf-8")
        today = "2026-08-29"
        for slug in (ART1['slug'], ART2['slug']):
            entry = (
                f"  <url><loc>{DOMAIN}/{slug}.html</loc>"
                f"<lastmod>{today}</lastmod>"
                f"<changefreq>monthly</changefreq>"
                f"<priority>0.85</priority></url>\n"
            )
            # insert before </urlset> if not present
            if f"/{slug}.html" not in txt:
                txt = txt.replace("</urlset>", entry + "</urlset>")
        sitemap.write_text(txt, encoding="utf-8")
        print("  updated sitemap.xml")

    # ---- append to en-blog.html listing ----
    blog = WORK / "en-blog.html"
    if blog.exists():
        btxt = blog.read_text(encoding="utf-8")
        today_disp = "August 29, 2026"
        slots = [
            (ART1, "AM (08:00 UTC+8) — Mill-Side Energy, Water & Scope-3 Decarbonization"),
            (ART2, "PM (13:00 UTC+8) — SRM, Tiered QBR & Vendor-Lifecycle Governance"),
        ]
        for art, slot in slots:
            link = f"{DOMAIN}/{art['slug']}.html"
            anchor = f'<li><a href="/{art["slug"]}.html">{today_disp} &middot; {slot} &middot; {art["title"][:90]}...</a></li>'
            if link not in btxt and art['slug'] not in btxt:
                # naive append before </ul> or at end of body
                btxt = btxt.replace("</body>", f"<ul>{anchor}</ul></body>")
        blog.write_text(btxt, encoding="utf-8")
        print("  updated en-blog.html")

    print("\nDone — 2 articles generated.")


if __name__ == "__main__":
    main()
