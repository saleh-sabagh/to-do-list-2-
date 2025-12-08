# CLI Deprecation Notice

The legacy CLI remains available for backward compatibility but will be removed after Phase 3 once the FastAPI Web API is adopted.

- **Announcement (now):** CLI shows a runtime warning on start. No new features will be added.
- **Migration window (Phase 3):** Please switch scripts/integrations to the FastAPI endpoints under `/api/v1`. Report gaps via issues/PR comments.
- **Removal (Phase 4):** CLI entrypoint (`main.py`) will be removed after confirmation.

Recommended action:
1. Stand up the API: `poetry run uvicorn app.main:app --reload`.
2. Use the OpenAPI docs at `/docs` to migrate commands to HTTP calls.
3. Confirm you no longer rely on the CLI before Phase 4.

