# Session notes

Newest entry first. Each entry covers where the session ended, what I struggled with, commands to revisit, and what to try next.

## 2026-11-06 — Session 3 (done)

- **Status:** Done: #36 create links (PR #39), #37 redirect (PR #40), #38 stats (PR #41), and an extra, #45 Postman collection (PR #46). This completes Session 3. Session 4 issues are ready: #42 release-please, #43 Dockerfile, #44 GHCR image.
- **Decisions worth remembering for interviews:**
  - Code uniqueness is enforced by the primary key, not by checking first, which would race under concurrent requests.
  - Codes come from `secrets` (7 base62 characters). A counter avoids collisions but makes links enumerable.
  - Redirects use 302, not 301, because browsers cache a 301 and the clicks would never be counted.
  - Clicks are incremented in one SQL statement (`clicks = clicks + 1`), so concurrent clicks aren't lost. 3 parallel redirects counted 3.
  - `GET /{code}` matches any single-segment path, so `/health` must be registered before it.
  - Per-link click counts don't belong in Prometheus: one series per link is high cardinality.
- **Struggled with:**
  - The review step was skipped on every PR (#39, #40, #41, #46), although the Session 3 plan asked for a self-review or an AI review before merging.
  - Commit titles: the service commit was first titled `feat: add POST /links endpoint`. Fixed with `git commit --amend -m` before pushing.
  - Issue setup: #38 was created without assignee and milestone, and #45 with an empty body.
  - Staging is a snapshot: a file changed after `git add` showed as `AM` and had to be added again.
  - Tools: `/docs` can't show a redirect, because `fetch` follows it and CORS blocks the target site. DBeaver kept the deleted `links.db` open and failed with `SQLITE_READONLY_DBMOVED` until reconnected.
- **Went well:** the PR descriptions from #39 on explained decisions and trade-offs, not just changes. Every commit passed the checks on its own, and #41 was kept as one commit because its rename crossed all layers.
- **Commands to revisit:** `git commit --amend -m`, `git status --short` (reading `A`, `M` and `AM`), `curl -i`, `sqlite3`.
- **Ideas:** Prometheus and Grafana after Session 5, with a `/metrics` endpoint and no per-link series. Postman tests with `pm.test`.
- **Try next:** in Session 4, review each PR before merging, or remove the review step from the plan on purpose instead of skipping it.

## 2026-11-05 — Session 2 (done)

- **Status:** Done: #21 dependency cache (PR #32) and #22 required checks on `main` (PR #33). This completes Session 2. Both items left open on 2026-11-04 are resolved: squash commits now use the PR title and description, and the title test ran on PR #32.
- **Results worth remembering:**
  - The cache works but didn't make CI faster: restoring it takes ~2 s, about what the install saves, and runs stayed at ~16 s. It should pay off once dependencies grow.
  - `main` now requires `checks`, `pr-title` and `checklists`, and branches must be up to date. PR #33 was blocked by `checklists` until #22's boxes were checked.
- **Struggled with:**
  - PR #32 was merged with its original description, so commit `4422acc` on `main` says the cache makes CI "a few seconds faster" and has no run times, while the box saying it did was checked. Since descriptions now become the commit body, these mistakes are permanent.
  - Running `git revert HEAD` twice reverted the revert. Caught before pushing and fixed with `git reset --hard HEAD~1`.
  - PRs #32 and #33 were merged without the review I had planned.
- **Went well:** PR #33 had the best description so far: the What covered the ruleset change that isn't in the diff, the Why explained the trade-off, and How it was tested linked the failing run.
- **Commands to revisit:** `git reset --hard HEAD~1`, `git revert` (and why running it twice undoes itself), `gh pr edit --title`, `gh run rerun --failed`.
- **Try next:** in Session 3, write each PR description like #33 before asking for a review, and wait for the review before merging.

## 2026-11-04 — Session 2 (in progress)

- **Status:** Done: #19 ruff and mypy (PR #23), #20 CI workflow (PR #24), #25 PR title and checklist checks (PR #26), #27 clearer PR template comments (PR #29). Next: #21 (cache dependencies, baseline is 13–18 s per run without cache) and #22 (require CI on `main`, including `pr-title` and `checklists`).
- **Still open from today:**
  - The squash merge setting is still `COMMIT_OR_PR_TITLE`, so single-commit PRs put the commit title on `main` and skip the title check. Change it to the PR title.
  - The title test from #25 never ran: give a PR an invalid title, watch `pr-title` fail, then fix it.
- **Struggled with:**
  - Merging before the work was finished: #24 without a review and with a non-conventional title (`Add ci workflow` is now on `main`), #26 with two "Done when" boxes checked but not done, #29 with the description copied unchanged from #28.
  - Committing new work on the branch of an already merged PR (#28). Fixed with a new branch from `main` and `git cherry-pick`.
  - Pushing after an amend: the branch diverges, so it needs `git push --force-with-lease`.
- **Commands to revisit:** `git cherry-pick`, `git revert`, `gh run rerun --failed`, `gh pr checks --watch`, `gh pr close --delete-branch`.
- **Ideas:** a third issue form for `chore`/`ci` tasks, since neither existing form fits them.
- **Try next:** before each merge, reread the issue's "Done when" and open each link in "How it was tested". Only check a box after doing the work.

## 2026-11-04 — Session 1 (done)

- **Status:** Done: #4 (PR #16), the project skeleton with uv, FastAPI, `GET /health` and one test. This completes Session 1. Still to confirm: both issue forms appear when opening a new issue, the check left from #2.
- **Struggled with:**
  - PR descriptions still took review rounds: "How it was tested" first listed what was added instead of what was checked, and the Why said the health endpoint was for CI instead of for whatever runs the app.
  - After the last session: committed the notes on `main` before creating the branch, and merged #15 with an empty description, so #14 had to be closed by hand.
  - Telling apart `--amend`, `--fixup` and `reword` for fixing an older commit.
- **Commands to revisit:** `git rebase -i` with `reword`, `git commit --fixup=reword:<hash>`, `git branch -f main origin/main`, `git log origin/main..HEAD`.
- **Ideas:** add uv to `docs/dev-environment.md`. Check whether `httpx2` is the official replacement Starlette's warning suggests.
- **Try next:** in Session 2, write "How it was tested" from the CI results of your own PR, including the one that fails on purpose.

## 2026-11-02 — Session 1 (in progress)

- **Status:** Done: #6 (PR #7), #8 (PR #10), #9 (PR #11), #2 (PR #12) and #3 (PR #13). Also set up the terminal and the git identity on this machine. Next: #4 (project skeleton), the last issue in Session 1. Also confirm both issue forms appear when opening a new issue, the check still open from #2.
- **Struggled with:**
  - PR descriptions: #7, #10, #11 and #12 skipped What, Why or How it was tested. #13 was the first with all three, and it took a review to make them specific.
  - PR #12 was merged without the review I had planned.
  - Commits on #10 and #11 had the wrong author because `user.name` and `user.email` weren't set, which added a `Co-authored-by` line to the squash message.
  - Telling apart `main` and `origin/main`, `fetch` and `pull`, and how rebase rewrites commits.
- **Commands to revisit:** `git pull --ff-only`, `git pull --rebase`, `git commit --amend`, `git commit --fixup`, `git rebase -i --autosquash`, `git push --force-with-lease`.
- **Try next:** run #4 through the full loop in several small commits, then ask for a review before merging.

## 2026-11-01 — Session 1 (in progress)

- **Status:** Done: ruleset, labels, milestone, board, issues #1–#4, and PR #5 (closes #1). Next: #2 (templates), #3 (`CONTRIBUTING.md`), #4 (project skeleton).
- **Struggled with:** finding the labels page and renaming board columns. The ruleset also needed fixing: a coverage rule and last-push approval don't suit a solo repo with no CI yet.
- **Commands to revisit:** `git switch -c`, `git push -u`, `git fetch --prune`, and why `git branch -D` is needed after a squash merge.
- **Try next:** run #2 through the full loop without step-by-step instructions, then ask for a review.
