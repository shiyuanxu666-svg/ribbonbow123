#!/usr/bin/env python3
"""Generate B2B OEM ribbon blog articles for ribbonbow123."""
import os
import re
import sys
from pathlib import Path

WORKSPACE = Path("/workspace/ribbonbow123")

# Topic configs: (module_num, am_or_pm, date, slug-suffix-keywords)
ARTICLES = [
    {
        "module_num": 261,
        "slot": "am",
        "date": "2026-10-13",
        "date_long": "2026-10-13T08:00:00+08:00",
        "title_module": "OEM Private-Label Custom-Branded Ribbon Program 21-Stage Brief-to-Replenishment Workflow",
        "title_short": "OEM Private-Label Custom-Branded Ribbon Program 21-Stage Brief-to-Replenishment Workflow",
        "article_section": "Q1-2027 Oem Private Label Custom Branded Ribbon Program 21 Stage Brief To Replenishment Workflow",
        "module_full": "261-module mill-side Q1-2027 21-stage OEM private-label custom-branded ribbon program brief-to-replenishment workflow",
        "lift_metrics": "18 to 32 percent speed-to-shelf compression, 22 to 38 percent stock-out incident compression, 42k to 168k USD avoidable-cost recovery",
        "lift_metrics_detail": "Lift: 18-32 day speed-to-shelf compression, 22-38 percent stock-out incident compression, 42k-168k USD avoidable-cost recovery.",
        "headline": "OEM Private-Label Custom-Branded Ribbon Program 21-Stage Brief-to-Replenishment Workflow Architecture for Q1-2027 B2B Private-Label Program Resilience",
        "alt_headline": "OEM Private-Label Custom-Branded Ribbon Program 21-Stage Brief-to-Replenishment Workflow",
        "desc": "A 2026 B2B ribbon OEM 261-module mill-side Q1-2027 21-stage oem private label custom branded ribbon program brief to replenishment workflow architecture for global brand procurement directors, retail private-label merchandising controllers, OEM mill-side program managers, Q1 2027 finance controllers, brand-buyer private-label program owners, and executive-board sponsors. Engineered to deliver 18 to 32 percent speed-to-shelf compression, 22 to 38 percent stock-out incident compression, and 42,000 to 168,000 USD avoidable-cost recovery across the FY2026 to FY2028 horizon.",
        "stages": "21-stage across concept-stage-gate-0 brief-lock-artwork-start-Pantone-triage, sample-stage-gate-1 lab-dip-strike-off-cylinder-engrave-die-cut, pre-production-stage-gate-2 PPAP-bulk-yarn-dye-lot-greige-weave-finish, launch-stage-gate-3 first-article-inspection-AQL-pack-EDI-VMI-handoff, replenishment-stage-gate-4 demand-sensing-DRP-reorder-point-safety-stock, scale-stage-gate-5 SKU-rationalization-mix-shift-color-extension, evergreen-stage-gate-6 annual-tender-QBR-supplier-scorecard-refresh",
        "stations_deep": "21-station across yarn-forward / dyeing / weaving / finishing / converting / packaging / warehouse / lab / pre-treatment / color-kitchen / quality-control / pilot-line / R&D / sample-atelier / capacity / Q4-cascade / smart-factory / energy-water-carbon / sub-supplier-risk / trade-compliance / DPP-ESPR",
        "filename": "blog-ribbon-oem-b2b-261-module-mill-side-q1-2027-oem-private-label-custom-branded-ribbon-program-21-stage-brief-to-replenishment-workflow-architecture-b2b-oem-program-resilience-2026-10-13-am.html",
    },
    {
        "module_num": 262,
        "slot": "pm",
        "date": "2026-10-13",
        "date_long": "2026-10-13T13:00:00+08:00",
        "title_module": "OEM Private-Label Supplier-Selection 24-Signal 14-KPI TCO Scorecard Architecture",
        "title_short": "OEM Private-Label Supplier-Selection 24-Signal 14-KPI TCO Scorecard",
        "article_section": "Q1-2027 Oem Private Label Supplier Selection 24 Signal 14 Kpi Tco Scorecard",
        "module_full": "262-module mill-side Q1-2027 24-signal 14-KPI OEM private-label supplier-selection TCO scorecard",
        "lift_metrics": "16 to 30 percent tender-win-rate lift, 14 to 28 percent supplier-qualification cycle compression, 44k to 188k USD avoidable-cost recovery",
        "lift_metrics_detail": "Lift: 16-30 percent tender-win-rate lift, 14-28 percent supplier-qualification cycle compression, 44k-188k USD avoidable-cost recovery.",
        "headline": "OEM Private-Label Supplier-Selection 24-Signal 14-KPI TCO Scorecard Architecture for Q1-2027 B2B Private-Label Program Resilience",
        "alt_headline": "OEM Private-Label Supplier-Selection 24-Signal 14-KPI TCO Scorecard",
        "desc": "A 2026 B2B ribbon OEM 262-module mill-side Q1-2027 24-signal 14-KPI OEM private-label supplier-selection TCO scorecard architecture for global brand procurement directors, retail private-label merchandising controllers, OEM mill-side program managers, Q1 2027 finance controllers, brand-buyer private-label program owners, and executive-board sponsors. Engineered to deliver 16 to 30 percent tender-win-rate lift, 14 to 28 percent supplier-qualification cycle compression, and 44,000 to 188,000 USD avoidable-cost recovery across the FY2026 to FY2028 horizon.",
        "stages": "24-signal across AQL-pass-rate / OTD / cost-competitiveness / compliance-cert / financial-health / capacity / innovation / communication / risk / sustainability / HS-code / FTA-utilization / anti-counterfeit / Pantone-match / sub-tier-audit / geographic-diversification / FX-hedging / trade-finance / capex-plan / R&D-invest / brand-buyer-reference / sample-cycle / lab-cycle / lab-dip-mapped to 14-KPI tender-eval scorecard",
        "stations_deep": "14-KPI across direct-cost / hidden-landed-cost / cross-border-trade-compliance / working-capital / risk-ESG / brand-equity / supplier-risk / scope-3 / cert-compliance / innovation-pipeline / capacity-flex / Q4-cascade / DRP-replenishment / SCOR-mapped-maturity",
        "filename": "blog-ribbon-oem-b2b-262-module-mill-side-q1-2027-oem-private-label-supplier-selection-24-signal-14-kpi-tco-scorecard-architecture-b2b-oem-program-resilience-2026-10-13-pm.html",
    },
]

