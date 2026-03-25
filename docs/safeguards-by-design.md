# Safeguards by Design

This document defines the safeguards required for any public-interest deployment of AI Police.

## Core Principle

The system should reduce harm without creating new abuse pathways.

## Required Safeguards

### 1. Human Oversight

- Consequential actions require human review.
- Role boundaries must be explicit.
- Children and survivor-related cases should receive elevated review protections.

### 2. Privacy and Data Minimization

- Collect the minimum data required for lawful support and review.
- Avoid broad retention by default.
- Separate welfare/support notes from investigative records where law requires it.

### 3. Safe Escalation Logic

- Prefer referral and support over punishment.
- Require confidence checks before escalation.
- Use jurisdiction-aware rules before recommending any high-severity step.

### 4. Anti-Bias and Fairness Controls

- Review rule packs for discriminatory effects.
- Monitor false positives affecting women, children, minorities, and displaced people.
- Require periodic revalidation of language and risk models.

### 5. Auditability

- Log intake, recommendation, and approval steps.
- Preserve rationale for escalations.
- Enable retrospective review and correction.

### 6. Appeal and Correction

- Provide a path for challenge, review, and reversal.
- Ensure records can be corrected where lawful.
- Distinguish between allegations, recommendations, and verified findings.

### 7. Conflict-Sensitive Controls

- Use the strictest review threshold in conflict-affected settings.
- Avoid coercive or intelligence-style positioning.
- Prioritize civilian protection and service continuity.

## Safe Defaults

- No automatic punitive action.
- No hidden policy triggers.
- No irreversible action without accountable approval.
- No deployment without jurisdiction profile completion.

## Safety Test Questions

- Does this feature reduce reporting or referral friction for vulnerable users?
- Could this feature increase surveillance or coercion risk?
- Does the feature keep women and children safer in practice?
- Can a reviewer reconstruct why the system recommended a step?
- Can a mistaken recommendation be challenged and corrected?
