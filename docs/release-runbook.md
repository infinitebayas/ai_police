# Release Runbook

This runbook covers the practical release path when there is no live production server yet.

## Goal

Publish a high-quality public repository that is:

- documented,
- testable,
- runnable locally,
- deployment-ready,
- safe for public review.

## Release Without Live Hosting

A live server is not required to publish a credible repository if the following are true:

- local runtime path works,
- API path works,
- UI path works locally,
- container path is documented,
- VPS and cloud paths are documented,
- tests pass,
- example configurations are included,
- release boundaries are explicit.

That is the current target state for this repository.

## Pre-Release Commands

```bash
python -m pip install -e .[dev]
python -m pytest
python -m ai_police show-settings
python -m ai_police recommend --profile jurisdiction-profiles/us-support.json --case examples/cases/us-school-cyberbullying.json --include-audit
python -m ai_police export-schema --dialect postgresql
python scripts/preflight.py
```

## First GitHub Push

This workspace can be prepared fully before a GitHub repository exists. The only external dependency is the final remote creation step.

From this local folder:

```bash
git init -b main
git add .
git commit -m "Initial public release"
```

Then create an empty GitHub repository and connect it:

```bash
git remote add origin <your-github-repository-url>
git push -u origin main
```

After the first push:

- confirm the README renders correctly,
- confirm GitHub Actions starts,
- confirm repository topics and description are set,
- confirm the license is detected by GitHub,
- confirm the issue templates appear correctly.

Use `launch-kit.md` for the initial repository description, topics, release title, and first public announcement copy.

## Local Demo Path

```bash
copy .env.example .env
python -m pip install -e .[api]
python -m ai_police serve
```

Then verify:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/ready`

## Release Tag Path

When ready for a tagged release:

1. update `CHANGELOG.md`
2. ensure tests pass
3. create a tag such as `v0.1.0`
4. push the tag
5. let `.github/workflows/release.yml` build the distribution artifacts

## Suggested Initial Public Positioning

Describe the repo as:

- public-interest governance baseline,
- support-first triage system,
- deployment-flexible developer baseline,
- government-friendly but not certification-claimed,
- open to community extension.

## Social Sharing Guidance

When sharing the repository link publicly, emphasize:

- the repository is open for public review and development,
- multiple deployment paths are supported,
- local and institutional adopters can adapt it through configuration,
- direct contact is via LinkedIn only.

For ready-to-use wording, see `launch-kit.md`.
