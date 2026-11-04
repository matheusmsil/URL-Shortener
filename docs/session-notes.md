# Session notes

Newest entry first. Each entry covers where the session ended, what I struggled with, commands to revisit, and what to try next.

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
