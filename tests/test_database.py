from pathlib import Path

from sqlalchemy import create_engine, select

from ai_police.config import load_profile
from ai_police.database import DatabaseStore, assessment_records, export_schema_sql
from ai_police.models import CaseContext
from ai_police.service import AssessmentService


def test_export_schema_contains_core_table_for_supported_dialects() -> None:
    postgres_sql = export_schema_sql('postgresql')
    mysql_sql = export_schema_sql('mysql')
    mariadb_sql = export_schema_sql('mariadb')

    assert 'assessment_records' in postgres_sql
    assert 'assessment_records' in mysql_sql
    assert 'assessment_records' in mariadb_sql


def test_database_store_persists_assessment_to_sqlite() -> None:
    store = DatabaseStore('sqlite+pysqlite:///:memory:')
    store.init_schema()

    profile = load_profile('jurisdiction-profiles/us-support.json')
    case = CaseContext(
        jurisdiction='US',
        summary='Stored cyberbullying assessment',
        involves_child=True,
        cyberbullying_indicator=True,
    )
    result = AssessmentService(store=store).assess(case, profile)

    assert result.record_id is not None

    with store.engine.connect() as connection:
        row = connection.execute(select(assessment_records.c.id, assessment_records.c.jurisdiction)).one()

    assert row.id == result.record_id
    assert row.jurisdiction == 'US'
