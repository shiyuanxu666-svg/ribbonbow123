#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 191-AM + 192-PM — 2026-09-23 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-23"

ART191 = {
    "file": "blog-ribbon-oem-b2b-191-module-mill-side-q1-2027-hs-code-digitization-fta-utilization-origin-documentation-dpp-traceability-architecture-b2b-oem-program-resilience-2026-09-23-am.html",
    "title": "Ribbon OEM B2B 191-Module Mill-Side Q1-2027 HS-Code Digitization FTA-Utilization Origin-Documentation DPP-Ready Traceability Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 HS-Code Digitization FTA-Utilization Origin-Documentation DPP-Ready Traceability Architecture",
    "date": TODAY,
    "desc": "191-module mill-side Q1-2027 HS-code digitization FTA-utilization origin-documentation DPP-ready traceability architecture (9-stage HS-code digitization engine, 9-stage FTA-utilization maximization ladder, 9-stage origin-documentation discipline, 9-stage DPP-ready traceability bundle, 9-stage AI-augmented HS-code classification, 9-stage tariff-engineering tied-in, 9-stage inbound-customs-clearance automation, 9-stage inbound-logistics-cost engineering, 9-stage trade-compliance-cadence closeout) for global brand procurement and Q1-2027 customs-trade-compliance officers. Lift: 38-64% customs-clearance-cycle compression, 4-11% landed-cost savings lift, 4-11% program-lifetime-margin-lift per year.",
}
ART192 = {
    "file": "blog-ribbon-oem-b2b-192-module-mill-side-q1-2027-ai-vision-inline-defect-detection-closed-loop-yield-recovery-oee-pareto-architecture-b2b-oem-program-resilience-2026-09-23-pm.html",
    "title": "Ribbon OEM B2B 192-Module Mill-Side Q1-2027 AI-Vision Inline Defect-Detection Closed-Loop Yield-Recovery OEE-Dashboard Pareto-Engine Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 AI-Vision Inline Defect-Detection Closed-Loop Yield-Recovery OEE-Dashboard Pareto-Engine Architecture",
    "date": TODAY,
    "desc": "192-module mill-side Q1-2027 AI-vision inline defect-detection closed-loop yield-recovery OEE-dashboard Pareto-engine architecture (9-stage AI-vision inline defect-detection ladder, 9-stage closed-loop yield-recovery system, 9-stage defect-Pareto engine, 9-stage OEE dashboard, 9-stage inline-color-Delta-E closed loop, 9-stage inline-tension-and-speed control, 9-stage AOI auto-reject and rework workflow, 9-stage pre-shipment-inspection auto-stack, 9-stage yield-and-quality continuous-improvement closeout) for global brand procurement and Q1-2027 supply-chain-resilience officers. Lift: 38-64% defect-rate compression, 4-11% first-pass-yield lift, 4-11% program-lifetime-margin-lift per year.",
}


def card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 26 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def card_blog(art, emoji):
    return (
        f'<article class="blog-card">\n'
        f'  <span class="blog-tag">{art["cat"]}</span>\n'
        f'  <h3><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="blog-meta">{art["date"]} &middot; 26 min read</div>\n'
        f'</article>\n\n'
    )


def insert_at_top(html, new_cards):
    """Find best insertion point - the most recent blog-card article block."""
    # Pattern A: Insert before the first existing blog-card article
    pattern = re.compile(r'(<article\s+class="blog-card">)', re.IGNORECASE)
    matches = list(pattern.finditer(html))
    if matches:
        first = matches[0]
        return html[:first.start()] + new_cards + html[first.start():]

    # Pattern B: posts-grid
    pattern2 = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m2 = pattern2.search(html)
    if m2:
        return html[:m2.end()] + "\n" + new_cards + html[m2.end():]

    # Pattern C: blog-list ul/div
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
        if art["file"] in html:
            print(f"{art['file']} already in en-blog.html — skipping")
            continue
        cards_to_add.append(card_en(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_at_top(html, "\n".join(cards_to_add))
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"UPDATED {path} ({len(cards_to_add)} cards)")
    elif not changed:
        print(f"en-blog.html: no changes")


def update_blog_html(arts):
    path = os.path.join(WORK, "blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    emojis = ["#1abc9c", "#d4367c"]
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        if art["file"] in html:
            print(f"{art['file']} already in blog.html — skipping")
            continue
        cards_to_add.append(card_blog(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_at_top(html, "\n".join(cards_to_add))
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"UPDATED {path} ({len(cards_to_add)} cards)")
    elif not changed:
        print(f"blog.html: no changes")


def update_sitemap(arts):
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        sm = f.read()
    changed = False
    for art in arts:
        if art["file"] in sm:
            print(f"{art['file']} already in sitemap.xml — skipping")
            continue
        block = (
            "  <url>\n"
            f"    <loc>{BASE}/{art['file']}</loc>\n"
            f"    <lastmod>{art['date']}</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.85</priority>\n"
            "  </url>\n"
        )
        sm = sm.replace("</urlset>", block + "</urlset>")
        changed = True
        print(f"INSERTED {art['file']} into sitemap.xml")
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(sm)


if __name__ == "__main__":
    arts = [ART191, ART192]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)