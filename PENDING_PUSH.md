# Pending Manual Push

- **Status**: ✅ CLEARED — 2026-11-27 cron (08:00 AM + 13:00 PM slots), ribbonbow123.
  Both articles published and live (HTTP 200); LOCAL-ONLY = 0; nothing pending.

## 2026-11-27 cron run

- **Articles published**:
  - AM `blog-ribbon-oem-woven-ribbon-weaving-defect-taxonomy-broken-picks-weft-bars-floats-snags-misses-inspection-specification-brand-procurement-guide-2026-11-27-am.html`
    — "Woven Ribbon Weaving Defect Taxonomy and Inspection Specifications" (~5,000 words, 8 FAQ)
  - PM `blog-ribbon-oem-winding-core-roll-format-specification-automated-feeding-bow-machine-packaging-line-jam-reduction-roll-changeover-brand-procurement-guide-2026-11-27-pm.html`
    — "Ribbon Winding, Core and Roll Format Specification for Automated Feeding" (~4,770 words, 8 FAQ)
- `publish_guard.py check` → 898 html scanned, **0 error**; sitemap 897 locs / 897 unique / 1 host.
- `publish_guard.py push --from-status` → **ok=6 skipped=0 failed=0** (2 articles + blog.html +
  en-blog.html + index.html + sitemap.xml).
