# Database Support

AI Police can run without a database, but it now supports optional persistence for assessment records through SQLAlchemy and portable schema files.

## Supported Database Targets

- PostgreSQL
- MySQL
- MariaDB

## Persistence Model

The current persistence layer stores assessment outputs in one portable table:

- `assessment_records`

This table captures:

- case metadata,
- routing context,
- recommendation tier and channel,
- rationale and actions,
- serialized audit record.

## Schema Files

- `db/schema/postgresql.sql`
- `db/schema/mysql.sql`
- `db/schema/mariadb.sql`

## Compose Examples

For local or server-side multi-container development, the repository also includes:

- `deploy/compose/docker-compose.postgres.yml`
- `deploy/compose/docker-compose.mysql.yml`
- `deploy/compose/docker-compose.mariadb.yml`

These files can be imported directly by teams that want explicit schema control.

## Runtime Variables

- `AI_POLICE_DATABASE_URL`
- `AI_POLICE_DATABASE_ECHO`
- `AI_POLICE_DATABASE_AUTO_INIT`

## Typical URLs

### PostgreSQL

`postgresql+psycopg://ai_police:password@127.0.0.1:5432/ai_police`

### MySQL

`mysql+pymysql://ai_police:password@127.0.0.1:3306/ai_police`

### MariaDB

`mysql+pymysql://ai_police:password@127.0.0.1:3306/ai_police`

## Initialization Options

Use one of these approaches:

1. Import the vendor-specific SQL file manually.
2. Use the CLI `init-db` command when `AI_POLICE_DATABASE_URL` is configured.
3. Enable `AI_POLICE_DATABASE_AUTO_INIT=true` for controlled environments where automatic schema creation is acceptable.

## Useful CLI Commands

- `python -m ai_police init-db`
- `python -m ai_police export-schema --dialect postgresql`
- `python -m ai_police export-schema --dialect mysql`
- `python -m ai_police export-schema --dialect mariadb`

## Development Note

The app remains usable without a database. Persistence activates only when `AI_POLICE_DATABASE_URL` is set.
