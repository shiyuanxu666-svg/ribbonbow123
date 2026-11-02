#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 219-AM + 220-PM — 2026-09-30 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-30"

ART219 = {
    "file": "blog-ribbon-oem-b2b-219-module-mill-side-q1-2027-19-stage-oem-brief-to-shipment-workflow-artwork-rider-sample-parallel-track-ai-vision-inline-defect-detection-edi-cpq-vmi-brand-exit-protocol-architecture-b2b-oem-program-resilience-2026-09-30-am.html",
    "title": "Ribbon OEM B2B 219-Module Mill-Side Q1-2027 19-Stage OEM Brief-to-Shipment Workflow Artwork Rider Sample Parallel Track AI Vision Inline Defect Detection EDI CPQ VMI Brand-Exit Protocol Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 19-Stage OEM Brief-to-Shipment Workflow Artwork Rider Sample Parallel Track AI Vision Inline Defect Detection EDI CPQ VMI Brand-Exit Protocol Architecture",
    "date": TODAY,
    "desc": "219-module mill-side Q1-2027 19-stage OEM brief-to-shipment workflow architecture (end-to-end customization with artwork-rider parallel track compressing approval from 14-21 days to 5-7 days, sample-approval parallel track with ΔE 1.0/1.5/2.5 tolerance compression, AI-vision inline defect detection with edge-AI Jetson AGX Orin processor, EDI 850/855/856/810 + CPQ + VMI + API digital integration with SAP/Oracle/NetSuite ERP, 22-touchpoint brand-exit protocol, 7-pillar compounding NPI margin asset) for global brand procurement and Q1 2027 supply-chain controllers. Lift: 38-64% speed-to-shelf compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
}
ART220 = {
    "file": "blog-ribbon-oem-b2b-220-module-mill-side-q1-2027-23-stage-smart-specimen-co-design-portal-ai-visual-library-pantone-fhi-translation-engine-digital-twin-ai-augmented-color-stewardship-architecture-b2b-oem-program-resilience-2026-09-30-pm.html",
    "title": "Ribbon OEM B2B 220-Module Mill-Side Q1-2027 23-Stage Smart-Specimen Co-Design Portal AI Visual Library Pantone FHI Translation Engine Digital Twin AI-Augmented Color Stewardship Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 23-Stage Smart-Specimen Co-Design Portal AI Visual Library Pantone FHI Translation Engine Digital Twin AI-Augmented Color Stewardship Architecture",
    "date": TODAY,
    "desc": "220-module mill-side Q1-2027 23-stage smart-specimen co-design portal architecture (brand-buyer self-service configuration, 5,000-SKU AI visual library with ΔE-verified Pantone matching, Pantone FHI translation engine for cross-substrate paper/fabric/plastic/ceramic/metallic color translation, digital twin 3D pre-visualization across 12 product-context templates, AI-augmented color stewardship with closed-loop batch consistency, 7-pillar compounding co-design margin asset) for global brand procurement and Q1 2027 digital-transformation controllers. Lift: 38-64% speed-to-design compression, 4-11% landed-cost savings, 4-11% program-lifetime-margin-lift per year.",
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
    """Insert cards_text right after the first match of marker_regex."""
    m = re.search(marker_regex, html, flags=re.IGNORECASE)
    if not m:
        # fallback: insert right after </header>
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
    update_en_blog([ART219, ART220])
    print("--- Updating blog.html ---")
    update_blog([ART219, ART220])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART219, ART220])
    print("Done.")