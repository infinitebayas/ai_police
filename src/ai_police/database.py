from __future__ import annotations

import json
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Index, MetaData, String, Table, Text, create_engine, insert
from sqlalchemy.schema import CreateIndex, CreateTable

from .config import JurisdictionProfile
from .models import CaseContext, Recommendation

metadata = MetaData()

assessment_records = Table(
    "assessment_records",
    metadata,
    Column("id", String(36), primary_key=True),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("profile_name", String(255), nullable=False, index=True),
    Column("profile_mode", String(64), nullable=False),
    Column("jurisdiction", String(128), nullable=False, index=True),
    Column("summary", Text, nullable=False),
    Column("involves_child", Boolean, nullable=False, default=False),
    Column("involves_woman", Boolean, nullable=False, default=False),
    Column("imminent_threat", Boolean, nullable=False, default=False),
    Column("exploitation_indicator", Boolean, nullable=False, default=False),
    Column("cyberbullying_indicator", Boolean, nullable=False, default=False),
    Column("harassment_indicator", Boolean, nullable=False, default=False),
    Column("crisis_context", Boolean, nullable=False, default=False),
    Column("evidence_available", Boolean, nullable=False, default=False),
    Column("requested_by_public_nodal_support", Boolean, nullable=False, default=False),
    Column("case_tags_json", Text, nullable=False),
    Column("recommendation_tier", String(64), nullable=False, index=True),
    Column("review_channel", String(64), nullable=False),
    Column("rationale_json", Text, nullable=False),
    Column("actions_json", Text, nullable=False),
    Column("requires_human_review", Boolean, nullable=False, default=True),
    Column("audit_record_json", Text, nullable=False),
)

Index("ix_assessment_records_created_at", assessment_records.c.created_at)


class DatabaseStore:
    def __init__(self, database_url: str, *, echo: bool = False) -> None:
        self.database_url = database_url
        self.engine = create_engine(database_url, echo=echo, future=True)

    def init_schema(self) -> None:
        metadata.create_all(self.engine)

    def save_assessment(
        self,
        *,
        case: CaseContext,
        profile: JurisdictionProfile,
        recommendation: Recommendation,
        audit_record: dict[str, Any],
    ) -> str:
        record_id = str(uuid4())
        payload = {
            "id": record_id,
            "created_at": datetime.now(UTC),
            "profile_name": profile.name,
            "profile_mode": profile.mode,
            "jurisdiction": case.jurisdiction,
            "summary": case.summary,
            "involves_child": case.involves_child,
            "involves_woman": case.involves_woman,
            "imminent_threat": case.imminent_threat,
            "exploitation_indicator": case.exploitation_indicator,
            "cyberbullying_indicator": case.cyberbullying_indicator,
            "harassment_indicator": case.harassment_indicator,
            "crisis_context": case.crisis_context,
            "evidence_available": case.evidence_available,
            "requested_by_public_nodal_support": case.requested_by_public_nodal_support,
            "case_tags_json": _json_dumps(list(case.tags)),
            "recommendation_tier": recommendation.tier.value,
            "review_channel": recommendation.review_channel.value,
            "rationale_json": _json_dumps(recommendation.rationale),
            "actions_json": _json_dumps(recommendation.actions),
            "requires_human_review": recommendation.requires_human_review,
            "audit_record_json": _json_dumps(audit_record),
        }
        with self.engine.begin() as connection:
            connection.execute(insert(assessment_records).values(**payload))
        return record_id


def export_schema_sql(dialect_name: str) -> str:
    dialect = _dialect_for_name(dialect_name)
    statements = [str(CreateTable(assessment_records).compile(dialect=dialect)).strip() + ";"]
    for index in assessment_records.indexes:
        statements.append(str(CreateIndex(index).compile(dialect=dialect)).strip() + ";")
    return "\n\n".join(statements) + "\n"


def _dialect_for_name(dialect_name: str):
    normalized = dialect_name.lower()
    if normalized == "postgresql":
        from sqlalchemy.dialects.postgresql import dialect

        return dialect()
    if normalized in {"mysql", "mariadb"}:
        from sqlalchemy.dialects.mysql import dialect

        return dialect()
    raise ValueError(f"Unsupported dialect: {dialect_name}")


def _json_dumps(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=True, sort_keys=True)
