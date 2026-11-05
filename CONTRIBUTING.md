# Contributing

Every change follows the same path: issue → branch → small commits → PR → squash-merge.

## Issues

Open an issue before starting work, using the bug report or feature request template when one fits.

## Branches

Create branches from an up-to-date `main`, named `<type>/<issue-number>-<short-description>`:

- `feat/12-link-expiry`
- `fix/18-redirect-404`
- `chore/7-ci-setup`

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org):

| Type | Use for |
|---|---|
| `feat:` | A new feature |
| `fix:` | A bug fix |
| `refactor:` | A code change that doesn't change behavior |
| `test:` | Tests only |
| `docs:` | Documentation only |
| `ci:` | CI/CD workflows |
| `chore:` | Other maintenance |

For example: `feat: add link expiry`.

Mark breaking changes with `feat!:` or a `BREAKING CHANGE:` footer.

## Pull requests

- One issue per PR, linked with `Closes #N`
- Small: aim for under ~300 changed lines
- A PR title in Conventional Commits format, since it becomes the commit title on `main`
- A description covering what changed, why, and how it was tested, since it becomes the commit body on `main`
- Every checklist item checked, both in the PR description and in the issues it closes
- All required checks green before merging
- Squash-merge

The branch is deleted automatically after merging.

## How `main` is protected

A ruleset on `main` enforces the following, with no bypass:

- Changes go through a PR, so no direct pushes
- Squash is the only merge method
- History stays linear, and force pushes are blocked
- The branch can't be deleted
- All review conversations must be resolved before merging
- These checks must pass:
  - `checks`: lint, formatting, type checks and tests
  - `pr-title`: the PR title follows Conventional Commits
  - `checklists`: no unchecked items in the PR description or the issues it closes
- The branch must be up to date with `main`, so checks run against the latest code

Approvals aren't required, because this is a solo project.
