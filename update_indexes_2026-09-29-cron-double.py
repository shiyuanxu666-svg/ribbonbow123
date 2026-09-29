#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 217-AM + 218-PM — 2026-09-29 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-29"

ART217 = {
    "file": "blog-ribbon-oem-b2b-217-module-mill-side-q1-2027-oem-cost-engineering-22-component-should-cost-19-component-landed-cost-multi-currency-fx-hedging-architecture-b2b-oem-program-resilience-2026-09-29-am.html",
    "title": "Ribbon OEM B2B 217-Module Mill-Side Q1-2027 OEM Cost-Engineering 22-Component Should-Cost 19-Component Landed-Cost Multi-Currency FX-Hedging Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 OEM Cost-Engineering 22-Component Should-Cost 19-Component Landed-Cost Multi-Currency FX-Hedging Architecture",
    "date": TODAY,
    "desc": "217-module mill-side Q1-2027 OEM cost-engineering architecture (22-component should-cost model decoder from yarn-forward to shipment, 19-component tariff-aware landed-cost basket, 7-instrument multi-currency FX-hedging stack covering USD/EUR/GBP/JPY/AUD/CAD/CNY, 7-stream country-of-origin & FTA-utilization decoder, 18-tier supplier tiering with mill-side variable-cost transparency, 7-pillar compounding margin asset delivering 4-11% program-lifetime-margin-lift) for global brand procurement and Q1 2027 finance controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART218 = {
    "file": "blog-ribbon-oem-b2b-218-module-mill-side-q1-2027-22-credential-retailer-tender-certification-compliance-decoder-bsci-sedex-smeta-oeko-tex-fsc-grs-gots-sbti-cdp-csrd-esrs-e1-roi-architecture-b2b-oem-program-resilience-2026-09-29-pm.html",
    "title": "Ribbon OEM B2B 218-Module Mill-Side Q1-2027 22-Credential Retailer-Tender Certification Compliance Decoder BSCI SEDEX SMETA OEKO-TEX FSC GRS GOTS SBTi CDP CSRD ESRS E1 ROI Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 22-Credential Retailer-Tender Certification Compliance Decoder BSCI SEDEX SMETA OEKO-TEX FSC GRS GOTS SBTi CDP CSRD ESRS E1 ROI Architecture",
    "date": TODAY,
    "desc": "218-module mill-side Q1-2027 22-credential retailer-tender certification compliance architecture (22-credential decoder across 6 buckets with credential-ROI weighting, OEKO-TEX 25-product-class chemical-residue screening, BSCI/SEDEX SMETA 4-pillar dual-audit acceptance, FSC/GRS/GOTS chain-of-custody for recycled & organic materials, SBTi/CDP/CSRD ESRS E1 8-framework decarbonization disclosure, Walmart/Target/Costco/Sephora retailer-vendor-manual mapping, 7-pillar compounding retailer-tender margin asset) for global brand procurement and Q1 2027 retail-compliance controllers. Lift: 38-64% supply-disruption compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
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


def insert_at_top(html, new_cards):
    pattern = re.compile(r'(<article\s+class="blog-card">)', re.IGNORECASE)
    matches = list(pattern.finditer(html))
    if matches:
        first = matches[0]
        return html[:first.start()] + new_cards + html[first.start():]

    pattern2 = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m2 = pattern2.search(html)
    if m2:
        return html[:m2.end()] + "\n" + new_cards + html[m2.end():]

    pat3 = re.compile(r'(<ul\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
    m3 = pat3.search(html)
    if m3:
        return html[:m3.end()] + "\n" + new_cards + html[m3.end():]

    return html.replace("</body>", new_cards + "\n</body>")


def update_en_blog(arts):
    path = os.path.join(WORK, "en-blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    emojis = ["#1abc9c", "#d4367c"]
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        card = card_en(art, emojis[i % len(emojis)])
        if art["file"] in html:
            print(f"  EN: {art['file']} already in en-blog.html")
            continue
        cards_to_add.append(card)
        changed = True
    if changed:
        new_cards_text = "\n".join(cards_to_add)
        updated = insert_at_top(html, new_cards_text)
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
        card = card_blog(art)
        if art["file"] in html:
            print(f"  BLOG: {art['file']} already in blog.html")
            continue
        cards_to_add.append(card)
        changed = True
    if changed:
        new_cards_text = "".join(cards_to_add)
        updated = insert_at_top(html, new_cards_text)
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
    update_en_blog([ART217, ART218])
    print("--- Updating blog.html ---")
    update_blog([ART217, ART218])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART217, ART218])
    print("Done.")