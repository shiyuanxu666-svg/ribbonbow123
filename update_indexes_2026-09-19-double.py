#!/usr/bin/env python3
"""Update en-blog.html, blog.html and sitemap.xml with articles 179-AM + 180-PM — 2026-09-19 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-19"

ART179 = {
    "file": "blog-ribbon-oem-b2b-179-module-mill-side-q1-2027-should-cost-reverse-engineering-24-component-quote-decoder-yarn-dye-weave-finish-package-overhead-architecture-b2b-oem-program-resilience-2026-09-19-am.html",
    "title": "Ribbon OEM B2B 179-Module Mill-Side Q1-2027 Should-Cost Reverse-Engineering 24-Component Quote Decoder Yarn-Dye-Weave-Finish-Package-Overhead",
    "cat": "Q1-2027 Should-Cost Reverse-Engineering 24-Component Quote Decoder",
    "date": TODAY,
    "desc": "179-module should-cost reverse-engineering 24-component quote decoder (20-stage yarn cost stack, 18-stage dye-house chemical-energy-water cost stack, 16-stage weave-knit-loom productivity cost stack, 14-stage finish-finishing cost stack, 12-stage packaging cost stack, 10-stage overhead cost stack, 8-stage tariff-aware landed-cost, 6-stage FX-hedging, 4-stage payment-term TVM, 2-stage carbon-adjusted TCO) for global brand procurement and Q1-2027 finance controllers. Lift: 24-38% quote gap closure, 18-27% landed-cost reduction, 12-19pp margin uplift.",
}
ART180 = {
    "file": "blog-ribbon-oem-b2b-180-module-mill-side-q1-2027-oem-end-to-end-customization-process-21-stage-decoder-brief-artwork-color-tooling-sampling-ppap-shipment-ramp-architecture-b2b-oem-program-resilience-2026-09-19-pm.html",
    "title": "Ribbon OEM B2B 180-Module Mill-Side Q1-2027 OEM End-to-End Customization Process 21-Stage Decoder Brief-Artwork-Color-Tooling-Sampling-PPAP-Shipment-Ramp",
    "cat": "Q1-2027 OEM End-to-End Customization 21-Stage Process Decoder",
    "date": TODAY,
    "desc": "180-module OEM end-to-end customization 21-stage process decoder (19-stage brief-to-artwork handoff, 17-stage artwork-to-color translation, 15-stage color-to-tooling, 13-stage tooling-to-sampling, 11-stage sampling-to-PPAP, 9-stage PPAP-to-shipment, 7-stage retailer-onboarding, 5-stage shelf-life-cycle-management) for global brand merchandising and Q1-2027 OEM-orchestration. End: 38-52% faster brief-to-shipment, 22-34pp FPA lift, 14-23% defect-rate reduction.",
}


def card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 42 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def card_blog(art, emoji):
    return (
        f'<article class="blog-post-card" data-category="{art["cat"]}">\n'
        f'  <a href="{art["file"]}" class="blog-post-thumb" style="background:linear-gradient(135deg,#1a5276,{emoji});" aria-label="{art["title"][:60]}"></a>\n'
        f'  <div class="blog-post-content">\n'
        f'    <span class="blog-post-category">{art["cat"]}</span>\n'
        f'    <h3 class="blog-post-title"><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'    <div class="blog-post-meta">📅 {art["date"]} · ⏱ 42 min read</div>\n'
        f'    <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'    <a href="{art["file"]}" class="blog-post-link">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


def insert_after_grid(html, new_cards):
    """Insert new blog cards right after the first <div class="...posts-grid..." opening."""
    pattern = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m = pattern.search(html)
    if m:
        return html[:m.end()] + "\n" + new_cards + html[m.end():]
    pat2 = re.compile(r'(<ul\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
    m2 = pat2.search(html)
    if m2:
        return html[:m2.end()] + "\n" + new_cards + html[m2.end():]
    pat3 = re.compile(r'(<div\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
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
    emojis = ["#d4367c", "#1abc9c"]
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        if art["file"] in html:
            print(f"{art['file']} already in en-blog.html — skipping")
            continue
        cards_to_add.append(card_en(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_after_grid(html, "\n".join(cards_to_add))
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
    emojis = ["#d4367c", "#1abc9c"]
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        if art["file"] in html:
            print(f"{art['file']} already in blog.html — skipping")
            continue
        cards_to_add.append(card_blog(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_after_grid(html, "\n".join(cards_to_add))
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
    arts = [ART179, ART180]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)