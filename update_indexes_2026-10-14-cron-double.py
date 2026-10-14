#!/usr/bin/env python3
"""Update blog.html, en-blog.html and sitemap.xml with articles 263-AM + 264-PM — 2026-10-14 cron double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-14"

ART263 = {
    "file": "blog-ribbon-oem-b2b-263-module-mill-side-q1-2027-oem-factory-procurement-guide-22-station-on-site-qualification-24-signal-brand-buyer-tender-readiness-decoder-architecture-b2b-oem-program-resilience-2026-10-14-am.html",
    "title": "Ribbon OEM B2B 263-Module Mill-Side Q1-2027 22-Station OEM Factory-Procurement-Guide On-Site Qualification 24-Signal Brand-Buyer Tender-Readiness Decoder Architecture for Brand Buyers and Procurement Managers",
    "cat": "Q1-2027 22 Station OEM Factory Procurement Guide On Site Qualification 24 Signal Brand Buyer Tender Readiness Decoder Architecture",
    "date": TODAY,
    "desc": "263-module mill-side Q1-2027 22-station OEM factory-procurement-guide on-site qualification 24-signal brand-buyer tender-readiness decoder architecture for global brand owners and Q1 2027 tender-RFP response teams. Lift: 14-28 day factory-procurement cycle compression, 22-38 percent supplier-qualification pass-rate lift, 24-42 percent tender-win-rate lift, 56k-218k USD avoidable-cost recovery.",
}
ART264 = {
    "file": "blog-ribbon-oem-b2b-264-module-mill-side-q1-2027-oem-should-cost-modeling-23-component-quote-decoder-25-signal-supplier-selection-framework-architecture-b2b-oem-program-resilience-2026-10-14-pm.html",
    "title": "Ribbon OEM B2B 264-Module Mill-Side Q1-2027 23-Component OEM Should-Cost-Modeling Quote-Decoder 25-Signal Supplier-Selection Framework Architecture for Brand Buyers and Procurement Managers",
    "cat": "Q1-2027 23 Component OEM Should Cost Modeling Quote Decoder 25 Signal Supplier Selection Framework Architecture",
    "date": TODAY,
    "desc": "264-module mill-side Q1-2027 23-component OEM should-cost-modeling quote-decoder 25-signal supplier-selection framework architecture for global brand owners and Q1 2027 finance controllers. Lift: 12-26 percent gross-margin lift, 14-32 percent supplier-selection-cycle compression, 48k-192k USD avoidable-cost recovery.",
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
    update_en_blog([ART263, ART264])
    print("--- Updating blog.html ---")
    update_blog([ART263, ART264])
    print("--- Updating sitemap.xml ---")
    update_sitemap([ART263, ART264])
    print("Done.")