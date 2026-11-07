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
