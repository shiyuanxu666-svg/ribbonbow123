"""Update en-blog.html, blog.html and sitemap.xml with the two new articles (159, 160) - 2026-09-14."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-14"

ART159 = {
    "file": "blog-ribbon-oem-b2b-159-module-mill-side-q1-2027-smart-specimen-co-design-portal-architecture-b2b-oem-program-resilience-2026-09-14-am.html",
    "title": "Ribbon OEM B2B 159-Module: Mill-Side Q1-2027 Smart-Specimen & Co-Design Portal Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 Smart-Specimen & Co-Design Portal",
    "date": "2026-09-14",
    "desc": "19-stage smart-specimen QR-RFID-NFC tag-stack + 15-tier multi-stakeholder co-design portal + 13-stage color-and-finish shared decision room + 11-stage artwork-versioning audit ledger + 9-stage live-pricing feedback + 7-stage brand-buyer-mill co-approval + 5-stage digital-twin swatch + 3-stage co-branded rights-clearance. Compress approval-cycle 24-47%, sample-logistics 28-55%, lift co-design first-shot-right 7-14pp.",
}

ART160 = {
    "file": "blog-ribbon-oem-b2b-160-module-mill-side-q1-2027-esg-marketing-claims-substantiation-green-premium-pricing-architecture-b2b-oem-program-resilience-2026-09-14-pm.html",
    "title": "Ribbon OEM B2B 160-Module: Mill-Side Q1-2027 ESG-Marketing-Claims Substantiation & Green-Premium Pricing Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 ESG-Claims Substantiation & Green-Premium Pricing",
    "date": "2026-09-14",
    "desc": "17-stage ESG-claims substantiation audit chain + 15-tier CSRD-ESRS-SASB-GRI disclosure mapping + 13-stage green-premium pricing model + 11-stage verified-PCF-LCA-boundary + 9-stage rPET-recycled-bio-yarn verification + 7-stage third-party certification chain-of-custody + 5-stage greenwashing-prevention legal-review gate + 3-stage green-premium retail-price pass-through test. Lift green-premium margin 19-42%, cut marketing-claim disputes 27-54%, lift ESG-trace score 6-12pp.",
}


def build_card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 27-28 min read</div>'
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
        f'    <div class="blog-post-meta">📅 {art["date"]} · ⏱ 27-28 min read</div>\n'
        f'    <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'    <a href="{art["file"]}" class="blog-post-link">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


def insert_into_grid(html, new_cards, marker_substring):
    """Insert new_cards at the start of the first blog-grid block in html, after marker_substring exists."""
    if marker_substring in html:
        m = re.search(r'(<div class="blog-grid">)', html)
        if m:
            grid_start = m.end()
            return html[:grid_start] + "\n" + new_cards + html[grid_start:]
    return None


def update_en_blog():
    path = os.path.join(WORK, "en-blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    has159 = "b2b-159" in html
    has160 = "b2b-160" in html
    print(f"Existing b2b-159 in en-blog.html: {has159}, b2b-160: {has160}")
    if has159 and has160:
        print("Both articles already in en-blog.html, skipping")
        return

    new_cards = build_card_en(ART159, "#2a9d8f") + "\n" + build_card_en(ART160, "#7b2cbf") + "\n"
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

    if "b2b-159" in html and "b2b-160" in html:
        print("Both articles already in blog.html, skipping")
        return

    new_cards = build_card_blog_html(ART159, "#2a9d8f") + "\n" + build_card_blog_html(ART160, "#7b2cbf") + "\n"
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

    for art in (ART159, ART160):
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
