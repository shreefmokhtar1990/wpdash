
.PHONY: venv run migrate seed test build-react

venv:
	python3.12 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run:
	. .venv/bin/activate && python -m flask --app backend.app:create_app run -h 0.0.0.0 -p 8000 --reload

migrate:
	. .venv/bin/activate && alembic upgrade head

seed:
	. .venv/bin/activate && python tools/seed_db.py

build-react:
	cd frontend/volt && npm install && npm run build

test:
	. .venv/bin/activate && pytest -q
