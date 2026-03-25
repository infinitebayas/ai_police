from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .config import JurisdictionProfile
from .models import CaseContext
from .service import AssessmentResult


def serialize_profile(profile: JurisdictionProfile) -> dict[str, Any]:
    payload = asdict(profile)
    payload["allowed_review_channels"] = [channel.value for channel in profile.allowed_review_channels]
    return payload


def serialize_case(case: CaseContext) -> dict[str, Any]:
    return asdict(case)


def serialize_result(result: AssessmentResult, profile: JurisdictionProfile, case: CaseContext) -> dict[str, Any]:
    return {
        "profile": serialize_profile(profile),
        "case": serialize_case(case),
        "recommendation": {
            "tier": result.recommendation.tier.value,
            "review_channel": result.recommendation.review_channel.value,
            "rationale": result.recommendation.rationale,
            "actions": result.recommendation.actions,
            "requires_human_review": result.recommendation.requires_human_review,
        },
        "audit_record": result.audit_record,
    }
