CREATE TABLE assessment_records (
    id VARCHAR(36) PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL,
    profile_name VARCHAR(255) NOT NULL,
    profile_mode VARCHAR(64) NOT NULL,
    jurisdiction VARCHAR(128) NOT NULL,
    summary TEXT NOT NULL,
    involves_child BOOLEAN NOT NULL DEFAULT FALSE,
    involves_woman BOOLEAN NOT NULL DEFAULT FALSE,
    imminent_threat BOOLEAN NOT NULL DEFAULT FALSE,
    exploitation_indicator BOOLEAN NOT NULL DEFAULT FALSE,
    cyberbullying_indicator BOOLEAN NOT NULL DEFAULT FALSE,
    harassment_indicator BOOLEAN NOT NULL DEFAULT FALSE,
    crisis_context BOOLEAN NOT NULL DEFAULT FALSE,
    evidence_available BOOLEAN NOT NULL DEFAULT FALSE,
    requested_by_public_nodal_support BOOLEAN NOT NULL DEFAULT FALSE,
    case_tags_json TEXT NOT NULL,
    recommendation_tier VARCHAR(64) NOT NULL,
    review_channel VARCHAR(64) NOT NULL,
    rationale_json TEXT NOT NULL,
    actions_json TEXT NOT NULL,
    requires_human_review BOOLEAN NOT NULL DEFAULT TRUE,
    audit_record_json TEXT NOT NULL
);

CREATE INDEX ix_assessment_records_created_at ON assessment_records (created_at);
CREATE INDEX ix_assessment_records_jurisdiction ON assessment_records (jurisdiction);
CREATE INDEX ix_assessment_records_profile_name ON assessment_records (profile_name);
CREATE INDEX ix_assessment_records_recommendation_tier ON assessment_records (recommendation_tier);
