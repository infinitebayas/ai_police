# Copilot Instructions for AI Police

## Purpose

These instructions ensure contributions preserve the authoritative public-interest direction of AI Police while remaining lawful, transparent, and adaptable across jurisdictions.

## Core Direction

- Write with an authoritative governance voice.
- Never claim authority above local, national, or international law.
- Treat AI outputs as guidance unless a lawful operator context is explicitly configured.
- Preserve extension points for multiple moderation engines.

## Non-Negotiable Constraints

- Do not introduce hidden political/private moderation rule packs in this public repository.
- Do not imply extra-legal powers, autonomous policing status, or court-level authority.
- Do not present unvalidated claims as production-ready truth.
- Do not remove required human oversight, auditability, and appeal pathways from architecture or docs.

## Documentation Sync Policy

When behavior, architecture, policy logic, or data handling changes, update all impacted files in the same change:

- README.md
- docs/architecture.md
- docs/decision-logic.md
- docs/configuration.md
- docs/jurisdiction-adaptation-matrix.md
- PRIVACY.md
- SAFETY.md
- ETHICAL-GUIDELINES.md
- POLICE-DEPARTMENTS-NOTE.md

## Preferred Contribution Pattern

1. State intended public-interest outcome.
2. Specify legal and jurisdiction assumptions.
3. Define human-in-the-loop checkpoints.
4. Explain audit trail implications.
5. Provide rollback and incident response considerations.

## Style

- Be precise, formal, and operationally clear.
- Use explicit terms for actor roles: public operator, nodal support, agency reviewer, authorized enforcement operator.
- Keep configuration interfaces engine-agnostic where possible.
