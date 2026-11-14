# Pending Manual Push

- **Status**: ✅ CLEARED — push landed on `origin/main` (remote ref `f39d93c197`).
- **Last successful push**: 2026-11-02 cron, commit `2f06f42` (article publish), superseded by
  `f39d93c` (SEO auto-fix on top of it). Both are in the pushed tree.
- **Articles published in this push**: ribbonbow123 #339 and #340 (see git log).
- Live verification: both article URLs return HTTP 200; sitemap.xml contains both `<loc>` entries
  with `<lastmod>2026-11-02</lastmod>`.
- All previously pending items (#322, #323, #327, #328, #330, #331) were included in the
  cumulative tree pushed by this run and are now live.

## Action required

None. If a future cron run reports a push failure, do not retry in the same run —
record it here and leave it for the next cron cycle or for manual action.

## Note on push-retry.py runtime

`python3 /workspace/push-retry.py` uploads blobs one-by-one through the GitHub API and can
take longer than a 5-minute command timeout on this repo size. When the wrapper kills it
with SIGTERM, the partial upload is harmless — re-running resumes from the same local commit
(the script exits early with `UP-TO-DATE` if remote already matches HEAD). Give it a longer
timeout on the next run rather than treating the SIGTERM as a push failure.

## 2026-11-02 15:00 cron — pushed and verified

- **ribbonbow123** article #343 pushed: `3780ac3..62781cc` on `origin/main` (git push, HTTP/1.1).
- **smithribbon** article #300 published via GitHub API: commit `f4c3b8d3`, main -> `f4c3b8d3`.
- Both live URLs return HTTP 200, content byte-identical to the generated artifacts, sitemap `<loc>`
  present with `<lastmod>2026-11-02</lastmod>`, and blog listing pages updated.
- **Status**: CLEARED — nothing pending.

### Operational notes for the next run

- `smithribbon-web` is a **sparse** local checkout: only recently published articles are on disk.
  `blog.html` / `en-blog.html` / `index.html` / `sitemap.xml` do **not** exist locally — they must be
  fetched from the GitHub API (`/contents/<path>?ref=<sha>`) and written back via the tree/commit API.
- The GitHub tree API returns **502 Server Error** if the tree payload contains all ~1200 entries.
  Send only the **changed** entries together with `base_tree` and let GitHub inherit the rest.
- `smithribbon-web/index.html` has no `<article class="blog-card">` anchor, so no card can be
  inserted there automatically. `blog.html` and `en-blog.html` are the working listing surfaces.
- `git push` to github.com intermittently fails ("Failed to connect to github.com port 443") while
  `api.github.com` stays reachable. Retry the push; do not treat it as a content failure.

## 2026-11-06 13:00 cron — pushed successfully

- **ribbonbow123** articles #357 (AM, 08:00) and #358 (PM, 13:00) pushed via
  `python3 /workspace/push-retry.py` (single attempt, exit 0).
- Local HEAD `a887b0c` → remote `main` `1013e61`. `push-retry.py` rebuilds the tree via the
  GitHub API, so the remote commit SHA differs from the local one while the content is identical.
  This is expected behaviour, not a failed push — check tree content, not SHA equality.
- Live verification (HTTP 200 on both URLs):
  - #357 AM — `blog-oem-custom-packaging-private-label-ribbon-programme-guide-nine-field-brief-sample-ladder-artwork-ownership-decoration-method-moq-cost-drivers-first-order-readiness-checklist-private-label-buyers-guide-2026-11-06-am.html`
    desc 200 chars, 8 FAQ items, FAQPage + BlogPosting present, ~5,857 visible words.
  - #358 PM — `blog-ribbon-oem-quote-comparison-total-cost-analysis-normalise-two-supplier-landed-cost-components-supplier-scoring-evidence-hidden-cost-traps-cost-reduction-sequence-brand-procurement-guide-2026-11-06-pm.html`
    desc 199 chars, 8 FAQ items, FAQPage + BlogPosting present, ~6,173 visible words.
  - sitemap.xml: exactly 1 `<loc>` per article (0 duplicates), `<lastmod>2026-11-06</lastmod>` x2.
- No pending items. Nothing requires manual action.

### Note for the next cron run

The 13:00 slot ran with the day's AM and PM articles **already built and committed** by an
earlier run of the same day. The job then correctly identified the unpushed state and pushed
once. If a future run finds both of the day's articles already committed and pushed, the correct
action is to verify and report, **not** to write replacement articles.

## 2026-11-07 13:00 cron — pushed successfully

- **ribbonbow123** articles #360 (AM, 08:00) and #361 (PM, 13:00) were already built and committed
  locally in `6b5220a` (committed 2026-11-07 00:07 UTC) by an earlier run of the same day.
  Per the rule above, this run **verified and pushed** rather than writing replacement articles.
- Push: `python3 /workspace/push-retry.py`, single attempt, exit 0.
  Local `6b5220a` → remote `main` `65a38f72` (the script rebuilds the tree via the GitHub API,
  so the remote SHA differs from the local one while content is identical — expected).
  Remote was 1 commit ahead / local 3 commits ahead before the push.
- Content verification (before push, local files):
  - #360 AM — `blog-ribbon-oem-private-label-packaging-purchasing-guide-9-evaluation-criteria-factory-capability-evidence-cost-transparency-sampling-approval-reorder-governance-brand-procurement-guide-2026-11-07-am.html`
    desc 190 chars, 8 FAQ items, BlogPosting + FAQPage + BreadcrumbList present, ~3,563 visible words.
  - #361 PM — `blog-ribbon-certification-compliance-credentials-what-each-certificate-actually-covers-verification-scope-expiry-evidence-archive-retail-audit-requests-brand-procurement-guide-2026-11-07-pm.html`
    desc 172 chars, 7 FAQ items, BlogPosting + FAQPage + BreadcrumbList present, ~3,391 visible words.
  - Both use the "since 2004" entity wording (no "since 2007" occurrences).
  - sitemap.xml: exactly 1 `<loc>` per article, 0 duplicates; blog.html + en-blog.html both updated.
- No pending items. Nothing requires manual action.

## 2026-11-07 15:00 cron — published and verified (RB #362)

- **ribbonbow123** article #362 (PM, 15:00 slot) published.
- Local commit `bbce2e3`; pushed via the **GitHub tree/commit API** (not `git push`).
  Remote `main` moved `3ecf31748` -> **`bffaac333`**. The remote SHA differs from the local
  SHA because the API rebuilds the tree from the remote base tree — content is identical.
- `git rebase origin/main` was attempted first and **aborted cleanly** (conflict in blog.html /
  en-blog.html with the concurrent cron's edits). The tree-based API push reconciled against
  the remote tree instead, so the concurrent `robots.txt` / `llms.txt` / `.gitignore` commits
  were preserved.
- Article: `blog-ribbon-oem-sample-approval-counter-sample-production-release-four-stage-approval-ladder-retained-sample-register-re-approval-triggers-release-note-evidence-retention-private-label-buyers-guide-2026-11-07-pm.html`
  desc 181 chars, 8 FAQ items, Article + BlogPosting + FAQPage + BreadcrumbList present,
  ~5,253 visible words, 0 "since 2007" occurrences.
- Live verification (HTTP 200): article 42,888B; blog.html +1 card; en-blog.html +2 links;
  index.html +1 card; sitemap.xml exactly 1 `<loc>`.
- No pending items. Nothing requires manual action.

### Note for the next cron run

`_push_rb_1107pm.py` / `_push_sr_1107pm.py` (in `/workspace`) are idempotent, tree-based
GitHub API push scripts that reconcile against the **current remote main tree** and upload only
the changed files. Use them instead of `git push` / `push-retry.py` when the local checkout
trails the remote — a `git push` will be rejected as non-fast-forward, and `git rebase` will
conflict on blog.html / en-blog.html.

## 2026-11-11 cron — pushed successfully (2 articles)

- **ribbonbow123** articles **#372** (AM, 08:00 slot) and **#373** (PM, 13:00 slot) published.
- Local commit `1c6e86f`; pushed via `python3 /workspace/push-retry.py`, single attempt.
  Remote `main` `0a3c847c` -> **`fe1d4f73`** (the script rebuilds the tree via the GitHub API,
  so the remote SHA differs from the local one while content is identical — expected).
- Remote commit touched exactly 6 files: 2 new articles + `blog.html`, `en-blog.html`,
  `index.html`, `sitemap.xml`.
- Content verification (via GitHub contents API on `ref=main`):
  - #372 AM — `blog-ribbon-oem-incoming-quality-inspection-acceptance-procedure-defect-classification-sampling-plan-shade-tolerance-correction-action-private-label-buyers-guide-2026-11-11-am.html`
    desc 172 chars, 7 FAQ items (LD == HTML), Article + BlogPosting + FAQPage present, ~5,003 words.
  - #373 PM — `blog-ribbon-oem-pilot-run-first-production-lot-sample-to-production-transition-scale-up-process-capability-brand-procurement-guide-2026-11-11-pm.html`
    desc 174 chars, 7 FAQ items (LD == HTML), Article + BlogPosting + FAQPage present, ~4,651 words.
  - Both use the "since 2004" entity wording (0 "since 2007" occurrences).
  - Remote sitemap.xml: 831 `<loc>`, 0 duplicates; both new URLs present exactly once with
    `<lastmod>2026-11-11</lastmod>`.
- Note: live `ribbonbow123.com` still served the pre-push sitemap (829 locs) at the moment of
  checking — normal GitHub Pages build propagation lag, not a content failure. The GitHub repo
  content is confirmed correct.
- **Status**: CLEARED — nothing pending.

### Note for the next cron run

`blog.html` currently contains 2 pre-existing duplicate `<h3><a>` links for the old
"b2b-68-module-sustainability-esg" and "b2b-69-module-retailer-tender-rfp" articles. These are
leftovers from the earlier keyword-stuffed "module" series, not from the current article runs.
Do not create new duplicates; the old ones are outside the scope of the daily publishing job.

### 2026-11-11 — documentation commit pending

- The article commit (`1c6e86f` -> remote `fe1d4f73`) is **pushed and verified**.
- A follow-up documentation-only commit `2d22189` (this PENDING_PUSH.md entry) was still
  uploading when the cron window closed. It touches **no article, blog.html, en-blog.html,
  index.html or sitemap.xml** — it is a log file only.
- Action for the next cron: run `python3 /workspace/push-retry.py` once. The script exits early
  with `UP-TO-DATE` if the remote already matches HEAD, so it is safe to run unconditionally.

## 2026-11-11 daily cron - pushed successfully

- **ribbonbow123** 2 articles published and pushed in one commit:
  - AM (08:00) `blog-ribbon-oem-rfq-writing-guide-comparable-quotations-procurement-manager-brand-buyers-guide-2026-11-11-am.html`
  - PM (13:00) `blog-ribbon-oem-incoterms-shipping-terms-landed-cost-risk-transfer-brand-procurement-guide-2026-11-11-pm.html`
- Local commit `6804008` -> remote tree `b0f3347` -> remote ref `8b7abc3a` (API HTTP 200).
- Pushed via `python3 /workspace/push-retry.py`; 7 blobs + 1 tree uploaded, ran ~8 min.
- blog.html / en-blog.html / index.html listing cards inserted newest-first
  (PM 13:00 before AM 08:00); sitemap.xml gained both `<loc>` entries with
  `<lastmod>2026-11-11</lastmod>`; 836 locs, 0 duplicates.
- Build script: `/workspace/rb_build_1111b.py`; bodies: `/workspace/rb_body_1111b_am.py`,
  `/workspace/rb_body_1111b_pm.py`; validator: `/workspace/rb_validate_1111b.py` (PASS).
- No pending manual action.

## 2026-11-14 daily cron — pushed successfully (2 articles)

- **ribbonbow123** articles **#382** (AM, 08:00) and **#383** (PM, 13:00) published.
- Topics: EUDR/EPR/PPWR packaging regulation (0 prior dedicated articles) and REACH/SVHC
  chemical compliance (0 prior dedicated articles) — both genuine coverage gaps in the
  credible content set.
- Pushed via `python3 /workspace/tools/publish_guard.py push --repo ribbonbow123
  --from-status <manifest>` (NOT `git push`). Result: ok=5, skipped=1 (idempotent
  re-push of the AM article), failed=0.
- Files touched: 2 new articles + `blog.html`, `en-blog.html`, `index.html`, `sitemap.xml`.
  sitemap.xml gained both `<loc>` entries with `<lastmod>2026-11-14</lastmod>`; 849 locs,
  0 duplicates.
- Content verification: #382 2699 words / 7 FAQ; #383 2549 words / 7 FAQ; all meta/og/
  twitter descriptions <= 200 chars and independently worded; Article + BlogPosting +
  FAQPage JSON-LD present in both; "since 2004" entity wording used.
- `reconcile_remote.py` -> **LOCAL-ONLY = 0** (local 887 = remote 887).
- Live verification (HTTP 200) confirmed for both articles + blog.html + en-blog.html +
  index.html + sitemap.xml.
- **Status**: CLEARED — nothing pending.

### Operational notes for the next cron run

1. `--from-status` manifest must contain **one bare relative path per line**. Writing
   `git status --short` output directly causes every file to fail with "file not found".
   Use: `git status --porcelain | sed -E 's/^.. //' | sed -E 's/.* -> //' > manifest.txt`
2. GitHub Pages needs ~30-60 s to rebuild after a push. A live 404 or 503 immediately
   after `push`/`verify` is propagation lag, **not** a failure — wait and re-check, but
   never re-push.
3. `index.html` has a pre-existing unclosed `<li>` in its bottom link list. Insert new
   items as siblings *after* closing the previous `<li>`, otherwise you create nested
   `<li>` tags and break the open/close balance.

### 2026-11-14 05:00 UTC cron — re-verification (no new publish needed)

- This cron slot found today's AM (#382 EUDR/EPR) and PM (#383 REACH/SVHC) articles
  **already published and live** by an earlier run of the same daily cron.
- Verified via `publish_guard.py check --repo ribbonbow123`: 850 HTML files scanned,
  sitemap 849 locs / 849 unique / 1 host, **0 errors**.
- `reconcile_remote.py --repo ribbonbow123`: local 887 = remote 887, **LOCAL-ONLY = 0**.
- Live HTTP 200 confirmed for both articles + blog.html + en-blog.html + index.html +
  sitemap.xml. (One PM curl returned a transient `000` timeout, re-request returned 200.)
- Local git tree was 6 files behind the remote publish (untracked articles + 4 listing
  files). Committed locally as `e150809` so the next run starts from a clean tree.
  **No re-push performed** — remote content already matches; re-pushing would be a no-op.
- **Status**: CLEARED — nothing pending.