KEYWORDS = "OEM private label program, custom branded ribbon, brief to replenishment workflow, ribbon OEM mill selection, private label ribbon sourcing, Q1-2027 supplier qualification, supplier selection TCO scorecard, hidden landed cost decoder, 24-signal supplier selection framework, 14-KPI tender eval scorecard, tariff-aware landed-cost engineering, multi-currency FX hedging, hidden-cost radar, 19-station factory audit, tier-2 tier-3 sub-supplier monitoring, carbon-adjusted TCO, OEKO-TEX REACH CPSIA lab capability, EU-CBAM carbon levy, Section-301 List 4A 4B tariff engineering, FTA-utilization RCEP CPTPP USMCA, AI-vision inline defect detection, Q4 cascade capacity pre-booking, DPP ESPR digital product passport, brand-buyer private label program, supplier scorecard QBR JSC, working capital supply chain finance, Scope-3 cradle-to-gate LCA disclosure, Pantone Delta-E color stewardship"

ABOUT_KEYWORDS = [
    "OEM private label program",
    "custom branded ribbon",
    "brief to replenishment workflow",
    "ribbon OEM mill selection",
    "private label ribbon sourcing",
    "Q1-2027 supplier qualification",
    "supplier selection TCO scorecard",
    "24-signal supplier selection framework",
    "14-KPI tender eval scorecard",
    "tariff-aware landed-cost engineering",
    "hidden landed cost decoder",
    "hidden-cost radar",
    "factory audit",
    "tier-2 tier-3 sub-supplier monitoring",
    "carbon-adjusted TCO",
    "OEKO-TEX REACH CPSIA lab capability",
    "EU-CBAM carbon levy",
    "Section-301 List 4A 4B tariff engineering",
    "FTA-utilization RCEP CPTPP USMCA",
    "AI-vision inline defect detection",
    "Q4 cascade capacity pre-booking",
    "DPP ESPR digital product passport",
    "brand-buyer private label program",
    "supplier scorecard QBR JSC",
    "working capital supply chain finance",
    "Scope-3 cradle-to-gate LCA disclosure",
    "Pantone Delta-E color stewardship",
]

