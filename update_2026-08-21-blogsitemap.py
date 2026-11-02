#!/usr/bin/env python3
"""Update en-blog.html and sitemap.xml for 2026-08-21 AM + PM articles."""
import os, re

BASE = "/workspace/ribbonbow123"
DATE_ISO = "2026-08-21"

AM = {
    "slug": "blog-ribbon-oem-b2b-86-module-hidden-landed-cost-reverse-engineering-architecture-b2b-oem-program-resilience-2026-08-21-am",
    "category": "Hidden-Landed-Cost Reverse-Engineering Architecture",
    "short_title": "Ribbon OEM B2B 86-Module Hidden-Landed-Cost Reverse-Engineering Architecture for B2B OEM Program Resilience",
    "description": "A 2026 B2B ribbon OEM 86-module hidden-landed-cost reverse-engineering architecture for global brand owners, retail private-label directors, sourcing managers, and procurement transformation teams. Covers 22-component TCO reverse-engineering, 18-supplier-quote decoder, 14-freight-line, 12-tariff-engineering, 10-duty-drawback, 8-customs-broker, 6-port-staging, 4-bonded-warehouse, 16-currency-hedge, 8-carbon-adjuster, 6-ESG-premium, 4-quality-failure-cost, 12-NCR-cost, 8-AQL-failure, 4-chargeback-defense, 6-rework-cost, 4-scrap-recovery, 4-payment-terms-NPV, 4-incoterm-DDP-CIF-FOB, 4-insurance, 4-financing-cost, 4-MOQ-amortization, 4-tooling-amortization, 4-warehousing-carrying, 4-safety-stock, 4-obsolescence-write-off, 4-port-demurrage, 4-detention, 4-chassis-pool, 4-fuel-adjustment, 4-foreign-exchange-spread, 4-letter-of-credit-fee, 4-supplier-financing-cost, 4-replenishment-frequency-cost, 4-bundle-consolidation, 4-VMI-cost, 4-rejected-lot-fee, 4-vendor-managed-cost, 4-supplier-recovery, 4-Q4-peak-surcharge, 4-Q4-air-freight-surcharge, 4-Q4-fuel-surcharge, 4-Q4-bunker-surcharge, 4-Q4-congestion-surcharge, 4-Q4-carrier-PIB. Smith Ribbon runs this 86-module hidden-landed-cost reverse-engineering architecture on a 6.4M meter multi-brand ribbon program delivering 100% landed-cost transparency, 14-22% margin-lift, 26-38% total-cost reduction, and 0% surprise-chargeback.",
    "date_label": "August 21, 2026 &middot; 29 min read",
}

PM = {
    "slug": "blog-ribbon-oem-b2b-87-module-supplier-selection-certification-compliance-decoder-architecture-b2b-oem-program-resilience-2026-08-21-pm",
    "category": "Supplier-Selection Certification-Compliance Decoder Architecture",
    "short_title": "Ribbon OEM B2B 87-Module Supplier-Selection Certification-Compliance Decoder Architecture for B2B OEM Program Resilience",
    "description": "A 2026 B2B ribbon OEM 87-module supplier-selection certification-compliance decoder architecture for global brand owners, retail private-label directors, sourcing managers, and procurement transformation teams. Covers 14-station factory-audit, 12-credential decoder, 10-quality-system, 8-ESG-system, 6-traceability-system, 4-IP-protection, 6-finance-health, 4-bank-reference, 4-tax-compliance, 4-insurance-coverage, 4-cybersecurity, 4-data-protection, 4-information-security, 4-supply-chain-resilience, 4-sub-supplier-risk, 4-geographic-risk, 4-weather-risk, 4-political-risk, 4-tariff-risk, 4-currency-risk, 4-freight-risk, 4-capacity-risk, 4-lead-time-risk, 4-quality-risk, 4-AQL-capability, 4-color-capability, 4-print-capability, 4-finishing-capability, 4-tooling-capability, 4-sample-speed, 4-communication-cadence, 4-raci-governance, 4-knowledge-transfer, 4-knowledge-continuity, 4-cross-functional, 4-engineering-support, 4-design-support, 4-artwork-support, 4-color-mgmt, 4-Pantone-match, 4-Delta-E-capability, 4-color-fastness, 4-wash-fastness, 4-light-fastness, 4-rub-fastness, 4-ph-value, 4-azo-free, 4-formaldehyde-free, 4-OPL-claim, 4-recycled-content, 4-bio-degradable, 4-FSC-paper, 4-GRS-yarn. Smith Ribbon runs this 87-module supplier-selection certification-compliance decoder architecture on a 7.1M meter multi-brand ribbon program delivering 100% on-time-quality, 14-22% margin-lift, 0% surprise-fail, and 0% compliance-violation.",
    "date_label": "August 21, 2026 &middot; 30 min read",
}


def insert_card(art, slot):
    blog_path = os.path.join(BASE, "en-blog.html")
    with open(blog_path, "r", encoding="utf-8") as f:
        content = f.read()
    slot_label = "Morning" if slot == "am" else "Afternoon"
    time_str = "10:00" if slot == "am" else "15:00"
    card = f"""        <!-- {slot_label} Article - August 21, 2026 ({time_str} UTC) -->
        <article class="blog-card">
            <span class="blog-tag">{art['category']}</span>
            <h3><a href="{art['slug']}.html">{art['short_title']}</a></h3>
            <p>{art['description'][:240]}...</p>
            <div class="blog-meta">{art['date_label']}</div>
        </article>

"""
    if f"{art['slug']}.html" in content:
        print(f"  [skip] {art['slug']}.html already in en-blog.html")
        return
    hero_match = re.search(r'(<section class="blog-hero">)', content)
    if not hero_match:
        raise RuntimeError("No blog-hero section in en-blog.html")
    art_match = re.search(r'<article class="blog-card">', content[hero_match.end():])
    if not art_match:
        raise RuntimeError("No existing blog-card in blog-hero")
    insert_pos = hero_match.end() + art_match.start()
    line_start = content.rfind('<!--', 0, insert_pos)
    if line_start == -1:
        line_start = insert_pos
    new_content = content[:line_start] + card + content[line_start:]
    with open(blog_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  [OK] en-blog.html: added {slot} card")


def add_sitemap(art):
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    if f'/{art["slug"]}.html' in content:
        print(f"  [skip] sitemap.xml: {art['slug']}.html already present")
        return
    new_url = f"""
  <url>
    <loc>https://ribbonbow123.com/{art['slug']}.html</loc>
    <lastmod>{DATE_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""
    content = content.replace("</urlset>", new_url + "\n</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] sitemap.xml: added {art['slug']}.html")


if __name__ == "__main__":
    print("=== Updating en-blog.html and sitemap.xml for 2026-08-21 articles ===\n")
    insert_card(AM, "am")
    add_sitemap(AM)
    insert_card(PM, "pm")
    add_sitemap(PM)
    print("\n=== Done. ===")
