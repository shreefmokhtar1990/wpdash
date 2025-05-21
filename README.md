
# WP Multisite Dashboard – Local (no Docker)

This repo lets you run backend + React UI entirely on WSL2 Ubuntu.

## Quick start

```bash
sudo apt update && sudo apt install python3.12 python3.12-venv      mariadb-server redis-server nodejs npm

git clone <repo> wpdash
cd wpdash
git submodule update --init --recursive   # pulls Volt React dashboard
cp .env.example .env
./scripts/setup.sh        # creates .venv, installs Python deps, builds React

make migrate              # Alembic -> creates tables
make seed                 # inserts admin user / demo WP site
make run                  # Flask http://localhost:8000
npm --prefix frontend/volt start   # React dev server http://localhost:3000
```

Login with **admin@example.com / password** then add more sites.
# wpdash
