"""Update en-blog.html, blog.html and sitemap.xml with the two new articles (154, 155) - 2026-09-13."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-13"

ART154 = {
    "file": "blog-ribbon-oem-b2b-154-module-mill-side-q1-2027-digital-integration-sap-erp-edi-api-order-orchestration-architecture-b2b-oem-program-resilience-2026-09-13-am.html",
    "title": "Ribbon OEM B2B 154-Module: Mill-Side Q1-2027 Digital-Integration (SAP/ERP/EDI/API) & Order-Orchestration Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 Digital Integration",
    "date": "2026-09-13",
    "desc": "17-tier ERP-coverage matrix + 15-stage PO-orchestration + 13-stage ASN-EDI + 11-stage VMI-CPQ-API + 9-stage invoice-E-invoicing-EDI + 7-stage label-pack data + 5-stage cartonization + 3-stage RMA. Compress order-touch-cost 23-41%, PO-ack 38-64%, lift OTIF 5-12pp.",
}

ART155 = {
    "file": "blog-ribbon-oem-b2b-155-module-mill-side-q1-2027-product-carbon-footprint-pcf-verified-lca-labeling-architecture-b2b-oem-program-resilience-2026-09-13-pm.html",
    "title": "Ribbon OEM B2B 155-Module: Mill-Side Q1-2027 Product-Carbon-Footprint (PCF) & Verified-LCA Labeling Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 PCF & Verified-LCA",
    "date": "2026-09-13",
    "desc": "19-stage cradle-to-gate LCA + 15-tier PCF-claim substantiation + 13-tier verified-labeling scheme + 11-stage Scope-3 inventory + 9-stage PEF/OEF + 7-stage DPP data model + 5-stage LCA peer-review + 3-stage carbon-label. Hit 18-38% PCF reduction, 9-22% premium, 5-14pp ESG lift.",
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
    """For the larger blog.html (uses different markup)."""
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

    has153 = "b2b-153" in html
    has154 = "b2b-154" in html
    print(f"Existing b2b-153 in en-blog.html: {has153}, b2b-154: {has154}")
    if has154:
        print("b2b-154 already in en-blog.html, skipping")
        return

    new_cards = build_card_en(ART154, "#2a9d8f") + "\n" + build_card_en(ART155, "#7b2cbf") + "\n"
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

    if "b2b-154" in html:
        print("b2b-154 already in blog.html, skipping")
        return

    new_cards = build_card_blog_html(ART154, "#2a9d8f") + "\n" + build_card_blog_html(ART155, "#7b2cbf") + "\n"
    new_html = insert_into_grid(html, new_cards, "blog-post")
    if new_html is None:
        # Try with alternative markup
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

    for art in (ART154, ART155):
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
