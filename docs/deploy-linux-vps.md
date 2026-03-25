# Deploy on a Linux VPS

This path is suitable for self-managed virtual machines, sovereign hosting, intranet deployment, or institutions that prefer direct control over the operating environment.

## Recommended Stack

- Ubuntu LTS or another supported Linux distribution
- Python 3.11+
- reverse proxy such as Nginx
- systemd service management
- optional Docker for container-based operation
- optional PostgreSQL, MySQL, or MariaDB for persistence

## Option A: Native Python Service

### 1. Install system packages

Example on Ubuntu:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nginx
```

### 2. Clone and install

```bash
git clone <your-repo-url> /opt/ai-police
cd /opt/ai-police
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[api]
```

Edit `.env` before starting the service. For example:

- Root domain or subdomain deployment: leave `AI_POLICE_BASE_PATH=` empty.
- Folder deployment such as `/ai-police`: set `AI_POLICE_BASE_PATH=/ai-police`.
- Database persistence: set `AI_POLICE_DATABASE_URL` for PostgreSQL, MySQL, or MariaDB if you want assessment records stored.

### 3. Run locally first

```bash
python -m ai_police serve
```

### 4. Install as a systemd service

Use the example service file in `deploy/linux/ai-police.service`.

```bash
sudo cp deploy/linux/ai-police.service /etc/systemd/system/ai-police.service
sudo systemctl daemon-reload
sudo systemctl enable ai-police
sudo systemctl start ai-police
```

### 5. Configure Nginx

Use the example config in `deploy/linux/nginx-ai-police.conf` and adjust the server name.

For subpath deployments, use `deploy/linux/nginx-ai-police-subpath.conf` and keep `AI_POLICE_BASE_PATH` in `.env` synchronized with the configured path.

```bash
sudo cp deploy/linux/nginx-ai-police.conf /etc/nginx/sites-available/ai-police
sudo ln -s /etc/nginx/sites-available/ai-police /etc/nginx/sites-enabled/ai-police
sudo nginx -t
sudo systemctl reload nginx
```

## Option B: Docker on a VPS

```bash
git clone <your-repo-url>
cd ai_police
cp .env.example .env
docker compose up --build -d
```

## Database Examples on Linux VPS

### PostgreSQL example

Install:

```bash
sudo apt install -y postgresql postgresql-contrib
```

Create database and user:

```bash
sudo -u postgres psql -c "CREATE USER ai_police WITH PASSWORD 'change-me';"
sudo -u postgres psql -c "CREATE DATABASE ai_police OWNER ai_police;"
sudo -u postgres psql -d ai_police -f /opt/ai-police/db/schema/postgresql.sql
```

Set in `.env`:

```env
AI_POLICE_DATABASE_URL=postgresql+psycopg://ai_police:change-me@127.0.0.1:5432/ai_police
```

### MySQL example

Install:

```bash
sudo apt install -y mysql-server
```

Create database and user:

```bash
sudo mysql -e "CREATE DATABASE ai_police;"
sudo mysql -e "CREATE USER 'ai_police'@'localhost' IDENTIFIED BY 'change-me';"
sudo mysql -e "GRANT ALL PRIVILEGES ON ai_police.* TO 'ai_police'@'localhost'; FLUSH PRIVILEGES;"
mysql -u ai_police -p ai_police < /opt/ai-police/db/schema/mysql.sql
```

Set in `.env`:

```env
AI_POLICE_DATABASE_URL=mysql+pymysql://ai_police:change-me@127.0.0.1:3306/ai_police
```

### MariaDB example

Install:

```bash
sudo apt install -y mariadb-server
```

Create database and user:

```bash
sudo mariadb -e "CREATE DATABASE ai_police;"
sudo mariadb -e "CREATE USER 'ai_police'@'localhost' IDENTIFIED BY 'change-me';"
sudo mariadb -e "GRANT ALL PRIVILEGES ON ai_police.* TO 'ai_police'@'localhost'; FLUSH PRIVILEGES;"
mariadb -u ai_police -p ai_police < /opt/ai-police/db/schema/mariadb.sql
```

Set in `.env`:

```env
AI_POLICE_DATABASE_URL=mysql+pymysql://ai_police:change-me@127.0.0.1:3306/ai_police
```

## App-Managed Schema Initialization

If you prefer the app to initialize schema instead of importing SQL manually:

```bash
python -m ai_police init-db
```

Or enable:

```env
AI_POLICE_DATABASE_AUTO_INIT=true
```

## Government-Friendly VPS Notes

For public-sector or sovereign hosting, consider:

- host hardening using CIS guidance,
- SSH access restrictions,
- firewall policy,
- centralized logging,
- backup and restore drills,
- encrypted storage,
- environment-level secrets handling,
- routine patching.

## Validation

After deployment, verify:

- `GET /health`
- `GET /profiles`
- `GET /ready`
- root UI at `/`
- reverse proxy routing
- service restart behavior after reboot
