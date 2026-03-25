# Quickstart

This quickstart covers repository orientation and documentation-first setup.

## Prerequisites

- Git
- A markdown-capable editor
- Python 3.11+
- Policy and legal review context for your intended jurisdiction

## Steps

1. Review core governance docs: ../README.md, ../SAFETY.md, ../PRIVACY.md, ../ETHICAL-GUIDELINES.md.
2. Review architecture and decision logic: architecture.md and decision-logic.md.
3. Review the safe research pack: social-risk-landscape.md, public-interest-use-cases.md, safeguards-by-design.md, country-adaptation-notes.md, and evaluation-metrics.md.
4. Create your initial jurisdiction profile using jurisdiction-adaptation-matrix.md.
5. Define institutional role mappings and escalation owners.
6. Create a local environment file from `.env.example`.
7. Install the package in editable mode for local work: `python -m pip install -e .[dev]`.
8. Run the baseline tests: `pytest`.
9. Validate one of the example jurisdiction profiles: `python -m ai_police validate-profile --profile jurisdiction-profiles/india-support.json`.
10. Generate a sample recommendation: `python -m ai_police recommend --profile jurisdiction-profiles/us-support.json --case examples/cases/us-school-cyberbullying.json --include-audit`.
11. Run the publish preflight: `python scripts/preflight.py`.
12. Start the local API and open the UI: `python -m pip install -e .[api]` and `python -m ai_police serve`.
13. Proceed to implementation scaffolding after legal and governance sign-off.

## Outcome

You should have a lawful deployment baseline and governance framework before any enforcement-capable implementation is activated.

For publication readiness without a live server, continue with `local-verification.md` and `github-publish-checklist.md`.
