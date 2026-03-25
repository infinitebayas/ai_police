# GitHub Publish Checklist

Use this checklist before making the repository public or promoting it on social media.

## Repository Basics

- Confirm the repository name, description, and visibility.
- Confirm the canonical license file is present: `LICENSE`.
- Confirm contact policy is present in `CONTACT.md`.
- Confirm README links resolve to real files.
- Confirm all example `.env` files are templates only and contain no secrets.

## Documentation Review

- Read `README.md` from the perspective of a first-time visitor.
- Confirm deployment options are documented for Python, API, Docker, Linux VPS, and Azure.
- Confirm database support is documented for PostgreSQL, MySQL, and MariaDB.
- Confirm government-readiness and compliance notes are present and do not make unsupported certification claims.
- Confirm public-contact instructions point to the approved public profiles.

## Technical Validation

- Run `python -m pytest`.
- Run `python -m ai_police show-settings`.
- Run `python -m ai_police recommend --profile jurisdiction-profiles/us-support.json --case examples/cases/us-school-cyberbullying.json --include-audit`.
- Run `python -m ai_police export-schema --dialect postgresql`.
- Run `python -m ai_police export-schema --dialect mysql`.
- Run `python -m ai_police export-schema --dialect mariadb`.
- Run `python scripts/preflight.py`.

## GitHub Readiness

- Confirm `.gitignore` excludes local editor and environment files.
- Confirm `.github/workflows/ci.yml` passes.
- Confirm `.github/workflows/container.yml` is valid.
- Confirm `.github/workflows/release.yml` matches the intended release flow.
- Confirm issue templates and PR template reflect current repo policy.

## Public Communication Review

- Confirm the README explains the project is support-first and law-bounded.
- Confirm no document suggests extra-legal power or autonomous punitive deployment.
- Confirm public readers can find deployment docs quickly.
- Confirm future development scope is documented for the community.
- Confirm `launch-kit.md` reflects the description, topics, and public announcement you want to use.

## Final Push Sequence

1. Review `git status`.
2. Run `git add .`.
3. Create the initial public commit set.
4. Create the GitHub repository and add `origin`.
5. Push to GitHub.
6. Enable GitHub Actions.
7. Add repository topics and social preview.
8. Publish the repository URL.
