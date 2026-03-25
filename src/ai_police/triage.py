from __future__ import annotations

from .models import CaseContext, Recommendation, RecommendationTier, ReviewChannel


class TriageEngine:
    """Support-first recommendation engine.

    This engine is intentionally limited to non-punitive routing and review guidance.
    It does not produce autonomous enforcement outputs.
    """

    def recommend(self, case: CaseContext) -> Recommendation:
        rationale: list[str] = []
        actions: list[str] = []

        if case.imminent_threat:
            rationale.append("The case indicates an immediate safety concern.")
            actions.append("Route to emergency review with an accountable human operator.")
            actions.append("Preserve available evidence and log the recommendation path.")
            return Recommendation(
                tier=RecommendationTier.SUPERVISED_ESCALATION,
                review_channel=ReviewChannel.EMERGENCY_REVIEW,
                rationale=rationale,
                actions=actions,
            )

        if case.involves_child and case.exploitation_indicator:
            rationale.append("The case involves a child and a possible exploitation indicator.")
            actions.append("Route to child-safety or welfare review before any punitive step.")
            actions.append("Limit handling to trained reviewers and preserve audit logs.")
            return Recommendation(
                tier=RecommendationTier.SUPERVISED_ESCALATION,
                review_channel=ReviewChannel.WELFARE_OR_SUPPORT,
                rationale=rationale,
                actions=actions,
            )

        if case.crisis_context:
            rationale.append("The case occurs in a crisis or conflict-sensitive context.")
            actions.append("Use referral-first handling with heightened confidentiality.")
            actions.append("Escalate only through supervised civilian protection channels.")
            return Recommendation(
                tier=RecommendationTier.SUPPORT,
                review_channel=ReviewChannel.WELFARE_OR_SUPPORT,
                rationale=rationale,
                actions=actions,
            )

        if case.cyberbullying_indicator:
            rationale.append("The case indicates possible cyberbullying or peer harassment.")
            actions.append("Preserve evidence and guide reporting to platforms or school/community channels.")
            actions.append("Escalate to agency review only if legal thresholds or threats are present.")
            return Recommendation(
                tier=RecommendationTier.SUPPORT,
                review_channel=ReviewChannel.SCHOOL_OR_COMMUNITY,
                rationale=rationale,
                actions=actions,
            )

        if case.harassment_indicator or case.involves_woman:
            rationale.append("The case may require survivor-centered support and structured review.")
            actions.append("Offer support-first routing and plain-language reporting guidance.")
            actions.append("Use agency review only where the jurisdiction profile requires it.")
            return Recommendation(
                tier=RecommendationTier.SUPPORT,
                review_channel=ReviewChannel.WELFARE_OR_SUPPORT,
                rationale=rationale,
                actions=actions,
            )

        rationale.append("No urgent or specialized indicator was detected from the submitted context.")
        actions.append("Monitor the case and request additional context if needed.")
        actions.append("Keep a minimal audit record for transparency.")
        return Recommendation(
            tier=RecommendationTier.MONITOR,
            review_channel=ReviewChannel.PLATFORM,
            rationale=rationale,
            actions=actions,
        )
