#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 253-AM + 254-PM — 2026-10-10 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-10"

ART253 = {
    "file": "blog-ribbon-oem-b2b-253-module-mill-side-q1-2027-oem-tariff-engineering-28-lever-country-of-origin-landed-cost-optimization-architecture-b2b-oem-program-resilience-2026-10-10-am.html",
    "title": "Ribbon OEM B2B 253-Module Mill-Side Q1-2027 28-Lever OEM Tariff-Engineering Country-of-Origin Landed-Cost Optimization Architecture for Brand Buyers and Procurement Managers",
    "cat": "Q1-2027 28 Lever OEM Tariff Engineering Country Of Origin Landed Cost Optimization Architecture",
    "date": TODAY,
    "desc": "253-module mill-side Q1-2027 28-lever OEM tariff-engineering country-of-origin landed-cost optimization architecture (28-lever across direct-tariff-engineering HS-code-Section-301-List-4A-4B-EU-CBAM-MFN-anti-dumping-safeguard-retaliatory, country-of-origin-diversification 21-country benchmark bonded-warehouse-FTZ, FTA-utilization RCEP-CPTPP-USMCA-EU-Mercosur-EU-Vietnam-EU-Singapore-EU-Korea-EU-Japan-ASEAN-AfCFTA-cumulation, FX-hedging multi-currency-forward-netting, working-capital-supply-chain-finance reverse-factoring-receivables-discounting-forfaiting-ESG-linked-finance) for global brand owners and Q1 2027 finance controllers. Lift: 22-46 percent Section-301 / EU-CBAM duty-exposure compression, 28-64 percent FTA-utilization savings lift, 56k-246k USD avoidable-cost recovery.",
}
ART254 = {
    "file": "blog-ribbon-oem-b2b-254-module-mill-side-q1-2027-oem-supplier-certification-26-credential-roi-decoder-hidden-cost-radar-architecture-b2b-oem-program-resilience-2026-10-10-pm.html",
    "title": "Ribbon OEM B2B 254-Module Mill-Side Q1-2027 26-Credential OEM Supplier-Certification ROI Decoder Hidden-Cost Radar Architecture for Brand Buyers and Procurement Managers",
    "cat": "Q1-2027 26 Credential OEM Supplier Certification ROI Decoder Hidden Cost Radar Architecture",
    "date": TODAY,
    "desc": "254-module mill-side Q1-2027 26-credential OEM supplier-certification ROI decoder hidden-cost radar architecture (26-credential across mill-side-compliance OEKO-TEX-GOTS-GRS-RCS-BCI-BSCI-SEDEX-SMETA-ISO-9001-14001, brand-buyer-tender FSC-OCS-ZDHC-MRSL-REACH-SVHC-CPSIA-Prop-65-RSL-Zero-UKCA-CE, tier-2-tier-3-sub-supplier WRAP-RBA-ICSA-C2C-Gold-Cradle-to-Cradle-Platinum, ESG-disclosure SBTi-CDP-CSRD-ESRS-E1-DPP-ESPR) for global brand owners and Q1 2027 retailer-tender program owners. Lift: 14-28 day audit-cycle compression, 18-32 percent tender-Win-rate lift, 62k-246k USD avoidable-cost recovery.",
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
    update_en_blog([ART253, ART254])
    print("--- Updating blog.html ---")
    update_blog([ART253, ART254])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART253, ART254])
    print("Done.")
