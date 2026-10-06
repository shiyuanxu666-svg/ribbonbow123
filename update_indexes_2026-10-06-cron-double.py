#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 236-AM + 237-PM — 2026-10-06 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-06"

ART236 = {
    "file": "blog-ribbon-oem-b2b-236-module-mill-side-q1-2027-22-stage-oem-cost-analysis-should-cost-modeling-19-component-quote-decoder-hidden-landed-cost-reverse-engineering-architecture-b2b-oem-program-resilience-2026-10-06-am.html",
    "title": "Ribbon OEM B2B 236-Module Mill-Side Q1-2027 22-Stage OEM Cost-Analysis Should-Cost Modeling 19-Component Quote-Decoder Hidden-Landed-Cost Reverse-Engineering Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 22-Stage OEM Cost Analysis Should Cost Modeling 19 Component Quote Decoder Hidden Landed Cost Reverse Engineering Architecture",
    "date": TODAY,
    "desc": "236-module mill-side Q1-2027 22-stage OEM cost-analysis should-cost modeling 19-component quote-decoder hidden-landed-cost reverse-engineering architecture (7-pillar cognitive fabric Hidden-Landed-Cost Reverse-Engineering 19-Component Quote-Decoder Plane + AI-Augmented Hidden-Cost Radar Variable-Cost-Modeling Plane + Multi-Currency FX-Hedging Forward-Contract Plane + Cross-Border Tariff-Engineering Country-of-Origin Plane + Volume-Mix Optimization SKU-Rationalization Plane + Carbon-Adjusted-TCO Scope-3-Plane + Supplier-Certification-Compliance Decoder Plane, 19-component yarn-cost dye-cost weave-cost finish-cost package-cost overhead-cost tariff-cost freight-cost FX-cost MOQ-cost tooling-cost should-cost baseline, 22-component hidden-cost decoder yarn/dye/weave/finish/package/overhead/tariff/freight/FX/MOQ/tooling/certification, 22-stage quote-to-margin cognitive-fabric mill-side smart-mill IIoT Edge-AI cost-decoder 14-photo-evidence stack 7-year ISO-9001-aligned retention, AI-augmented hidden-cost radar variable-cost-modeling volume-mix optimization supplier-relationship-management SRM tiered-QBR-cadence) for global brand owners and Q1 2027 controllers. Lift: 38-64% unit-economics-leak compression, 4-11% margin lift per quote, 4-11% program-lifetime-margin-lift.",
}
ART237 = {
    "file": "blog-ribbon-oem-b2b-237-module-mill-side-q1-2027-24-stage-oem-supplier-selection-factory-audit-certification-compliance-decoder-25-credential-roi-architecture-b2b-oem-program-resilience-2026-10-06-pm.html",
    "title": "Ribbon OEM B2B 237-Module Mill-Side Q1-2027 24-Stage OEM Supplier-Selection Factory-Audit Certification-Compliance Decoder 25-Credential ROI Architecture for Brand Owners and Procurement Managers",
    "cat": "Q1-2027 24-Stage OEM Supplier Selection Factory Audit Certification Compliance Decoder 25 Credential ROI Architecture",
    "date": TODAY,
    "desc": "237-module mill-side Q1-2027 24-stage OEM supplier-selection factory-audit certification-compliance decoder 25-credential ROI architecture (7-pillar cognitive fabric 25-Credential ROI Decoder Plane + AI-Augmented Supplier-Scorecard Plane + Tier-1-Tier-2-Tier-3 Supplier-Resilience Plane + Cross-Border Tariff-Engineering Country-of-Origin Plane + 14-Station On-Site Factory-Audit Qualification Plane + Hidden-Landed-Cost Reverse-Engineering 19-Component Quote-Decoder Plane + Supplier-Relationship-Management SRM Tiered-QBR-Cadence Vendor-Lifecycle Governance plane, 24-credential OEKO-TEX-100 BSCI SEDEX-SMETA FSC GRS-RPET GOTS ISO-9001-14001-45001 ZDHC REACH-CPSIA-Prop-65 WRAP-RBA-ICSA C2C-Gold tender-RFP ROI baseline, 24-stage credential-to-tender cognitive-fabric mill-side 14-station on-site factory-audit qualification 14-photo-evidence stack 7-year ISO-9001-aligned retention, AI-augmented supplier-scorecard supplier-risk-tiering tier-1-tier-2-tier-3 dual-sourcing bridge-order-migration) for global brand owners and Q1 2027 controllers. Lift: 38-64% tender-RFP cycle-time compression, 4-11% credential-pass-rate lift per tender, 4-11% program-lifetime-margin-lift.",
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
    update_en_blog([ART236, ART237])
    print("--- Updating blog.html ---")
    update_blog([ART236, ART237])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART236, ART237])
    print("Done.")