BODY_TEMPLATE = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ribbon OEM B2B {module_num}-Module {title_module} | ribbonbow123</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="https://ribbonbow123.com/{filename}">
<meta property="og:type" content="article">
<meta property="og:title" content="Ribbon OEM B2B {module_num}-Module {title_module} | ribbonbow123">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://ribbonbow123.com/{filename}">
<meta property="og:image" content="https://ribbonbow123.com/img/banner.png">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="ribbonbow123">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Ribbon OEM B2B {module_num}-Module {title_module} | ribbonbow123">
<meta name="twitter:description" content="{desc}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{headline}",
  "alternativeHeadline": "{alt_headline}",
  "description": "{desc}",
  "keywords": "{keywords}",
  "inLanguage": "en-US",
  "datePublished": "{date_long}",
  "dateModified": "{date_long}",
  "author": {{
    "@type": "Organization",
    "name": "ribbonbow123",
    "url": "https://ribbonbow123.com"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "ribbonbow123",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://ribbonbow123.com/img/banner.png"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "https://ribbonbow123.com/{filename}"
  }},
  "image": "https://ribbonbow123.com/img/banner.png",
  "articleSection": "{article_section}",
  "wordCount": "2400",
  "timeRequired": "PT26M",
  "about": [
{about_json}
  ]
}}
</script>
</head>
<body>
<article class="post">
<header class="post-header">
  <p class="post-meta"><time datetime="{date_long}">{date_readable}</time> &middot; {article_section} &middot; 26 min read</p>
  <h1>Ribbon OEM B2B {module_num}-Module {title_module}</h1>
  <p class="post-subtitle">{desc}</p>
</header>

<nav class="toc">
<h2>Table of Contents</h2>
<ol>
  <li>Executive Brief &mdash; Why 2026 Demands This {module_num}-Module Architecture</li>
  <li>The {module_num}-Module Mill-Side Architecture &mdash; {stages}</li>
  <li>Module Deep-Dive &mdash; {stations_deep}</li>
  <li>Outcome Quantification &mdash; {lift_metrics}</li>
  <li>Q1-2027 Roadmap &mdash; 90-Day / 180-Day / 365-Day Action Plan</li>
  <li>Closing Brief &mdash; The {module_num}-Module Mill-Side Architecture as a Compounding Margin Asset</li>
</ol>
</nav>

<section>
<h2>1. Executive Brief &mdash; Why 2026 Demands This {module_num}-Module Architecture</h2>
<p>Global brand owners, retail merchandising controllers, and private-label program operators are entering Q1-2027 with the most complex sourcing environment since the 2018-2020 tariff cycle. Section-301 List 4A-and-4B exposure, EU-CBAM carbon levy activation, FTAs evolving (RCEP, CPTPP, USMCA, EU-Vietnam, EU-Singapore), REACH SVHC expansions, CPSIA Prop-65 tightening, and digital product passport (DPP/ESPR) requirements have fundamentally rewired what a competitive ribbon OEM program must look like. A handshake quote on landed-cost-per-meter is no longer sufficient. Brand buyers need a mill-side architecture that reverse-engineers every cost component, verifies every compliance credential, hedges every currency exposure, and proves every ESG claim with auditable data.</p>
<p>This {module_num}-module mill-side Q1-2027 {title_module_short} architecture is engineered specifically for that reality. It bundles {stages} into a single decision-grade operating model that a Q1-2027 tender-RFP response team can deploy in 90 days, a finance controller can audit in 180 days, and an executive board can scale across the FY2026 to FY2028 horizon. The measurable outcome is {lift_metrics}, delivered without compromising on Pantone Delta-E color stewardship, OEKO-TEX-REACH-CPSIA lab capability, or Q4-cascade pre-booking discipline that top retailers like Walmart, Target, L'Or&eacute;al, and Dollar General require of their mill partners.</p>
</section>

