"""Update en-blog.html, blog.html and sitemap.xml with the two new articles (156, 157) - 2026-09-13."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-13"

ART156 = {
    "file": "blog-ribbon-oem-b2b-156-module-mill-side-q1-2027-ai-augmented-design-color-stewardship-architecture-b2b-oem-program-resilience-2026-09-13-am.html",
    "title": "Ribbon OEM B2B 156-Module: Mill-Side Q1-2027 AI-Augmented Design & Color-Stewardship Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 AI Design & Color-Stewardship",
    "date": "2026-09-13",
    "desc": "17-stage AI-aided design-render + 15-tier Pantone-FHI-CxF color-library + 13-stage virtual lab-dip + 11-stage spectral-Delta-E closed-loop + 9-stage 3D-woven-ribbon preview + 7-stage artwork-rider + 5-stage digital-twin swatch + 3-stage buyer co-design portal. Compress design-cycle 21-44%, sample-cost 31-58%, lift first-shot-right 6-13pp.",
}

ART157 = {
    "file": "blog-ribbon-oem-b2b-157-module-mill-side-q1-2027-brand-to-mill-digital-thread-traceability-architecture-b2b-oem-program-resilience-2026-09-13-pm.html",
    "title": "Ribbon OEM B2B 157-Module: Mill-Side Q1-2027 Brand-to-Mill Digital-Thread Traceability Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 Digital-Thread Traceability",
    "date": "2026-09-13",
    "desc": "19-stage brand-to-mill digital-thread + 15-tier GS1-128/GTIN-14/RFID/NFC tag-stack + 13-stage yarn-to-slit-lot genealogy + 11-stage blockchain-anchored provenance + 9-stage recall-readiness drill + 7-stage multi-stakeholder ledger + 5-stage tamper-evident seal + 3-stage DPP handoff. Compress recall-latency 27-49%, audit-cost 24-56%, lift ESG-trace 4-11pp.",
}


def build_card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 26-27 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def build_card_blog_html(art, emoji):
    """For the larger blog.html (uses different markup)."""
    return (
        f'<article class="blog-post-card" data-category="{art["cat"]}">\n'
        f'  <a href="{art["file"]}" class="blog-post-thumb" style="background:linear-gradient(135deg,#1a5276,{emoji});" aria-label="{art["title"][:60]}"></a>\n'
        f'  <div class="blog-post-content">\n'
        f'    <span class="blog-post-category">{art["cat"]}</span>\n'
        f'    <h3 class="blog-post-title"><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'    <div class="blog-post-meta">📅 {art["date"]} · ⏱ 26-27 min read</div>\n'
        f'    <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'    <a href="{art["file"]}" class="blog-post-link">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


def insert_into_grid(html, new_cards, marker_substring):
    """Insert new_cards at the start of the first blog-grid block in html, after marker_substring exists."""
    if marker_substring in html:
        # Find the opening of the blog-grid after the marker
        m = re.search(r'(<div class="blog-grid">)', html)
        if m:
            grid_start = m.end()
            return html[:grid_start] + "\n" + new_cards + html[grid_start:]
    return None


def update_en_blog():
    path = os.path.join(WORK, "en-blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    has155 = "b2b-155" in html
    has156 = "b2b-156" in html
    print(f"Existing b2b-155 in en-blog.html: {has155}, b2b-156: {has156}")
    if has156:
        print("b2b-156 already in en-blog.html, skipping")
        return

    new_cards = build_card_en(ART156, "#2a9d8f") + "\n" + build_card_en(ART157, "#7b2cbf") + "\n"
    new_html = insert_into_grid(html, new_cards, "b2b-")
    if new_html is None:
        print("ERROR: could not find blog-grid in en-blog.html")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"UPDATED {path}  (added 2 cards at top of grid)")


def update_blog_html():
    """Update the larger blog.html (the original ribbonbow123 blog index)."""
    path = os.path.join(WORK, "blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    if "b2b-156" in html:
        print("b2b-156 already in blog.html, skipping")
        return

    new_cards = build_card_blog_html(ART156, "#2a9d8f") + "\n" + build_card_blog_html(ART157, "#7b2cbf") + "\n"
    new_html = insert_into_grid(html, new_cards, "blog-post")
    if new_html is None:
        m = re.search(r'(<div\s+class="posts-grid")', html) or re.search(r'(<ul\s+class="blog-list")', html) or re.search(r'(<div\s+class="blog-list")', html)
        if m:
            grid_start = m.end()
            new_html = html[:grid_start] + ">\n" + new_cards + html[grid_start:]
    if new_html is None:
        print(f"WARNING: could not find grid in blog.html, falling back to manual injection before </body>")
        new_html = html.replace("</body>", new_cards + "\n</body>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"UPDATED {path}  (added 2 cards)")


def update_sitemap():
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        sm = f.read()

    for art in (ART156, ART157):
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
        print(f"INSERTED into sitemap.xml: {art['file']}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(sm)
    print(f"UPDATED {path}")


if __name__ == "__main__":
    update_en_blog()
    update_blog_html()
    update_sitemap()
