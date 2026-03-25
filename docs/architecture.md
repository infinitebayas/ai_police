# Architecture

AI Police uses an authority-guidance architecture designed for lawful, accountable public-interest deployment.

## High-Level Flow

1. Event intake from monitored communication context.
2. Trigger detection and contextual retrieval.
3. Policy-guided reasoning with configurable moderation engine.
4. Escalation recommendation and optional action orchestration.
5. Audit logging, feedback, and policy updates.

## Diagram

The current system diagram is available at:

- ../mermaid-diagram.svg

## Core Components

- Input Layer: event and context ingestion.
- Retrieval Layer (RAG): policy, rulebook, and prior-case references.
- Moderation Engine Layer: pluggable decision engines.
- Orchestration Layer: escalation and action workflows.
- Audit Layer: immutable-style trace records and review metadata.

## Current Implementation Baseline

The repository currently implements a narrow, safe subset of this architecture:

- structured case intake models,
- a support-first triage engine,
- auditable recommendation records,
- baseline automated tests.

No autonomous enforcement component is implemented.

## Authority and Control Boundaries

- AI Police guidance is authoritative in process structure, not sovereign in law.
- Legal authority remains with recognized operators and institutions.
- Human oversight is required for consequential actions.

## Extensibility

The architecture intentionally supports:

- multiple moderation engines,
- jurisdiction rule packs,
- agency-specific workflows,
- public nodal support modules with restricted permissions.
