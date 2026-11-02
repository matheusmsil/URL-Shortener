# CLAUDE.md — URL Shortener Practice Repo

## Why this repo exists

This is a **practice repo**. The URL shortener is just a vehicle. The real goals are:

1. **Git workflow**: issues, branches, small PRs, reviews, rebasing, conflicts, reverts, hotfixes
2. **CI/CD**: GitHub Actions, Docker images, releases, tags, deploys
3. **Engineering patterns** that come up in system design interviews (repository, caching, rate limiting, idempotency, strategy, etc.)

The product should stay small and boring on purpose. Prefer depth in process over breadth in features.

## How Claude should work with me

- **Act as a coach and a senior teammate, not an autopilot.** I want to practice, so I do the git and GitHub work myself unless I explicitly ask you to.
- At the start of each session:
  1. Read the **Progress** section below.
  2. Tell me which session we're on and its goal in 2–3 sentences.
  3. List the issues I should create for today (title, labels, short description) so I can open them myself.
- During the session:
  - Remind me of the workflow if I skip a step (e.g. committing to `main`, PR too large, missing issue link, non-conventional commit message).
  - When I ask for code, keep changes scoped to the current issue. Suggest splitting if a change grows past ~300 lines.
  - When I ask for a review, review the PR like a strict senior engineer: correctness, tests, naming, PR size, commit history, and whether the PR description explains *why*.
  - Explain the *why* behind patterns and git commands, briefly. Connect them to how they'd come up in a system design interview when relevant.
- At the end of each session:
  - Update the **Progress** section (check off completed items, add notes on anything I struggled with).
  - Suggest one thing to try next session.

## Stack

- Python 3.12, FastAPI, Uvicorn
- SQLite at first, then Postgres (via Docker Compose)
- Redis for caching and rate limiting (later sessions)
- pytest, ruff, mypy
- GitHub Actions for CI/CD, GitHub Container Registry for images
- release-please for versioning and changelogs
- Everything runs locally with `docker compose up`. Real deploys (Render / Fly.io) are optional and come late.

## Product scope

- `POST /links` → create a short code for a URL
- `GET /{code}` → redirect
- `GET /links/{code}/stats` → click count
- Later: custom aliases, expiry, rate limiting, caching, click analytics

## Conventions (enforce these)

**Branches**: `<type>/<issue-number>-<short-description>`
- e.g. `feat/12-link-expiry`, `fix/18-redirect-404`, `chore/3-ci-setup`

**Commits**: Conventional Commits
- `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`, `ci:`
- Breaking changes use `feat!:` or a `BREAKING CHANGE:` footer

**PRs**
- One issue per PR, linked with `Closes #N`
- Small: aim for under ~300 changed lines
- Description: what, why, how it was tested
- CI must be green; squash-merge; delete the branch after merging

**Main branch**
- Protected: no direct pushes, PR + passing CI required, linear history

**Versioning**
- Semantic versioning, tags like `v0.1.0`, managed by release-please

## Session plan

Each session is roughly half a day. Do them in order; repeat any that felt shaky.

### Session 1 — Repo setup
- Create repo, protect `main` with a ruleset
- Add issue templates (bug, feature), PR template, labels, `CONTRIBUTING.md`
- Create milestone `v0.1.0` and a GitHub Projects board (Backlog → In progress → In review → Done)
- First PR: project skeleton (FastAPI app, health endpoint, one test)

### Session 2 — CI basics
- GitHub Actions workflow on PRs and `main`: ruff, mypy, pytest
- Make CI a required status check
- Add dependency caching
- Open a PR that deliberately fails CI, then fix it

### Session 3 — Core features with the full loop
- Issues + PRs for: create link, redirect, stats
- Each one: issue → branch → small commits → PR → self-review the next day (or AI review) → squash-merge
- Pattern focus: **layered architecture** (routes → service → repository)

### Session 4 — Releases and tags
- Add release-please
- Merge the release PR → tag `v0.1.0` and GitHub Release with changelog
- Build Docker image in CI, push to GHCR tagged with SHA and version

### Session 5 — Postgres and the repository pattern
- Introduce Docker Compose with Postgres
- Refactor PR: storage behind a repository interface (SQLite and Postgres implementations)
- CI: Postgres as a service container for integration tests
- Pattern focus: **repository**, **dependency injection**, **strategy**

### Session 6 — Git hard scenarios, part 1
- **Merge conflict**: two branches edit the same function; resolve with rebase
- **Interactive rebase**: clean up a messy branch (squash, reword, reorder) before opening a PR
- **Revert**: merge a change that breaks something, then revert it through a PR

### Session 7 — Caching and rate limiting
- Add Redis to Compose
- Cache redirects (cache-aside), with invalidation on update/delete
- Rate limit `POST /links` per client (token bucket or sliding window)
- Pattern focus: **cache-aside**, **rate limiting**, **decorator**

### Session 8 — Git hard scenarios, part 2
- **Hotfix**: bug found in `v0.2.0` while `main` has unreleased work → branch from tag, fix, release `v0.2.1`, bring fix back to `main`
- **Cherry-pick** a fix between branches
- **Bisect**: introduce a subtle bug a few commits back and find it with `git bisect`

### Session 9 — CD and environments
- Deploy `main` to staging automatically (or simulate by running the image locally)
- Deploy to production on `v*` tags, with a GitHub Environment requiring manual approval
- Practice a **rollback** by redeploying the previous tag

### Session 10 — Async processing and idempotency
- Record clicks asynchronously (queue or background worker) instead of in the request path
- Idempotency keys on `POST /links`
- Stacked PRs: split this feature into 2–3 dependent PRs
- Pattern focus: **producer/consumer**, **idempotency**, **eventual consistency**

### Extras (pick any)
- Dependabot, pre-commit hooks mirroring CI, coverage comments on PRs
- Matrix builds across Python versions
- Load test with Locust and a simple metrics endpoint
- Invite a friend to review PRs, or review theirs

## Progress

Claude: update this section at the end of each session.

- [ ] Session 1 — Repo setup
- [ ] Session 2 — CI basics
- [ ] Session 3 — Core features with the full loop
- [ ] Session 4 — Releases and tags
- [ ] Session 5 — Postgres and the repository pattern
- [ ] Session 6 — Git hard scenarios, part 1
- [ ] Session 7 — Caching and rate limiting
- [ ] Session 8 — Git hard scenarios, part 2
- [ ] Session 9 — CD and environments
- [ ] Session 10 — Async processing and idempotency

### Notes
- Session 1 is in progress. Done: ruleset, labels, milestone, board, issues #1–#4, and PR #5 (closes #1). Next: #2 (templates), #3 (`CONTRIBUTING.md`), #4 (project skeleton).
- Struggled with: finding the labels page and renaming board columns. The ruleset also needed fixing: a coverage rule and last-push approval don't suit a solo repo with no CI yet.
- Commands to revisit: `git switch -c`, `git push -u`, `git fetch --prune`, and why `git branch -D` is needed after a squash merge.
- Try next: run #2 through the full loop without step-by-step instructions, then ask for a review.
