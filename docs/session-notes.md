# Session notes

Newest entry first. Each entry covers where the session ended, what I struggled with, commands to revisit, and what to try next.

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
