#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with article 223 PM — 2026-09-30 cron 15:00."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-30"

ART223 = {
    "file": "blog-ribbon-oem-b2b-223-module-mill-side-q1-2027-25-stage-ai-vision-inline-defect-detection-closed-loop-yield-recovery-pareto-engine-edge-ai-jetson-agx-orin-mill-side-yield-improvement-architecture-b2b-oem-program-resilience-2026-09-30-pm.html",
    "title": "Ribbon OEM B2B 223-Module Mill-Side Q1-2027 25-Stage AI Vision Inline Defect Detection Closed-Loop Yield-Recovery Pareto-Engine Architecture Edge-AI Jetson AGX Orin 64-Core Mill-Side Yield-Improvement B2B OEM Program Resilience",
    "cat": "Q1-2027 25-Stage AI Vision Inline Defect Detection Closed-Loop Yield-Recovery Pareto-Engine Architecture Edge-AI Jetson AGX Orin 64-Core Mill-Side Yield-Improvement Architecture",
    "date": TODAY,
    "desc": "223-module mill-side Q1-2027 25-stage AI vision inline defect detection closed-loop yield-recovery pareto-engine architecture (edge-AI-Jetson-AGX-Orin 64-core processor with 4K-CMOS 120-fps inline defect detection at 99.2 percent sensitivity, pareto-defect-stream-engineering with top-5 defect categories 80/20 rule and root-cause 5-why fishbone-diagram SPC, OEE tracking Availability × Performance × Quality target 85-92 percent, AQL-2.5 final-inspection with claim-rate ≤0.3 percent vs industry-baseline 2.0 percent, pre-shipment-AQL-photo-evidence with 4K-photo per SKU per lot, COPQ reduction target ≤0.8 percent vs industry-baseline 4.0 percent, 7-pillar compounding yield-recovery margin asset) for global brand procurement and Q1 2027 operations controllers. Lift: 38-64 percent yield-recovery lift, 4-11 percent landed-cost savings, 4-11 percent program-lifetime-margin-lift per year.",
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
        emoji_color = "#7b2cbf" if "pm" in art["file"] else "#1abc9c"
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
            updated = xml + "\n".join(new_entries)
        else:
            updated = xml[:idx] + "".join(new_entries) + xml[idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED sitemap.xml with {len(new_entries)} new URL(s)")


if __name__ == "__main__":
    print("--- Updating en-blog.html ---")
    update_en_blog([ART223])
    print("--- Updating blog.html ---")
    update_blog([ART223])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART223])
    print("Done.")