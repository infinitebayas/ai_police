from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .audit import build_audit_record
from .config import JurisdictionProfile
from .models import CaseContext, Recommendation, RecommendationTier, ReviewChannel
from .triage import TriageEngine


@dataclass(slots=True)
class AssessmentResult:
    profile_name: str
    recommendation: Recommendation
    audit_record: dict[str, object]
    record_id: str | None = None


class AssessmentStore(Protocol):
    def save_assessment(
        self,
        *,
        case: CaseContext,
        profile: JurisdictionProfile,
        recommendation: Recommendation,
        audit_record: dict[str, object],
    ) -> str: ...


class AssessmentService:
    def __init__(self, engine: TriageEngine | None = None, store: AssessmentStore | None = None) -> None:
        self._engine = engine or TriageEngine()
        self._store = store

    def assess(self, case: CaseContext, profile: JurisdictionProfile) -> AssessmentResult:
        recommendation = self._engine.recommend(case)
        adjusted = self._apply_profile_guards(case, recommendation, profile)
        audit_record = build_audit_record(case, adjusted)
        audit_record["profile_name"] = profile.name
        audit_record["profile_mode"] = profile.mode
        record_id: str | None = None
        if self._store is not None:
            record_id = self._store.save_assessment(
                case=case,
                profile=profile,
                recommendation=adjusted,
                audit_record=audit_record,
            )
            audit_record["record_id"] = record_id
        return AssessmentResult(
            profile_name=profile.name,
            recommendation=adjusted,
            audit_record=audit_record,
            record_id=record_id,
        )

    def _apply_profile_guards(
        self,
        case: CaseContext,
        recommendation: Recommendation,
        profile: JurisdictionProfile,
    ) -> Recommendation:
        rationale = list(recommendation.rationale)
        actions = list(recommendation.actions)
        review_channel = recommendation.review_channel
        tier = recommendation.tier

        if review_channel not in profile.allowed_review_channels:
            review_channel = self._fallback_channel(profile)
            rationale.append(
                "The requested review channel is not enabled by the jurisdiction profile, so the recommendation was routed to a safer permitted channel."
            )
            actions.append(f"Use the profile-approved review channel: {review_channel.value}.")
            if tier is RecommendationTier.MONITOR:
                tier = RecommendationTier.SUPPORT

        if case.requested_by_public_nodal_support:
            actions.append("Require named institutional reviewer acknowledgement before case closure.")

        if case.involves_child and profile.child_safety_priority:
            actions.append("Use child-safe handling and minimize repeated disclosure requests.")

        if case.involves_woman and profile.women_safety_priority:
            actions.append("Use survivor-centered communication and support routing where available.")

        if profile.crisis_sensitive:
            actions.append("Apply crisis-sensitive confidentiality and least-intrusive handling rules.")

        return Recommendation(
            tier=tier,
            review_channel=review_channel,
            rationale=rationale,
            actions=actions,
            requires_human_review=profile.require_human_review_for_all or recommendation.requires_human_review,
        )

    @staticmethod
    def _fallback_channel(profile: JurisdictionProfile) -> ReviewChannel:
        safe_preference = (
            ReviewChannel.WELFARE_OR_SUPPORT,
            ReviewChannel.SCHOOL_OR_COMMUNITY,
            ReviewChannel.AGENCY_REVIEW,
            ReviewChannel.PLATFORM,
            ReviewChannel.EMERGENCY_REVIEW,
        )
        for channel in safe_preference:
            if channel in profile.allowed_review_channels:
                return channel
        return profile.allowed_review_channels[0]
