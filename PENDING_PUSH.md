# Pending Manual Push

- **Status**: ✅ CLEARED — push landed on `origin/main`; both 2026-11-26 articles live (HTTP 200).
- **Last successful push**: 2026-11-26 cron (08:00 AM + 13:00 PM slots), ribbonbow123.
- **Articles published (2026-11-26)**:
  - AM `blog-ribbon-oem-backing-substrate-materials-solid-organza-metallic-film-nonwoven-decoration-method-construction-tradeoffs-brand-procurement-guide-2026-11-26-am.html`
  - PM `blog-ribbon-oem-decoration-durability-foil-adhesion-rub-fastness-print-abrasion-resistance-metallic-film-transfer-testing-brand-procurement-guide-2026-11-26-pm.html`
- Publish path: `publish_guard.py push --from-status` → ok=6 skipped=10 failed=0 (10 legacy files
  already byte-identical on remote). `publish_guard.py verify` → both files present on remote tree
  but live 404 → Pages deploy lag → single `workflow_dispatch` of `deploy.yml` on `ref: main`
  after queue drain → both articles HTTP 200 (matches the 11-23/11-24 playbook).
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
- **Articles published**:
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

## Action required

None. If a future cron run reports a push failure, do not retry in the same run —
record it here and leave it for the next cron cycle or for manual action.
