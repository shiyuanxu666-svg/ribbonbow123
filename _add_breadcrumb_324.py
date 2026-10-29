#!/usr/bin/env python3
"""Add BreadcrumbList JSON-LD to RB article #324, matching the site convention
established on #322/#323 in the 2026-10-29 AM run."""
import re
from pathlib import Path

ROOT = Path("/workspace/ribbonbow123")
F = ("blog-ribbon-oem-outdoor-apparel-trim-weatherproof-uv-cold-flex-abrasion-"
     "sun-rain-salt-performance-private-label-buyers-guide-2026-10-29-pm.html")
SITE = "https://ribbonbow123.com"
SLUG = F[:-5]
URL = f"{SITE}/{SLUG}"

p = ROOT / F
h = p.read_text(encoding="utf-8")

if "BreadcrumbList" in h:
    print("[SKIP] BreadcrumbList already present")
    raise SystemExit(0)

# breadcrumb name = slug with dashes turned into spaces (matches #322 convention)
crumb_name = SLUG.replace("blog-", "", 1).replace("-", " ")

bc = f"""    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "{URL}#breadcrumb",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{SITE}/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "{SITE}/blog.html"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{crumb_name}",
      "item": "{URL}"
    }}
  ]
}}
    </script>
</head>"""

assert h.count("</head>") == 1, "expected exactly one </head>"
h = h.replace("</head>", bc, 1)
p.write_text(h, encoding="utf-8")

# verify it parses
import json
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
types = []
for b in blocks:
    o = json.loads(b)
    types.append(o.get("@type"))
print(f"[OK] BreadcrumbList added -> {F[:60]}")
print(f"     JSON-LD blocks now: {len(blocks)} | types={types}")
assert "BreadcrumbList" in types
print("[VERIFIED] all JSON-LD parses cleanly")
