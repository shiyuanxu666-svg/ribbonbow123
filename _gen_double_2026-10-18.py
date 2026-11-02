#!/usr/bin/env python3
"""Generate 2 B2B articles for ribbonbow123 (2026-10-18 AM/PM)
Article 273 AM: OEM Custom Branded Ribbon Manufacturing Process (22-stage RFQ-to-shipment)
Article 274 PM: OEM Ribbon Supplier Selection & Cost Engineering (19-signal scorecard + TCO)
"""
import os
import json
from datetime import datetime
from pathlib import Path

DIR = "/workspace/ribbonbow123"
SITE = "ribbonbow123.com"

ART_AM_NUM = "273"
ART_AM_SLUG = "oem-custom-branded-ribbon-manufacturing-process-22-stage-rfq-to-shipment-mill-side-b2b-procurement-buyers-2026"
ART_AM_TITLE = "OEM Custom Branded Ribbon Manufacturing Process: The 22-Stage RFQ-to-Shipment B2B Procurement Playbook for Brand Buyers and Private-Label Merchandisers (2026)"
ART_AM_DESC = "A 2026 B2B procurement playbook detailing the 22-stage OEM custom-branded ribbon manufacturing process from RFQ to shipment. Built for global brand procurement managers, private-label merchandisers, retail sourcing coordinators, and gift-industry wholesale buyers sourcing OEM/ODM custom ribbon from China and Asia. Covers artwork spec, Pantone FHI color approval, lab-dip loop, PPAP, pre-shipment AQL 2.5 inspection, VMI hub-and-spoke replenishment, EU DPP/ESPR traceability, OEKO-TEX/BSCI/SEDEX documentation, freight booking, and customs clearance. Engineered to compress first-PO cycle 14 to 32 days, lift first-pass color-match from 71 to 94 percent, and recover 32,000 to 96,000 USD in avoidable Q1 2027 cost across the FY2026 to FY2028 horizon."
ART_AM_KEYWORDS = "OEM custom ribbon manufacturing, private label ribbon process, custom branded ribbon supplier, OEM ribbon RFQ process, ribbon Pantone FHI color approval, ribbon PPAP pre production approval, ribbon pre shipment AQL 2.5 inspection, OEM ribbon factory audit, ribbon VMI hub and spoke, custom printed ribbon wholesale, branded ribbon China factory, OEM ribbon minimum order quantity, ribbon mill lead time, custom ribbon artwork setup, B2B ribbon procurement 2026"

ART_PM_NUM = "274"
ART_PM_SLUG = "oem-ribbon-supplier-selection-cost-engineering-19-signal-scorecard-tariff-aware-tco-architecture-b2b-procurement-2026"
ART_PM_TITLE = "OEM Ribbon Supplier Selection and Cost Engineering: The 19-Signal Scorecard and Tariff-Aware TCO Architecture for B2B Procurement Buyers (2026)"
ART_PM_DESC = "A 2026 B2B supplier-selection and cost-engineering playbook for OEM ribbon procurement. Built for global brand procurement directors, retail private-label controllers, sourcing managers, and finance controllers evaluating Asia-based OEM ribbon mills. Covers the 19-signal multi-criteria decision matrix, the 22-component should-cost decoder, the 9-scenario landed-cost sensitivity heat-map (FX + tariff + EU CBAM carbon cost), HS-code digitization across 5806/5807/5808, FTA pathway mapping, supplier-financial-health tier-2/tier-3 12-signal disclosure, and dual-sourcing bridge-order migration. Engineered to lift supplier-quote transparency 38 to 64 percent, deliver 4 to 11 percent landed-cost savings, and recover 32,000 to 88,000 USD in FX-hedge and tariff-engineering recovery across the FY2026 to FY2028 horizon."
ART_PM_KEYWORDS = "OEM ribbon supplier selection, ribbon factory scorecard, ribbon supplier audit checklist, ribbon should cost analysis, ribbon landed cost tariff, ribbon OEM HS code 5806, ribbon country of origin FTA, ribbon supplier financial health, ribbon CBAM carbon adjusted cost, ribbon OEM minimum order quantity, ribbon factory China Vietnam, custom ribbon supplier comparison, ribbon supplier tier 1 tier 2 tier 3, B2B ribbon sourcing 2026"

DATE_AM = "2026-10-18T08:00:00+08:00"
DATE_PM = "2026-10-18T13:00:00+08:00"
DATE_AM_ISO = "2026-10-18"
DATE_PM_ISO = "2026-10-18"
AUTHOR_NAME = "Smith Ribbon Co., Ltd."
AUTHOR_URL = "https://ribbonbow123.com"
LOGO_URL = "https://ribbonbow123.com/img/banner.png"

# Sections will be loaded from external files to keep this Python script compact
# (we will read content from a JSON file later)