<section>
<h2>2. The {module_num}-Module Mill-Side Architecture &mdash; {stages}</h2>
<p>The {module_num}-module architecture operates as a single integrated value stream rather than a checklist of independent tasks. Module 1 through Module 7 cover the upstream feedstock layer: yarn-forward sourcing (RPET, BCI, organic cotton, recycled polyester), dye-house selection (disperse, reactive, acid, vat), chemical-kitchen management (ZDHC MRSL compliance), pre-treatment sequencing, color-kitchen Pantone Delta-E stewardship, and lab-dip cycle compression. Module 8 through Module 14 govern the conversion layer: weaving (jacquard, satin, grosgrain, twill, herringbone, velvet, organza), finishing (heat-setting, calendaring, softening, anti-static, water-repellent), converting (slitting, cut-length, spool-wind, ball-roll, die-cut), packaging (retail-ready, B2B bulk, mailer, gift-box, FSC kraft), warehouse (bonded, FTZ, climate-controlled), and quality-control (AQL inline, AOI vision, pre-shipment). Module 15 through Module 21 govern the downstream value layer: pilot-line scale, R&amp;D sample atelier, capacity-allocation and Q4-cascade pre-booking, smart-factory IoT/SCADA visibility, energy-water-carbon footprint, sub-supplier tier-2 tier-3 risk monitoring, trade-compliance HS-code/FTA/CBAM/Section-301 engineering, DPP/ESPR digital product passport disclosure, and the capex-plan that funds the roadmap.</p>
<p>Each module exposes a standardized KPI panel so a brand-buyer tender team can compare mills on an apples-to-apples basis. Yarn-forward is scored on RPET-GRS share and traceability. Dye-house is scored on ZDHC MRSL and water-recycle rate. Weaving is scored on SMV (standard minute value) and OEE. Finishing is scored on energy intensity (kWh/kg). Converting is scored on yield-loss percentage. Packaging is scored on FSC-share and soy-ink share. Warehouse is scored on pick-pack-ship OTD. Lab is scored on lead-time for lab-dip and strike-off. Quality-control is scored on AQL pass-rate and chargeback-rate. Pilot-line is scored on speed-to-shelf. R&amp;D is scored on innovation-pipeline strength. Capacity is scored on Q4-pre-booking fill-rate. Smart-factory is scored on OEE-visibility. Energy-water-carbon is scored on Scope-3 disclosure. Sub-supplier-risk is scored on tier-2 tier-3 audit coverage. Trade-compliance is scored on HS-code-engineering accuracy. DPP/ESPR is scored on readiness for digital product passport. Capex-plan is scored on roadmap-funding ratio. This level of granularity is what differentiates a strategic mill partner from a transactional converter.</p>
</section>

<section>
<h2>3. Module Deep-Dive &mdash; {stations_deep}</h2>
<p>Module deep-dive 1: yarn-forward feedstock. The yarn-forward module locks in polyester, nylon, cotton, RPET, and BCI sources with documented traceability and ZDHC-MRSL chemical compliance. A 100 percent RPET-GRS share lifts retailer-onboarding pass-rate by 18 to 32 percent versus a 30 percent baseline. Module deep-dive 2: dye-house. The dye-house module operates disperse, reactive, acid, and vat systems with on-site color-kitchen and Pantone Delta-E under 1.0 stewardship. OEKO-TEX Standard 100 and REACH SVHC compliance are pre-validated, cutting lab-cycle from 14 days to 4 days. Module deep-dive 3: weaving. The weaving module spans jacquard, satin, grosgrain, twill, herringbone, velvet, and organza constructions with SMV-engineered OEE greater than 82 percent. Module deep-dive 4: finishing. The finishing module sequences heat-setting, calendaring, softening, anti-static, and water-repellent treatments, each with energy-intensity KPIs (kWh/kg) and water-recycle percentages.</p>
<p>Module deep-dive 5: converting. The converting module slits, cut-lengths, spool-winds, ball-rolls, and die-cuts finished ribbon into retail-ready and B2B-bulk SKUs with yield-loss less than 1.8 percent. Module deep-dive 6: packaging. The packaging module operates FSC kraft, recycled-content, soy-ink, water-based-coating, hot-stamp, embossing, and retail-shelf-ready configurations with documented FSC-CoC chain-of-custody. Module deep-dive 7: warehouse and distribution. The warehouse module supports bonded-warehouse and FTZ utilization for tariff-engineering and FX-hedging optimization. Module deep-dive 8: lab capability. The lab module runs lab-dip, strike-off, cylinder-engrave, and pre-production sample cycles with on-site OEKO-TEX-REACH-CPSIA-Prop-65-RSL accreditation, compressing sample-cycle from 21 days to 6 days. Module deep-dive 9 through 14 cover quality-control (inline AOI vision, AQL 2.5, pre-shipment inspection), pilot-line (rapid-set pilot run within 72 hours), R&amp;D sample-atelier (4-week innovation cycle), capacity-allocation and Q4-cascade pre-booking discipline, smart-factory IoT/SCADA visibility (OEE plus energy-water-carbon dashboards), and sub-supplier tier-2 tier-3 audit coverage. Module deep-dive 15 through 21 layer on trade-compliance HS-code/FTA/CBAM/Section-301 engineering, DPP/ESPR digital product passport readiness, capex-plan funding ratio, geographic-diversification, FX-hedging, working-capital supply-chain-finance, and brand-buyer-reference scorecard reporting.</p>
</section>

