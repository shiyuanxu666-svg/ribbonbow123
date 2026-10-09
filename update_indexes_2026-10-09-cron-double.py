#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 248-AM + 249-PM — 2026-10-09 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-09"

ART248 = {
    "file": "blog-ribbon-oem-b2b-248-module-mill-side-q1-2027-oem-custom-branded-ribbon-concept-to-shelf-24-stage-brief-to-shipment-workflow-architecture-b2b-oem-program-resilience-2026-10-09-am.html",
    "title": "Ribbon OEM B2B 248-Module Mill-Side Q1-2027 24-Stage OEM Custom-Branded Ribbon Concept-to-Shelf Brief-to-Shipment Workflow Architecture for Brand Buyers and Procurement Managers",
    "cat": "Q1-2027 24 Stage OEM Custom Branded Ribbon Concept To Shelf Brief To Shipment Workflow Architecture",
    "date": TODAY,
    "desc": "248-module mill-side Q1-2027 24-stage OEM custom-branded ribbon concept-to-shelf brief-to-shipment workflow architecture (24-stage across concept-to-stage-gate-0 brief-lock-artwork-start-Pantone-triage, sample-to-tooling-stage-gate-1 lab-dip-strike-off-cylinder-engrave-die-cut, pre-production-stage-gate-2 PPAP-bulk-yarn-dye-lot-greige-weave-finish, inline-quality-and-capacity-stage-gate-3 inline-AOI-cut-sew-finish-lines-pack, lab-test-and-compliance-stage-gate-4 OEKO-TEX-REACH-CPSIA-RSL-DPP, ship-and-restock-stage-gate-5 pre-shipment-AQL-container-pack-EDI-VMI-handoff) for global brand owners and Q1 2027 brand-buyer procurement managers. Lift: 22-36 day speed-to-shelf compression, 14-28 percent tender-win-rate lift, 38k-142k USD avoidable-cost recovery.",
}
ART249 = {
    "file": "blog-ribbon-oem-b2b-249-module-mill-side-q1-2027-oem-supplier-selection-cost-analysis-25-signal-12-kpi-framework-architecture-b2b-oem-program-resilience-2026-10-09-pm.html",
    "title": "Ribbon OEM B2B 249-Module Mill-Side Q1-2027 25-Signal 12-KPI OEM Supplier Selection Cost-Analysis Framework Architecture for Brand Buyers and Procurement Managers",
    "cat": "Q1-2027 25 Signal 12 KPI OEM Supplier Selection Cost Analysis Framework Architecture",
    "date": TODAY,
    "desc": "249-module mill-side Q1-2027 25-signal 12-KPI OEM supplier selection cost-analysis framework architecture (25-signal across direct-cost-reverse-engineering yarn-dye-weave-finish-conversion, hidden-cost-quality-defect rework-AQL-chargeback-air-freight, cross-border-trade-compliance HS-code-Section-301-FTA-drawback-FTZ, working-capital-FX-financing FX-hedge-payment-terms-DSO-supply-chain-finance, risk-ESG-brand-equity supplier-risk-scope-3-cert-compliance-brand-equity mapped to 12-KPI tender-eval scorecard) for global brand owners and Q1 2027 finance controllers. Lift: 14-28 percent tender-win-rate lift, 18-42 percent hidden-landed-cost uncovered, 38-142k USD avoidable-premium recovery.",
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
    update_en_blog([ART248, ART249])
    print("--- Updating blog.html ---")
    update_blog([ART248, ART249])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART248, ART249])
    print("Done.")
