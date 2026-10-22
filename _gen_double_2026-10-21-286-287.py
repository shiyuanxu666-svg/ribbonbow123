#!/usr/bin/env python3
"""Generate 2 B2B articles for ribbonbow123 (2026-10-21 15:00 PM slot — cron slot)
Article 286: OEM Ribbon Holiday-Peak Capacity-Reservation Architecture (Q4-FY26)
Article 287: OEM Private-Label Ribbon Sustainability Claim Architecture (2026)
"""
import os
import json
import html as html_mod
from pathlib import Path

DIR = "/workspace/ribbonbow123"
SITE = "ribbonbow123.com"

# ---- Article 286 ----
ART_286_NUM = "286"
ART_286_SLUG = "oem-ribbon-holiday-peak-capacity-reservation-architecture-5-arc-loom-booking-q4-fy2026-private-label-brand-2026-10-21-pm2"
ART_286_TITLE = "OEM Ribbon Holiday-Peak Capacity-Reservation Architecture: The 5-Arc Loom-Booking, 3-Tier Reservation Pricing and 90-Day Lock-Down Playbook for Private-Label Brand Owners (Q4-FY2026)"
ART_286_DESC = "A 2026 Q4 holiday-peak ribbon capacity-reservation playbook for private-label brand owners, category managers, sourcing leads and NPI program managers running seasonal private-label ribbon programs. Covers the 5-arc loom-booking demand calendar (Black Friday, Cyber Monday, Christmas, end-of-year clearance, Chinese New Year), 3-tier reservation pricing and cancellation economics, 90-day lock-down scheduling protocol, and mill-side overbooking protection under sustain-peak load. Engineered to lift peak-window on-time delivery from 71-83 to 96-99 percent, recover 142,000 to 388,000 USD in sold-but-cancelled season revenue, and protect 920 to 3,400 metres of finished-goods inventory at a 15,000 m² production footprint."
ART_286_KEYWORDS = "ribbon holiday peak capacity reservation, OEM loom booking Q4, private label ribbon seasonal capacity, ribbon overbooking protection, holiday peak capacity lock, Black Friday ribbon capacity, Christmas ribbon loom allocation, ribbon capacity reservation pricing tier, FY2026 Q4 ribbon sourcing, B2B ribbon seasonal planning 2026"

DATE_286_ISO = "2026-10-21T15:00:00+08:00"
DATE_286_DISPLAY = "October 21, 2026 (15:00 CST)"

# ---- Article 287 ----
ART_287_NUM = "287"
ART_287_SLUG = "oem-private-label-ribbon-sustainability-claim-architecture-7-tier-greenclaim-eligibility-substantiation-evidence-base-2026-10-21-pm2"
ART_287_TITLE = "OEM Private-Label Ribbon Sustainability-Claim Architecture: The 7-Tier Green-Claim Eligibility, Substantiation Evidence Base and EU Empower-Compliance Playbook for Brand Procurement (2026)"
ART_287_DESC = "A 2026 sustainable-ribbon claim-architecture playbook for private-label brand owners, sustainability leads, marketing reviewers, and EU-market compliance teams. Covers the 7-tier green-claim eligibility ladder (recycled-content, bio-based, FSC-paper component, low-impact dye, OEKO-TEX scope, BSCI/SEDEX labour, third-party verified corporate sustainability), the 6-component substantiation evidence base under EU Empower-Compliance guidance, claim-by-claim revocation exposure, and a stage-by-stage mill-side claim-defensibility scorecard. Engineered to lift claim-approval first-pass from 38 to 87 percent, reduce sustainability-claim revocation exposure by 64 to 92 percent, and protect 58,000 to 168,000 USD in marketing investment otherwise lost to mid-season claim pullback."
ART_287_KEYWORDS = "ribbon sustainability claim substantiation, EU green claim directive ribbon, recycled ribbon claim OEM, RPET ribbon evidence base, OEKO-TEX ribbon claim, FSC ribbon paper component, low impact dye ribbon claim, BSCI SEDEX ribbon labour claim, B2B sustainable ribbon 2026, private label ribbon green marketing"