def build_html(article_num, slug, title, desc, keywords, date_iso, date_display, sections, date_attr):
    """Build a complete English B2B article HTML with meta/OG/Schema JSON-LD."""
    url = f"https://{SITE}/{slug}.html"
    sections_html = []
    for h2_title, paragraph in sections:
        sections_html.append(
            f'        <h2>{h2_title}</h2>\n'
            f'        <p>{paragraph}</p>'
        )
    body = "\n\n".join(sections_html)
    schema_article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {"@type": "Organization", "name": AUTHOR_NAME, "url": SITE},
        "datePublished": date_iso,
        "dateModified": date_iso,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}
    }
    schema_blog = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "image": LOGO_URL,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {
            "@type": "Organization",
            "name": AUTHOR_NAME,
            "logo": {"@type": "ImageObject", "url": LOGO_URL}
        },
        "datePublished": date_iso,
        "dateModified": date_iso,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": keywords,
        "articleSection": "B2B Sourcing",
        "wordCount": sum(len(p.split()) + len(h.split()) for h, p in sections) + 200
    }
    sa = json.dumps(schema_article, indent=4, ensure_ascii=False)
    sb = json.dumps(schema_blog, indent=4, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Smith Ribbon</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN-35" />
    <meta name="geo.placename" content="Xiamen, Fujian, China" />
    <link rel="canonical" href="{url}">
    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{LOGO_URL}">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{LOGO_URL}">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{date_attr}">
    <meta property="article:modified_time" content="{date_attr}">
    <meta property="article:author" content="{AUTHOR_NAME}">
    <meta property="article:section" content="B2B Sourcing">
    <!-- Article Schema -->
    <script type="application/ld+json">
{sa}
    </script>
    <script type="application/ld+json">
{sb}
    </script>
    <style>
        :root {{ --primary: #e91e63; --secondary: #9c27b0; --dark: #2c3e50; --light: #f8f9fa; --text: #333; --muted: #666; --border: #e0e0e0; --accent: #0066cc; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: var(--text); background: #fafafa; }}
        a {{ color: var(--primary); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        nav {{ background: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 100; }}
        .logo {{ font-size: 1.6rem; font-weight: bold; color: var(--primary); }}
        .container {{ max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; background: white; }}
        h1 {{ font-size: 2.2rem; color: var(--dark); margin: 1.5rem 0 1rem; line-height: 1.3; }}
        h2 {{ font-size: 1.4rem; color: var(--dark); margin: 2rem 0 0.8rem; padding-top: 1rem; border-top: 2px solid var(--light); }}
        p {{ margin-bottom: 1rem; font-size: 1.05rem; }}
        .meta {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; }}
        .toc {{ background: var(--light); padding: 1.2rem; border-radius: 8px; margin: 1.5rem 0; }}
        .toc h3 {{ margin-bottom: 0.6rem; color: var(--dark); }}
        .toc ol {{ padding-left: 1.4rem; }}
        .toc li {{ margin-bottom: 0.3rem; font-size: 0.95rem; }}
        footer {{ background: var(--dark); color: white; padding: 2rem; text-align: center; margin-top: 3rem; }}
        footer a {{ color: #fff; margin: 0 8px; }}
    </style>
</head>
<body>
    <nav>
        <div class="logo">Smith Ribbon</div>
        <div><a href="https://ribbonbow123.com/">Home</a> | <a href="https://ribbonbow123.com/blog.html">Blog</a> | <a href="https://ribbonbow123.com/about.html">About</a></div>
    </nav>
    <div class="container">
        <h1>{title}</h1>
        <p class="meta">By {AUTHOR_NAME} | Published {date_display} | Category: B2B Sourcing | Article #{article_num}</p>
        <div class="toc">
            <h3>Table of Contents</h3>
            <ol>
{chr(10).join(f'                <li>{h}</li>' for h, _ in sections)}
            </ol>
        </div>
{body}
    </div>
    <footer>
        <p>&copy; 2026 Smith Ribbon Co., Ltd. (Xiamen Meisida Decoration Co., Ltd.) | OEM & ODM Custom Ribbon Manufacturer</p>
        <p>
            <a href="https://ribbonbow123.com/">Home</a>
            <a href="https://ribbonbow123.com/blog.html">Blog</a>
            <a href="https://ribbonbow123.com/about.html">About</a>
            <a href="mailto:xmmsd@126.com">Contact</a>
        </p>
    </footer>
</body>
</html>
"""
    return html


def main():
    # Load AM sections
    am_json = Path("/tmp/am_sections.json")
    pm_json = Path("/tmp/pm_sections.json")
    if not am_json.exists() or not pm_json.exists():
        print("Missing sections JSON files. Run the section writer first.")
        return
    am_sections = json.loads(am_json.read_text())
    pm_sections = json.loads(pm_json.read_text())

    os.chdir(DIR)

    am_filename = f"blog-{ART_AM_SLUG}.html"
    am_html = build_html(ART_AM_NUM, ART_AM_SLUG, ART_AM_TITLE, ART_AM_DESC, ART_AM_KEYWORDS,
                         DATE_AM_ISO, "October 18, 2026 (08:00 CST)", am_sections, DATE_AM)
    Path(am_filename).write_text(am_html)
    print(f"Wrote {am_filename}")

    pm_filename = f"blog-{ART_PM_SLUG}.html"
    pm_html = build_html(ART_PM_NUM, ART_PM_SLUG, ART_PM_TITLE, ART_PM_DESC, ART_PM_KEYWORDS,
                         DATE_PM_ISO, "October 18, 2026 (13:00 CST)", pm_sections, DATE_PM)
    Path(pm_filename).write_text(pm_html)
    print(f"Wrote {pm_filename}")

if __name__ == "__main__":
    main()
