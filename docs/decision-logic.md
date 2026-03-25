# Decision Logic

AI Police decision logic should be auditable, proportional, and legally bounded.

## Decision Pipeline

1. Ingest event context.
2. Retrieve policy and precedent context.
3. Run moderation engine analysis.
4. Assign risk tier and confidence score.
5. Select recommended response tier.
6. Route to human or authorized operator based on severity.
7. Record decision trace for review.

## Response Tiers

- Tier 0: monitor only
- Tier 1: warning/recommendation
- Tier 2: supervised intervention
- Tier 3: authorized consequential action (lawful operator required)

## Control Requirements

- No hidden rule triggers.
- Confidence-aware fallback to human review.
- Jurisdiction policy compatibility checks before action recommendation.
- Mandatory trace records for all tiered outcomes.

## Public Interest Rule

When uncertain, prefer containment and review over punitive escalation.
