#!/usr/bin/env python3
"""Update blog.html, en-blog.html, index.html and sitemap.xml for RB article #324 — 2026-10-29 PM.

Insert order: newest-first (published_time desc), so #324 goes above #322/#323.
"""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-29"

ART324 = {
    "file": ("blog-ribbon-oem-outdoor-apparel-trim-weatherproof-uv-cold-flex-abrasion-"
             "sun-rain-salt-performance-private-label-buyers-guide-2026-10-29-pm.html"),
    "title": ("Ribbon for Outdoor Apparel Trim &mdash; UV, Cold Flex, Abrasion, Salt and "
              "Weather Performance (2026)"),
    "cat": "Outdoor Apparel Performance Trim",
    "date": TODAY,
    "time": "15:00",
    "desc": ("Outdoor trim sees UV, freeze-thaw, abrasion, salt spray and repeated washing that "
              "indoor trims never face. Covers construction choice (polyester, nylon, reflective, "
              "backed and laminated), what each test method actually proves and does not prove, "
              "how to write a method-bound performance specification, and the failure modes that "
              "only appear after a season in the field."),
    "read": "19 min read",
}


def card_en(art, emoji_color):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji_color});">{emoji_color.replace("#","")}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ {art["read"]}</div>'
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
        f'  <div class="blog-meta">{art["date"]} &middot; {art["read"]}</div>\n'
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
    cards_to_add, changed = [], False
    for art in arts:
        if art["file"] in html:
            print(f"  EN-BLOG: {art['file']} already present")
            continue
        emoji_color = "#7b2cbf" if "-pm." in art["file"] else "#1abc9c"
        cards_to_add.append(card_en(art, emoji_color))
        changed = True
    if changed:
        updated = insert_at_top(html, "".join(cards_to_add), r'<div\s+class\s*=\s*["\']blog-grid["\']')
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
    cards_to_add, changed = [], False
    for art in arts:
        if art["file"] in html:
            print(f"  BLOG: {art['file']} already present")
            continue
        cards_to_add.append(card_blog(art))
        changed = True
    if changed:
        updated = insert_at_top(html, "".join(cards_to_add), r'<div\s+class\s*=\s*["\']blog-list["\']')
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
        idx = xml.rfind("</urlset>")
        if idx == -1:
            updated = xml + "\n".join(new_entries)
        else:
            updated = xml[:idx] + "".join(new_entries) + xml[idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED sitemap.xml with {len(new_entries)} new URL(s)")


def update_index(arts):
    path = os.path.join(WORK, "index.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    missing = [a for a in arts if a["file"] not in html]
    if not missing:
        print("  INDEX: article already linked")
        return
    for art in missing:
        print(f"  INDEX: {art['file']} not present - adding link block")
        link = (
            f'\n        <li><a href="{art["file"]}">{art["title"]}</a></li>\n'
        )
        m = re.search(r'(<ul[^>]*id="blog-links"[^>]*>)', html, flags=re.IGNORECASE)
        if not m:
            m = re.search(r'(<ul[^>]*class="[^"]*blog[^"]*"[^>]*>)', html, flags=re.IGNORECASE)
        if m:
            html = html[:m.end()] + link + html[m.end():]
        else:
            print("    (no blog link list marker found - appending to end of body)")
            html = html.replace("</body>", link + "</body>")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  UPDATED index.html with {len(missing)} new link(s)")


if __name__ == "__main__":
    arts = [ART324]  # newest first
    print("--- Updating en-blog.html ---")
    update_en_blog(arts)
    print("--- Updating blog.html ---")
    update_blog(arts)
    print("--- Updating index.html ---")
    update_index(arts)
    print("--- Updating sitemap.xml ---")
    update_sitemap(arts)
    print("Done.")