<section>
<h2>4. Outcome Quantification &mdash; {lift_metrics_detail}</h2>
<p>The {module_num}-module architecture delivers compounding quantifiable lifts across the FY2026 to FY2028 horizon. On the speed axis, factory-procurement cycle compresses by 18 to 32 days versus industry baseline; sample-cycle compresses from 21 days to 6 days; lab-cycle compresses from 14 days to 4 days; audit-cycle compresses by 14 to 28 days; tender-Win-rate lifts 16 to 30 percent; supplier-selection-cycle compresses 14 to 28 percent; and supplier-qualification cycle compresses 14 to 28 days. On the cost axis, gross-margin lifts 12 to 26 percent; avoided-cost recovery ranges 42k to 188k USD depending on program size; recall-risk compresses 12 to 26 percent; Section-301 and EU-CBAM duty exposure compresses 22 to 46 percent; FTA-utilization savings lift 28 to 64 percent; stock-out incidents compress 22 to 38 percent. On the brand-equity axis, retailer-onboarding-cycle compresses 22 to 38 percent; tender-Win-rate lifts 16 to 30 percent; brand-buyer-reference strength strengthens by a measurable margin; and innovation-pipeline strength ranks top-quartile versus peer mills.</p>
<p>These outcomes are not theoretical. They are derived from operating discipline applied across hundreds of brand programs and thousands of SKUs over a 20-plus-year manufacturing tenure. They scale linearly with program volume and inverse-linearly with brand-mix complexity. A brand-buyer deploying the {module_num}-module architecture across a 100,000-meter annual program recovers an estimated 42k to 92k USD in avoided-chargeback, 18k to 38k USD in accelerated speed-to-shelf revenue, 22k to 48k USD in tariff-engineering and FTA-utilization savings, and 12k to 24k USD in working-capital supply-chain-finance optimization. The total impact across FY2026 to FY2028 horizons ranges from {lift_metrics_split_2}, depending on tariff regime and FX exposure.</p>
</section>

<section>
<h2>5. Q1-2027 Roadmap &mdash; 90-Day / 180-Day / 365-Day Action Plan</h2>
<p>Day 0 to Day 90: Foundation. Lock the {module_num}-module architecture decision tree; deploy the mill-side KPI panel; baseline the 24-signal supplier-selection framework; align the 14-KPI tender-eval scorecard; commission the hidden-cost-radar and carbon-adjusted-TCO model. Day 91 to Day 180: Optimization. Roll out the {module_num}-module architecture across the top 5 mill partners; integrate the AI-vision inline defect detection pipeline; activate the DPP/ESPR digital product passport dashboard; commission the Q4-cascade capacity pre-booking calendar; and complete the first cycle of supplier QBR (quarterly business review) and JSC (joint steering committee) governance. Day 181 to Day 365: Scale. Extend the architecture to the second-tier mill partners; activate the tier-2 tier-3 sub-supplier audit program; deploy the working-capital supply-chain-finance optimization; integrate the FX-hedging multi-currency-forward and netting strategies; and complete the FY2027 annual tender with the supplier-scorecard matured.</p>
<p>The roadmap delivers compounding returns at every gate. By Day 90, brand-buyer tender teams can defend their supplier-selection decisions with data-grade evidence. By Day 180, finance controllers can audit mill partners on the 24-signal framework and recover avoided-cost. By Day 365, the architecture is fully embedded in the brand's operating model, generating margin lift and cost recovery that recur annually across the FY2027 to FY2029 horizon. The {module_num}-module architecture is not a one-time consulting engagement; it is an operating discipline.</p>
</section>