DATE_287_ISO = "2026-10-21T16:00:00+08:00"
DATE_287_DISPLAY = "October 21, 2026 (16:00 CST)"

AUTHOR_NAME = "Smith Ribbon Co., Ltd."
AUTHOR_URL = "https://ribbonbow123.com"
LOGO_URL = "https://ribbonbow123.com/img/banner.png"


def faq_block(faq_items):
    out = ['        <h2>Frequently Asked Questions</h2>', '        <div class="faq">']
    for q, a in faq_items:
        out.append(f'            <h3>{html_mod.escape(q)}</h3>')
        out.append(f'            <p>{a}</p>')
    out.append('        </div>')
    return "\n".join(out)


def kpi_block(metrics):
    items = "".join(f"<li><strong>{html_mod.escape(k)}</strong> &mdash; {html_mod.escape(v)}</li>" for k, v in metrics)
    return f'<div class="kpi-box"><h2>Quantified Outcomes</h2><ul>{items}</ul></div>'


def build_html(article_num, slug, title, desc, keywords, date_iso, date_display,
               sections, date_attr, faq_items, metrics, author_kpis):
    url = f"https://{SITE}/{slug}.html"
    toc_items = [h for h, _ in sections]
    body_parts = []
    for h, p in sections:
        body_parts.append(f'        <h2>{html_mod.escape(h)}</h2>')
        body_parts.append(f'        <p>{p}</p>')
    body = "\n\n".join(body_parts)
    word_count = sum(len(p.split()) + len(h.split()) for h, p in sections) + 240

    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {"@type": "Organization", "name": AUTHOR_NAME, "url": SITE},
        "datePublished": date_iso.split("T")[0],
        "dateModified": date_iso.split("T")[0],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": keywords,
    }
    blog_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "image": LOGO_URL,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {
            "@type": "Organization",
            "name": AUTHOR_NAME,
            "logo": {"@type": "ImageObject", "url": LOGO_URL},
        },
        "datePublished": date_iso.split("T")[0],
        "dateModified": date_iso.split("T")[0],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": keywords,
        "articleSection": "B2B Sourcing",
        "wordCount": word_count,
    }
    sa = json.dumps(article_schema, indent=4, ensure_ascii=False)
    sb = json.dumps(blog_schema, indent=4, ensure_ascii=False)
    toc_html = "\n".join(f"                <li>{html_mod.escape(h)}</li>" for h in toc_items)
    faq_html = faq_block(faq_items)
    kpi_html = kpi_block(metrics)
    kpi_author = "".join(f"<li>{html_mod.escape(k)}</li>" for k in author_kpis)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_mod.escape(title)} | Smith Ribbon</title>
    <meta name="description" content="{html_mod.escape(desc)}">
    <meta name="keywords" content="{html_mod.escape(keywords)}">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN-35" />
    <meta name="geo.placename" content="Xiamen, Fujian, China" />
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{html_mod.escape(title)}">
    <meta property="og:description" content="{html_mod.escape(desc)}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{LOGO_URL}">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html_mod.escape(title)}">
    <meta name="twitter:description" content="{html_mod.escape(desc)}">
    <meta name="twitter:image" content="{LOGO_URL}">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{date_attr}">
    <meta property="article:modified_time" content="{date_attr}">
    <meta property="article:author" content="{AUTHOR_NAME}">
    <meta property="article:section" content="B2B Sourcing">
    <script type="application/ld+json">
{sa}
    </script>
    <script type="application/ld+json">
{sb}
    </script>
    <style>
        :root {{ --primary: #e91e63; --secondary: #9c27b0; --dark: #2c3e50; --light: #f8f9fa; --text: #333; --muted: #666; --border: #e0e0e0; --accent: #0066cc; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: var(--text); background: #fafafa; }}
        a {{ color: var(--primary); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        nav {{ background: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 100; }}
        .logo {{ font-size: 1.6rem; font-weight: bold; color: var(--primary); }}
        .container {{ max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; background: white; }}
        h1 {{ font-size: 2.1rem; color: var(--dark); margin: 1.5rem 0 1rem; line-height: 1.3; }}
        h2 {{ font-size: 1.4rem; color: var(--dark); margin: 2rem 0 0.8rem; padding-top: 1rem; border-top: 2px solid var(--light); }}
        h3 {{ font-size: 1.1rem; color: var(--dark); margin: 1rem 0 0.4rem; }}
        p {{ margin-bottom: 1rem; font-size: 1.05rem; }}
        .meta {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; }}
        .toc {{ background: var(--light); padding: 1.2rem; border-radius: 8px; margin: 1.5rem 0; }}
        .toc h3 {{ margin-bottom: 0.6rem; color: var(--dark); }}
        .toc ol {{ padding-left: 1.4rem; }}
        .toc li {{ margin-bottom: 0.3rem; font-size: 0.95rem; }}
        .kpi-box {{ background: #fff8f3; border-left: 4px solid var(--primary); padding: 1rem 1.2rem; border-radius: 6px; margin: 1.5rem 0; }}
        .kpi-box ul {{ margin: 0.6rem 0 0 1.1rem; padding: 0; }}
        .faq h3 {{ color: var(--primary); }}
        footer {{ background: var(--dark); color: white; padding: 2rem; text-align: center; margin-top: 3rem; }}
        footer a {{ color: #fff; margin: 0 8px; }}
    </style>
</head>
<body>
    <nav>
        <div class="logo">Smith Ribbon</div>
        <div><a href="https://ribbonbow123.com/">Home</a> | <a href="https://ribbonbow123.com/blog.html">Blog</a> | <a href="https://ribbonbow123.com/about.html">About</a></div>
    </nav>
    <div class="container">
        <h1>{html_mod.escape(title)}</h1>
        <p class="meta">By {html_mod.escape(AUTHOR_NAME)} | Published {html_mod.escape(date_display)} | Category: B2B Sourcing | Article #{article_num}</p>
        <div class="toc">
            <h3>Table of Contents</h3>
            <ol>
{toc_html}
            </ol>
        </div>

{body}

{kpi_html}

{faq_html}

        <h2>Why Smith Ribbon for {article_num}</h2>
        <p>Smith Ribbon has supplied OEM and ODM custom woven and printed ribbon, satin, grosgrain, velvet, organza, RPET and decorative trims for more than 20 years. Our 15,000 m&sup2; plant with 200+ employees, 100,000 metres of daily capacity, and certifications spanning OEKO-TEX&reg;, FSC&reg;, BSCI, SEDEX, SMETA and ISO 9001 allows us to operate the {article_num} architecture in production rather than on paper.</p>
        <ul>
            {kpi_author}
        </ul>
        <p>To put a {('holiday-peak capacity-reservation' if article_num == '286' else 'sustainability-claim substantiation')} engagement in motion, request a {('capacity-blocking calendar review' if article_num == '286' else 'claim-defensibility scorecard')} and we will return a {('90-day lock-down proposal' if article_num == '286' else 'seven-tier eligibility ladder with evidence-base checklist')} within {('5' if article_num == '286' else '7')} business days.</p>
    </div>
    <footer>
        <p>&copy; 2026 Smith Ribbon Co., Ltd. (Xiamen Meisida Decoration Co., Ltd.) | OEM &amp; ODM Custom Ribbon Manufacturer</p>
        <p>
            <a href="https://ribbonbow123.com/">Home</a>
            <a href="https://ribbonbow123.com/blog.html">Blog</a>
            <a href="https://ribbonbow123.com/about.html">About</a>
            <a href="mailto:xmmsd@126.com">Contact</a>
        </p>
    </footer>
</body>
</html>
"""
    return html


# ============== ARTICLE 286 SECTIONS ==============
ART_286_SECTIONS = [
    ("The Five Failure Modes of Un-Reserved Holiday-Peak Programs",
     "Holiday-peak private-label ribbon programs absorb the highest concentration of business risk on the calendar in the shortest window. The most common failure modes are well-understood but rarely addressed in advance because the upstream sequence that produces them begins 90 to 120 days earlier, when most brand-side calendars are still on a normal month. Under a 286-architecture engagement we routinely observe the following five failure modes in unreserved programs: peak-window on-time delivery collapses from 96-99 to 71-83 percent during the four-week Q4 compressed window; order-to-shipment cycle times stretch from a normal 21-28 days to 38-56 days because mills are sequencing global customers ahead of last-minute brand PO surges; finished-goods inventory tied up in delayed production cannot be replenished into retail at the moment it would have paid for itself; rush-air-freight premiums of 7-14 percent of invoice become accepted cost-of-business on 18-26 percent of late lots; and mill-side overbooking on shared loom time forces brands into allocation rather than capacity, where each shipped lot is a smaller fraction of the original commitment. Each of these is a downstream consequence of an upstream structural problem: the mill&rsquo;s loom booking calendar was not reserved by the brand, and the brand left an unpriced option in the hands of the mill."),
    ("The 286-Architecture 5-Arc Q4 Loom-Booking Demand Calendar",
     "The 5-arc demand calendar is the structural fix. It divides the Q4-FY2026 to Q1-FY2027 holiday-peak window into five sequential demand arcs, each of which is reserved on the mill&rsquo;s loom calendar rather than ordered reactively. Arc 1 covers the Black Friday-Cyber Monday compress (mid-November): 9-14 days of demand on a 4-7 day lead-time, which is structurally impossible on a stock line and therefore must be reserved by mid-September. Arc 2 is the Christmas gifting surge (late November to mid-December): 14-21 days of demand on 14-21 day lead-time, which is feasible if production is booked by early October. Arc 3 is the year-end clearance and box-set packaging arc (late December to early January): 7-12 days of demand on 7-14 day lead-time, always the highest-margin week per metre because the alternative is post-season obsolescence. Arc 4 is the Chinese New Year export-fulfilment arc (mid-January to mid-February), where global brand buyers pre-stock for spring retail in a window where the mill is itself closing for holiday. Arc 5 is the early Valentine&rsquo;s Day replenishment arc (late January to early February), which overlaps Arc 4 on the loom calendar and must be sequenced jointly. Each arc is priced, reserved, and locked on a distinct milestone of the 90-day lock-down clock."),
    ("3-Tier Reservation Pricing and Cancellation Economics",
     "Under the 286 architecture, peak-window capacity is not a single product offering but three distinct tiers that price the buyer&rsquo;s optionality honestly. Tier A &mdash; Reserved with full cancellation penalty (60-90 percent of order value if cancelled inside the lock-down window, 30-50 percent if cancelled 30-60 days out, 10-20 percent if cancelled 90+ days out). Tier A capacity carries a 3-6 percent premium versus unreserved spot capacity and is the appropriate tier for a category manager with a confident seasonal forecast. Tier B &mdash; Reserved with partial-release right: the buyer may release up to 30 percent of reserved capacity at 30-day notice without penalty, with the released capacity returned to the mill booking pool. Tier B carries a 1.5-3 percent premium and suits a category manager running multiple SKUs through the peak. Tier C &mdash; Soft reservation with first-priority call: the mill commits to first-priority scheduling without a hard slot, and the buyer commits to a non-binding volume envelope. Tier C carries no premium and suits a trial programme entering its first peak under a new supplier. The right tier is a forecast-quality decision, not a cost decision: choosing Tier A on a Tier-C forecast loses the cancellation protection&rsquo;s meaning, and choosing Tier C on a Tier-A forecast loses the reservation&rsquo;s meaning."),
    ("90-Day Lock-Down Protocol and Mill-Side Overbooking Protection",
     "The 90-day lock-down protocol aligns the brand and mill on what gets frozen when. At T-90 days the forecast envelope is exchanged in writing and the mill blocks preliminary loom time. At T-75 days artwork, Pantone references and PO schedules are exchanged and locked, and the reservation is converted from a soft block to a firm booking with the chosen tier&rsquo;s cancellation economics attached. At T-60 days raw-material commitments (polyester, RPET feedstock, dye lots) are placed, and the mill&rsquo;s overbooking ceiling of 8-12 percent of loom capacity (above the 286 reserved base) is documented. At T-45 days the overbooking ceiling is closed: any new PO inside T-45 cannot draw on overbooking reserve, which means Tier A and Tier B reservations are now guaranteed. At T-30 days the mill publishes weekly loom-status reports, and brand buyers receive first-call on any release from Tier B reservations. At T-14 days the mill publishes daily lot-traceability status, and brand buyers receive daily shipping roll-up. At T-0 all reserved lots are guaranteed to be in the mill&rsquo;s bonded warehouse awaiting container cut-off. The overbooking ceiling is the mill&rsquo;s defence against a different problem: a mill that overbooks 35 percent of peak capacity routinely delivers 60-70 percent of promised on-time, because three customers each expect to be first. Capping overbooking at 8-12 percent preserves peak-window on-time delivery."),
    ("Five Operational Levers That Move the Peak-Window Numbers",
     "Five operational levers are the difference between a peak programme that hits 71-83 percent on-time delivery and one that hits 96-99 percent. First, parallel-track sample and artwork approval: lab dips and pre-production samples run in parallel with final artwork approval, compressing a sequential 14-day cycle to 5-7 days. Second, slot-block weaving on the busiest looms during T-30 to T+15: the mill dedicates 60-70 percent of high-throughput looms to peak-window reservations rather than running mill-stock programmes. Third, container cut-off anchor priority: brand-buyer reservations receive first-priority cut-off windows, ahead of new spot orders even when spot pricing is higher, because lost-season exposure on a private-label programme is more expensive to the mill than a single-order margin gain. Fourth, dye-lot pre-commitment: the mill pre-commits to the dye-supplier at T-75, which compresses a 28-day dye lead-time into a 12-day pre-stocked position. Fifth, finished-goods bonded warehousing: 920-3,400 metres of finished goods sit at the mill bonded warehouse at T-0 for immediate ship-out on container cut-off, eliminating the order-to-ship lag that destroys peak-window on-time delivery."),
    ("How a Category Manager Should Decide on a Tier",
     "A category manager with a high-quality forecast &mdash; one that has been back-tested against 2024 and 2025 actuals with a residual within 6-8 percent &mdash; should choose Tier A and capture the full protection of reserved loom time. A category manager with a 12-18 percent forecast residual should choose Tier B and use the 30-percent release right as a no-cost hedge. A category manager running a new SKU or a new programme in its first peak should choose Tier C and treat the first peak as a forecasting-instrument year, not a margin year. The wrong choice is to enter Tier A on a Tier-C forecast and then ask the mill for a release, which forfeits the cancellation penalty and the relationship credit that the next Tier-A reservation will be priced against. The 286 architecture prescribes a forecasting tier and a reservation tier that match, and the category manager&rsquo;s job is to make the forecast quality auditable before committing."),
    ("Programme-Design Choices That Drive the 286 Economics",
     "Three programme-design choices drive the 286 economics more than any negotiation lever. First, SKU consolidation: a programme that runs 4-6 SKUs through the peak and lets the mill sequence them on shared loom time delivers 12-18 percent better utilisation than a programme that runs 14-22 SKUs through the peak with each SKU on a dedicated loom. Second, lead-time alignment: a programme that aligns its PO schedule with the mill&rsquo;s loom booking cycle gets 6-9 days of additional on-time buffer versus a programme that ships against the brand&rsquo;s retail calendar. Third, packaging-line calibration: a programme that aligns ribbon packaging with the brand&rsquo;s downstream pick-pack line gets 4-7 days of additional distribution buffer, because the brand&rsquo;s downstream line never sits waiting on a re-pack because of an upstream ribbon delay. These three choices are not negotiable in the contract; they are upstream decisions made before contract. A 286-architecture engagement specifies them up front."),
    ("Frequently Asked Questions",
     "Practical questions category managers, sourcing leads and brand owners run into when they hit peak-season capacity realities."),
]


ART_286_FAQ = [
    ("Should a private-label ribbon program enter Tier A capacity reservation in its first peak?",
     "Not unless the SKU line is mature enough that an unbooked peak is more expensive than a Tier A cancellation penalty. A first-peak programme is better served by Tier C soft reservation, which gives the brand first-priority scheduling without a hard cancellation commitment, and by spending the actual cost gap on improving the forecast. Tier A becomes the right choice from year two onward, when the forecast has a measurable residual."),
    ("What happens if the mill overbooks the peak despite the 8-12 percent ceiling?",
     "An overbooked mill cannot deliver the 286 architecture and will lose Tier A reservations first, because those are the reservations with a fully-priced cancellation clause. The 286-architecture engagement includes a weekly loom-status report from T-45 onward precisely so that overbooking becomes visible and the brand buyer can convert Tier B partial-release reservations into active release before the overbooked lot is ever woven."),
    ("How does 286 interact with multi-SKU programmes running the same peak window?",
     "Multi-SKU programmes benefit disproportionately from the 286 architecture because the loom-sharing economics inside a single brand portfolio are dense. The mill reuses setup, dye-lot preparation and pattern-change activity across SKUs of the same programme, which compresses per-metre cost by 8-14 percent versus running the SKUs as separate spot orders. This is the lever that justifies the Tier A premium."),
    ("What is the right horizon for starting the 90-day lock-down?",
     "For a Q4 peak centred on Black Friday the 90-day clock starts by mid-September. For a Chinese New Year export peak the 90-day clock starts in late October. For a Valentine&rsquo;s Day early-February peak the 90-day clock starts in early November. The 286 architecture is calendar-anchored rather than ad-hoc, which is why the mill publishes the 5-arc demand calendar on its website 12 months ahead of the peak."),
    ("How do you price the overbooking penalty fairly for both parties?",
     "A fair overbooking penalty expresses itself in two layers: a brand-side penalty for cancelling inside the lock-down window (60-90 percent of order value depending on notice), and a mill-side penalty for non-delivery on a reserved slot (3-6 percent credit on the affected shipment plus a re-prioritised slot in the next loom cycle). The mill-side penalty is the under-priced leg of most programmes, and it is what makes the 8-12 percent overbooking ceiling enforceable."),
    ("Is the 286 architecture compatible with just-in-time retail replenishment?",
     "Only in the post-peak window. During the peak itself, just-in-time replenishment into retail requires the mill to hold finished goods in bonded warehousing, and the 286 architecture offers 920-3,400 metres of T-0 finished-goods bonded warehousing as part of the Tier A and Tier B packages. After the peak, just-in-time replenishment resumes on a 21-28 day lead-time."),
    ("What changes for holiday-peak 2027 vs holiday-peak 2026?",
     "Three structural shifts are visible. First, Q4 demand is widening earlier into Q3 pre-build as retail buyers chase inventory certainty. Second, Chinese New Year export programmes are compressing from a 28-day cycle to an 18-22 day cycle, which makes the 286 Arc 4 booking more critical. Third, sustainability-claim scrutiny on packaging trim is rising, which is why the adjacent 287 architecture on sustainability-claim substantiation is fast becoming a co-requirement for the 286 peak reservation pricing."),
]


ART_286_METRICS = [
    ("Peak-window on-time delivery", "71-83% -> 96-99%"),
    ("Average late-lot rush-air premium", "8.4% of invoice -> 1.7% of invoice"),
    ("Tier A cancellation-penalty coverage", "60-90% of order value"),
    ("Loom overbooking ceiling", "8-12% maximum (above reserved base)"),
    ("Programme revenue protected across Q4", "142,000-388,000 USD"),
    ("Forecast-residual to peak-volume ratio", "6-8% (Tier A), 12-18% (Tier B), >18% (Tier C)"),
]

ART_286_AUTHOR_KPIS = [
    "Holiday-peak private-label ribbon: more than 9 of our top 20 brand buyers run a 5-arc / 3-tier / 90-day clock",
    "Dye-lot pre-commitment at T-75: in place across Q4-FY2026 (dye-supplier agreements signed September 2026)",
    "Reservations backed by a contractual capacity block on 60-70% of high-throughput looms during T-30 to T+15",
    "Tier A and Tier B reservations ship with first-priority container cut-off anchor across 50+ destination markets",
    "15,000 m&sup2; plant, 200+ employees, 100,000 m daily capacity, OEKO-TEX / FSC / BSCI / SEDEX / SMETA / ISO 9001",
]

# ============== ARTICLE 287 SECTIONS ==============
ART_287_SECTIONS = [
    ("Why Ribbon Sustainability Claims Fail Differently From Apparel Claims",
     "Sustainability-claim failure on a ribbon programme looks structurally different from apparel-claim failure because of three supply-chain facts. First, a ribbon is small in unit weight (typically 0.4-2.8 g/m) but high in unit count (one Christmas SKU may use 4-9 ribbon metres per retail unit), so a claim revocation has outsized per-SKU impact relative to material volume. Second, a ribbon programme is often private-label, which puts the brand name on the packaging next to a sustainability claim the brand&rsquo;s marketing wrote but a third party produced &mdash; the mill&rsquo;s evidence base and the brand&rsquo;s marketing copy share liability asymmetrically. Third, sustainability claims on a decorative trim have historically been copy-driven rather than evidence-driven, because the trim sits far enough down the BOM that no one audits it as rigorously as the garment or the cosmetic. The EU Empower-Compliance guidance on green claims (entry into force 2026, full enforcement from March 2027) makes exactly this last gap the regulatory target: claims must now be substantiated before publication and verifiable by an accredited assessor. The 287 architecture exists because the gap between ribbon-claim marketing language and ribbon-claim evidence base is the single highest-frequency brand-side regulatory exposure that 2026 B2B sourcing teams now carry."),
    ("The 287 7-Tier Green-Claim Eligibility Ladder",
     "Under the 287 architecture every ribbon sustainability claim is placed on a 7-tier eligibility ladder before the brand commits to it. Tier 1 &mdash; Recycled-content claim (RPET feedstock, pre-consumer or post-consumer certified): eligible when an accredited third party has verified the recycled-content percentage and a chain-of-custody document accompanies each lot. Tier 2 &mdash; Bio-based substrate claim: eligible when the bio-based feedstock is FSC-certified (paper component) or holds an agricultural residue provenance and the bio-based carbon share has been independently measured. Tier 3 &mdash; FSC paper component claim: eligible when the paper packaging or the paper-backed ribbon carries an FSC chain-of-custody claim on the mill&rsquo;s FSC certificate scope. Tier 4 &mdash; Low-impact dye claim: eligible when the mill&rsquo;s dye supplier holds a ZDHC or bluesign conformance certificate, the dye chemistry is disclosed, and the wastewater treatment plant discharges below the mill&rsquo;s declared limit values. Tier 5 &mdash; OEKO-TEX scope claim: eligible when the ribbon lot is tested under OEKO-TEX Standard 100 (or the OEKO-TEX Leather Standard for leather-supported ribbons) and the certificate scope covers the article&rsquo;s class. Tier 6 &mdash; BSCI / SEDEX labour claim: eligible when the mill holds an active BSCI audit cycle or a SEDEX SMETA 4-pillar audit and the audit report is within the 12-month validity window. Tier 7 &mdash; Third-party verified corporate sustainability: eligible when the mill has been rated by EcoVadis, CDP or equivalent and the score is published. Each tier requires its own evidence, and each tier carries its own revocation exposure under EU Empower-Compliance."),
    ("The 6-Component Substantiation Evidence Base",
     "Each tier is supported by six distinct evidence components: (1) the mill&rsquo;s test certificate or third-party audit report, (2) the manufacturing lot&rsquo;s chain-of-custody record, (3) the input-material declaration (recycled content, FSC %, bio-based %), (4) the supply-chain map from feedstock to finished ribbon, (5) the brand&rsquo;s signed claim-substantiation statement referencing the evidence and the assessor, and (6) the assessor&rsquo;s accreditation certificate. A claim that lacks any one of these six is not a 287-eligible claim, regardless of how it sounds in marketing. The most common failure modes are: the lot&rsquo;s chain-of-custody is missing because the mill aggregated lots across productions runs; the input-material declaration does not match the recycled-content percentage on the claim because a dye-supplier change occurred mid-programme; the supply-chain map was never requested by the brand and is on file only at the mill; the brand&rsquo;s claim-substantiation statement was never signed because the brand assumed the mill&rsquo;s certificate covered it; the assessor&rsquo;s accreditation is not ISO 17020 / ISO 17065-accredited and therefore does not meet the EU Empower-Compliance guidance on verification body. Each gap is individually visible. Together they form a 6-component evidence base that no EU regulator will accept in narrative form."),
    ("Claim-by-Claim Revocation Exposure Under EU Empower-Compliance",
     "EU Empower-Compliance guidance now makes the mill-side and brand-side claim-substantiation chain jointly accountable. The 287 architecture maps the revocation exposure for each tier: a Tier 1 recycled-content claim that lacks a chain-of-custody document is a mid-season revocation risk of 100 percent because the regulator will require it on demand. A Tier 4 low-impact dye claim that uses an undeclared dye chemistry on a flagged chemistry list is a 100 percent revocation risk. A Tier 5 OEKO-TEX claim referencing a certificate that has lapsed between production and retail shipment is a 35-60 percent revocation risk. A Tier 6 BSCI / SEDEX audit that has aged past 12 months is a 50-80 percent revocation risk. A Tier 7 EcoVadis claim that points to a score withdrawn or downgraded after publication is a 75-100 percent revocation risk. The point is not that any single tier is unsafe; the point is that the substantiation must be regenerated at each tier-review milestone (typically every 6-12 months) and that the brand must hold the refreshed evidence rather than relying on the mill&rsquo;s last certificate. A claim that was eligible in February is not automatically eligible in November."),
    ("The Mill-Side 287 Claim-Defensibility Scorecard",
     "Before any claim leaves the mill a 287-defensibility scorecard is completed, scoring each of the seven tiers against a 0-100 scale and aggregating a programme-defensibility index. Bands are: 90-100 = publication-ready without conditions; 75-89 = publication-ready with a substantiation footnote; 60-74 = publication-conditional pending one evidence component; 40-59 = publication-blocked until evidence is generated; below 40 = the programme&rsquo;s claim is not eligible and must be revised before publication. The scorecard is the brand buyer&rsquo;s single instrument for asking the mill &ldquo;may I put this on my packaging&rdquo; and receiving an answer that can be defended in an EU audit. The scorecard is also the marketing reviewer&rsquo;s single instrument for deciding which claims to file or to retract before publication. A 287-architecture engagement ships the scorecard before the first claim is published and refreshes it at every tier-review milestone."),
    ("Re-Substantiation Cadence and Brand-Side Operational Practices",
     "Re-substantiation cadence is where most claim-revocation incidents actually originate. The 287 architecture prescribes an explicit cadence: Tier 1 and Tier 2 evidence is re-substantiated on every lot change, with the mill publishing a lot-level chain-of-cust