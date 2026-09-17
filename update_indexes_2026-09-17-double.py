#!/usr/bin/env python3
"""Update en-blog.html, blog.html and sitemap.xml with articles 172-AM + 173-PM — 2026-09-17 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-17"

ART172 = {
    "file": "blog-ribbon-oem-b2b-172-module-brand-buyer-q1-2027-private-label-ribbon-oem-total-cost-of-ownership-tco-decoder-25-component-quote-reverse-engineering-architecture-b2b-oem-program-resilience-2026-09-17-am.html",
    "title": "Ribbon OEM B2B 172-Module Brand-Buyer Q1-2027 Private-Label Ribbon OEM TCO Decoder 25-Component Quote Reverse-Engineering",
    "cat": "Q1-2027 Private-Label TCO Decoder 25-Component Quote Reverse-Engineering",
    "date": TODAY,
    "desc": "172-module TCO decoder (25-component quote reverse-engineering stack, 21-stage should-cost modeling, 19-stage hidden-cost-radar, 17-stage FX-hedging, 15-stage tariff-aware landed-cost, 13-stage volume-mix MOQ tiering, 11-stage carbon-adjusted TCO, 9-stage supplier benchmark, 7-stage quote line-item, 5-stage freight-and-duties, 3-stage payment-term TVM) for global brand procurement and Q1-2027 finance controllers. Lift: 18-26% TCO gap closure, 12-18% landed-cost reduction, 8-14% margin uplift.",
}
ART173 = {
    "file": "blog-ribbon-oem-b2b-173-module-mill-side-q1-2027-supplier-capacity-pre-booking-q4-cascade-supplier-mix-tier-1-2-3-supplier-resilience-architecture-b2b-oem-program-resilience-2026-09-17-pm.html",
    "title": "Ribbon OEM B2B 173-Module Mill-Side Q1-2027 Q4 Cascade Supplier-Capacity Pre-Booking Tier-1-2-3 Supplier-Resilience",
    "cat": "Q1-2027 Q4 Cascade Supplier-Capacity Pre-Booking Tier-1-2-3 Supplier-Resilience",
    "date": TODAY,
    "desc": "173-module Q4 cascade supplier-capacity pre-booking (23-stage pre-booking workflow, 19-stack tier-1-2-3 supplier-mix engine, 17-stage Q4-cascade capacity-lock, 15-stage holiday-peak simulator, 13-stage supplier-financial-health, 11-stage supplier-quality scorecard, 9-stage supplier OTIF, 7-stage bridge-order migration, 5-stage capacity-risk heat-map, 3-stage tariff-and-FX-aware pre-booking). End: 80-92% peak-season OTIF, 60-78% capacity-reservation coverage, 20-32% overtime-and-air-freight avoidance.",
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
    """Insert new blog cards right after the first <div class=\"...posts-grid...\" opening."""
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
    arts = [ART172, ART173]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)