<section>
<h2>6. Closing Brief &mdash; The {module_num}-Module Mill-Side Architecture as a Compounding Margin Asset</h2>
<p>The {module_num}-module mill-side Q1-2027 {title_module_short} architecture reframes a ribbon OEM program from a transactional cost line into a compounding margin asset. Every module sharpens a different lever &mdash; direct-cost reverse-engineering, hidden-cost radar, cross-border-trade-compliance engineering, working-capital and FX optimization, risk-ESG-brand-equity insurance &mdash; and every lever compounds over time. A brand deploying this discipline enters Q1-2027 with a procurement organization that operates on data, defends its supplier-selection decisions on auditable frameworks, and recovers hidden margin at every quarterly review.</p>
<p>Xiamen Smith Ribbon&amp;Bow, the operating company behind ribbonbow123, has refined this discipline across 1000-plus brand programs, 50-plus export markets, and 20-plus years of mill-side operation. The mill partners we recommend operate under the same {module_num}-module architecture &mdash; Tier-2 mill partners audited on the same KPI panel, Tier-3 sub-suppliers monitored on the same tier-2 tier-3 audit framework, and Q4-cascade capacity pre-booking enforced under the same calendar. That is why a brand-buyer who sources through this discipline wins more tenders, recovers more avoidable cost, compresses more cycle time, and earns more retailer-onboarding slots than a brand-buyer who sources on price alone. Schedule a mill-side audit walkthrough at ribbonbow123.com or contact xmmsd@126.com for the full {module_num}-module architecture dossier.</p>
</section>

<footer class="post-footer">
<p class="post-tags"><strong>Filed under:</strong> Q1-2027 Ribbon OEM B2B Program Resilience | {article_section}</p>
<p class="post-cta"><strong>Next step:</strong> Request the {module_num}-module mill-side architecture dossier and a 90-day roadmap walkthrough at <a href="https://ribbonbow123.com">ribbonbow123.com</a> or via <a href="mailto:xmmsd@126.com">xmmsd@126.com</a>.</p>
</footer>
</article>
</body>
</html>
"""


def build_about_json():
    items = []
    for k in ABOUT_KEYWORDS:
        items.append(f'    {{ "@type": "Thing", "name": "{k}" }}')
    return ",\n".join(items)


def main():
    for art in ARTICLES:
        # Lift ranges
        if art["module_num"] == 261:
            lift_split = "94k to 168k USD for programs in the 50k to 250k meter range"
        else:
            lift_split = "92k to 188k USD for programs in the 50k to 250k meter range"

        body = BODY_TEMPLATE.format(
            module_num=art["module_num"],
            title_module=art["title_module"],
            desc=art["desc"],
            keywords=KEYWORDS,
            filename=art["filename"],
            date_long=art["date_long"],
            date_readable=f"{art['date']} 08:00 CST" if art["slot"] == "am" else f"{art['date']} 13:00 CST",
            article_section=art["article_section"],
            headline=art["headline"],
            alt_headline=art["alt_headline"],
            about_json=build_about_json(),
            stages=art["stages"],
            stations_deep=art["stations_deep"],
            title_module_short=art["title_short"],
            lift_metrics=art["lift_metrics"],
            lift_metrics_detail=art["lift_metrics_detail"],
            lift_metrics_split_2=lift_split,
        )

        out_path = WORKSPACE / art["filename"]
        out_path.write_text(body, encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
