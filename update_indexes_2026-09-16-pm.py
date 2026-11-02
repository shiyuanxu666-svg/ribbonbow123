"""Update en-blog.html, blog.html and sitemap.xml with article 169 — 2026-09-16 PM slot."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-16"

ART169 = {
    "file": "blog-ribbon-oem-b2b-169-module-mill-side-q1-2027-digital-twin-smart-mill-iot-edge-closed-loop-yield-oee-energy-water-carbon-productivity-architecture-b2b-oem-program-resilience-2026-09-16-pm.html",
    "title": "Ribbon OEM B2B 169-Module: Mill-Side Q1-2027 Digital-Twin Smart-Mill IoT-Edge Closed-Loop Yield OEE Energy-Water-Carbon Productivity Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 Smart-Mill IoT-Edge Closed-Loop Productivity",
    "date": "2026-09-16",
    "desc": "19-stage digital-twin smart-mill IoT-edge closed-loop yield workflow + 15-sensor IIoT edge-AI vision stack + 13-stage OEE energy-water-carbon productivity scorecard + 11-stage predictive-maintenance trigger + 9-stage SCADA-MES-ERP integration + 7-stage yield-loss Pareto engine + 5-stage cradle-to-gate carbon-adjusted yield + 3-stage closed-loop APC color-delta-E tolerance. Lift OEE yield 21-39%, lift energy-water-carbon productivity 18-34%, improve first-pass-acceptance 9-19pp.",
}


def build_card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 27 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def build_card_blog_html(art, emoji):
    return (
        f'<article class="blog-post-card" data-category="{art["cat"]}">\n'
        f'  <a href="{art["file"]}" class="blog-post-thumb" style="background:linear-gradient(135deg,#1a5276,{emoji});" aria-label="{art["title"][:60]}"></a>\n'
        f'  <div class="blog-post-content">\n'
        f'    <span class="blog-post-category">{art["cat"]}</span>\n'
        f'    <h3 class="blog-post-title"><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'    <div class="blog-post-meta">📅 {art["date"]} · ⏱ 27 min read</div>\n'
        f'    <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'    <a href="{art["file"]}" class="blog-post-link">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


def insert_into_grid(html, new_cards, marker_class):
    """Insert new blog cards right after the first `<div class="posts-grid"` opening."""
    pattern = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m = pattern.search(html)
    if not m:
        return None
    insert_at = m.end()
    return html[:insert_at] + "\n" + new_cards + html[insert_at:]


def update_en_blog():
    path = os.path.join(WORK, "en-blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    if ART169["file"] in html:
        print(f"{ART169['file']} already in en-blog.html — skipping")
        return
    card = build_card_en(ART169, "#1abc9c") + "\n"
    new_html = insert_into_grid(html, card, "posts-grid")
    if new_html is None:
        m = re.search(r'(<div\s+class="blog-?)', html, re.IGNORECASE)
        if m:
            new_html = html[:m.end()] + "\n" + card + html[m.end():]
    if new_html is None:
        new_html = html.replace("</body>", card + "\n</body>")
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"UPDATED {path}")


def update_blog_html():
    path = os.path.join(WORK, "blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    if ART169["file"] in html:
        print(f"{ART169['file']} already in blog.html — skipping")
        return
    new_cards = build_card_blog_html(ART169, "#1abc9c") + "\n"
    pattern = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m = pattern.search(html)
    new_html = None
    if m:
        new_html = html[:m.end()] + "\n" + new_cards + html[m.end():]
    if new_html is None:
        m = re.search(r'(<ul\s+class="blog-list)|(<div\s+class="blog-list)', html, re.IGNORECASE)
        if m:
            new_html = html[:m.end()] + ">\n" + new_cards + html[m.end():]
    if new_html is None:
        new_html = html.replace("</body>", new_cards + "\n</body>")
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"UPDATED {path}")


def update_sitemap():
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        sm = f.read()
    if ART169["file"] in sm:
        print(f"{ART169['file']} already in sitemap.xml — skipping")
        return
    block = (
        "  <url>\n"
        f"    <loc>{BASE}/{ART169['file']}</loc>\n"
        f"    <lastmod>{ART169['date']}</lastmod>\n"
        "    <changefreq>weekly</changefreq>\n"
        "    <priority>0.85</priority>\n"
        "  </url>\n"
    )
    sm = sm.replace("</urlset>", block + "</urlset>")
    with open(path, "w", encoding="utf-8") as f:
        f.write(sm)
    print(f"UPDATED {path} (inserted {ART169['file']})")


if __name__ == "__main__":
    update_en_blog()
    update_blog_html()
    update_sitemap()