- `publish_guard.py verify` → both files present on remote tree, but live 404 →
  **Pages deploy lock contention** (occurrence #26, same root cause as 11-24).
  Fix: queue-drain wait → **single `workflow_dispatch` of `deploy.yml` on `ref: main`**
  → both articles HTTP 200 on first poll.
  Tool: `/workspace/tools/rb_pages_rebuild_1127.py`.
- `reconcile_remote.py` → **LOCAL-ONLY = 0** (REMOTE-ONLY = 28 legacy `_body_*` build artifacts, harmless).
- Live verification: both article URLs HTTP 200; `blog.html` / `en-blog.html` / `index.html` HTTP 200
  and each contain both slugs; live `sitemap.xml` = 897 `<loc>`, 2× `<lastmod>2026-11-27</lastmod>`.
- Local git commit: `db269f3`.

## ⚠️ sitemap.xml corruption repaired (2026-11-27) — pre-existing, not caused by this run

The `sitemap.xml` inherited from the 2026-11-26 rebase merge had **two structural defects that
were already committed in HEAD** (`b5785b6`) and were being **served live**:

1. A stray merge-conflict marker `<<<<<<< HEAD` on line 2 (the `=======` / `>>>>>>>` halves had
   been resolved away, but the opening marker survived).
2. **No `</urlset>` closing tag** — the file was truncated XML.

Consequence: the entire 895-URL sitemap was **not parseable as XML** by any strict parser, so
search engines could not process it — despite every individual URL returning HTTP 200.

Every committed version going back to `f35cc48` carried the marker, and none had the closing tag;
the last clean sitemap in history was `b5d5564` (63 URLs). The rebase merge on 2026-11-26
produced this.

**Repair** (`/workspace/tools/fix_rb_sitemap_xml.py`, idempotent): strip the conflict-marker line,
append the missing `</urlset>`, keep all 895 `<loc>` entries unchanged. Verified:
`xml.etree.ElementTree.fromstring()` parses OK; 897 locs / 897 unique; 1 host; 0 conflict markers.
**Live sitemap now parses correctly** with 897 `<loc>` entries.

*Note for future slots:* `publish_guard.py check` does **not** validate sitemap XML well-formedness
— only loc uniqueness, host, and future-dates. It passed clean while the sitemap was invalid XML.
Consider adding an `ET.fromstring()` assertion to `check_sitemap()`.

## Historical

- **Last successful push**: 2026-11-26 cron (08:00 AM + 13:00 PM slots), ribbonbow123.
- Articles published (2026-11-26):
  - AM `blog-ribbon-oem-backing-substrate-materials-solid-organza-metallic-film-nonwoven-decoration-method-construction-tradeoffs-brand-procurement-guide-2026-11-26-am.html`
  - PM `blog-ribbon-oem-decoration-durability-foil-adhesion-rub-fastness-print-abrasion-resistance-metallic-film-transfer-testing-brand-procurement-guide-2026-11-26-pm.html`
- Publish path: `publish_guard.py push --from-status` → ok=6 skipped=10 failed=0. `publish_guard.py
  verify` → both files present on remote tree but live 404 → Pages deploy lag → single
  `workflow_dispatch` of `deploy.yml` on `ref: main` after queue drain → both articles HTTP 200.
- Live verification: both article URLs HTTP 200; `blog.html` / `en-blog.html` / `index.html` each
  contain both slugs; `sitemap.xml` 891 locs / 891 unique, 2× `<lastmod>2026-11-26</lastmod>`.
- `reconcile_remote.py` → LOCAL-ONLY = 0.
- `publish_guard.py check` → 895 html scanned, 0 error.
- Local git commit: `3e50349`.
- **Last successful push**: 2026-11-24 cron (08:00 AM + 13:00 PM slots), ribbonbow123.
- **Re-verified 2026-11-24 (13:00 slot re-entry)**: reconcile LOCAL-ONLY = 0; both article
  URLs HTTP 200; live sitemap carries 2× `<lastmod>2026-11-24</lastmod>` and 885 `<loc>`;
  live blog.html / en-blog.html / index.html all link both articles. `publish_guard.py check`
  → 888 html, 0 error. Local git history now records both articles (commit `74c268d`).
  → **No new push was needed**; the 13:00 slot was already published by the earlier run.
- Articles published:
  - AM `blog-ribbon-oem-scrap-yield-waste-material-efficiency-trim-loss-setup-waste-colour-change-waste-defective-roll-cost-recovery-brand-procurement-guide-2026-11-24-am.html`
  - PM `blog-ribbon-oem-supplier-risk-assessment-business-continuity-dual-sourcing-financial-health-warning-signs-exit-plan-dependency-map-brand-procurement-guide-2026-11-24-pm.html`
- Live verification: both article URLs return HTTP 200; sitemap.xml contains both `<loc>` entries with `<lastmod>2026-11-24</lastmod>`.
- `reconcile_remote.py` → LOCAL-ONLY = 0.
- `publish_guard.py check` → 888 html scanned, 0 error; sitemap 885 locs / 885 unique / 1 host.

## Pages deploy incident (2026-11-24, historical same root cause, occurrence #25)

- `publish_guard.py push` uploads one file per Contents API call → **6 consecutive commits** in ~20 s.
- GitHub Actions `Deploy to GitHub Pages` runs then failed **in a batch**, all at the
  `Deploy to GitHub Pages` step (`Setup Pages` / `Upload artifact` = success).
- Result: remote tree contained every file (LOCAL-ONLY = 0) but the site served the older
  tree — AM article 404, PM article 404, live sitemap stale (883 locs vs remote 885).
- `actions/runs` rerun of the failed run **also failed** — a rerun does not clear the Pages
  deployment lock.
- **Fix that worked** (matches the 11-23 playbook): wait for the workflow queue to drain
  (`busy == 0`), then **one single `workflow_dispatch` of `deploy.yml` on `ref: main`** →
  serial rebuild → success → both articles HTTP 200.
- Tooling: `/workspace/tools/rb_pages_rebuild_1124.py` (queue-drain wait + single dispatch + live 200 verify).
- Note: the `seo-sitemap-submit.yml` workflow rerun returned **403** (token cannot rerun that
  workflow). GSC sitemap submission for 2026-11-24 may therefore be missing — harmless for
  crawl discovery (the sitemap is served live and linked from robots.txt) but worth a manual
  GSC ping if the next slot reports a stale `last seen`.
