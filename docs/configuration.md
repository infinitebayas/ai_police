# Configuration

AI Police configuration should be explicit, auditable, and jurisdiction-aware.

## Configuration Domains

- Jurisdiction profile
- Policy rule packs
- Moderation engine selection
- Escalation thresholds
- Human approval gates
- Audit and retention settings

## Recommended Config Model

- global: common defaults
- jurisdiction: legal constraints and speech boundaries
- institution: agency policy and workflow ownership
- engine: moderation model and retrieval parameters
- operations: incident handling and rollback

## Mandatory Configuration Controls

- Disabled-by-default consequential action pathways.
- Named reviewer requirements for escalations.
- Versioned policy packs with change history.
- Clear fallback behavior when confidence is low.

## Multi-Engine Support

The system should permit multiple moderation engines and retrieval backends through stable interfaces.

Avoid hard-coupling policy logic to a single vendor or model.

## Current Profile Format

The current runnable scaffold uses JSON jurisdiction profiles stored in `jurisdiction-profiles/`.

Each profile can define:

- profile name and mode,
- allowed review channels,
- whether all outcomes require human review,
- crisis-sensitive handling,
- child and women safety priority flags,
- public nodal support enablement,
- support resources and notes.
