# INTERVENTION REQUIRED

- id: INT-001
  area: "Database credentials"
  description: "Provide a DATABASE_URL for Postgres to run migrations and deploy the API. Current automation used a local SQLite URL for CI/tests."
  options:
    - "Set DATABASE_URL to your development/staging Postgres instance and rerun `alembic upgrade head`."
    - "Keep using SQLite locally (testing only) and supply Postgres credentials before deploying."
  recommended: "Use a managed Postgres instance and store DATABASE_URL in a secure secret store."
  action_by_user: "Add DATABASE_URL to .env (not committed), then run: `poetry install && alembic upgrade head`."
  related_commits:
    - "pending"

