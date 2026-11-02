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
