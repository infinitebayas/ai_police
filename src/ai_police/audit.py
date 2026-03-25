from __future__ import annotations

from dataclasses import asdict
from datetime import UTC, datetime
from typing import Any

from .models import CaseContext, Recommendation


def build_audit_record(case: CaseContext, recommendation: Recommendation) -> dict[str, Any]:
    """Create a minimal, serializable audit record for a recommendation."""

    return {
        "created_at": datetime.now(UTC).isoformat(),
        "case": asdict(case),
        "recommendation": {
            "tier": recommendation.tier.value,
            "review_channel": recommendation.review_channel.value,
            "rationale": recommendation.rationale,
            "actions": recommendation.actions,
            "requires_human_review": recommendation.requires_human_review,
        },
    }
