# 🗂️ To-Do List (FastAPI Phase 3)

FastAPI Web API for managing projects and tasks, built on the existing service/repository layer. The legacy CLI remains available but is now deprecated (see `DEPRECATION.md`).

## Stack
- FastAPI + Pydantic
- SQLAlchemy (sync) + Alembic
- PostgreSQL (default) — SQLite supported for local tests
- Poetry for dependency management
- Pytest + httpx for API tests

## Getting started
1. Install Poetry (https://python-poetry.org/docs/#installation)
2. Install deps
   ```bash
   poetry install
   ```
3. Configure environment
   ```bash
   cp .env.example .env
   # update DATABASE_URL=postgresql+psycopg2://user:pass@localhost:5432/tododb
   ```
4. Run migrations (local/dev DB)
   ```bash
   alembic upgrade head
   ```
5. Launch API
   ```bash
   poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
6. Open docs: http://localhost:8000/docs (or Redoc at `/redoc`)

## Endpoints (v1)
- `GET /api/v1/health` – healthcheck
- `GET /api/v1/projects` / `POST /api/v1/projects`
- `GET /api/v1/projects/{project_id}` / `PUT` / `PATCH` / `DELETE`
- `GET /api/v1/projects/{project_id}/tasks` / `POST`
- `GET /api/v1/tasks` / `GET|PUT|PATCH|DELETE /api/v1/tasks/{task_id}`

## CLI (deprecated)
The CLI still works for now:
```bash
poetry run python main.py
```
On start it emits a deprecation warning. No new features will be added; migrate to the API.

## Testing
```bash
DATABASE_URL=sqlite:///./test.db poetry run pytest -q
```

## Development notes
- Environment secrets live in `.env` (not committed).
- CI runs linting (ruff/black/isort) and tests via GitHub Actions (`.github/workflows/ci.yml`).
- Service and repository layers remain reusable by both CLI and API.

