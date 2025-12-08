import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

# Configure test database before importing the app
os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")
os.environ.setdefault("SQL_ECHO", "false")

from app.db.base import Base  # noqa: E402
from app.db.session import engine  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def setup_database() -> Generator[None, None, None]:
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_healthcheck():
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_project_and_task_flow():
    client = TestClient(app)

    # Create a project
    project_resp = client.post(
        "/api/v1/projects",
        json={"name": "API Project", "description": "From tests"},
    )
    assert project_resp.status_code == 201, project_resp.text
    project_id = project_resp.json()["id"]

    # List projects
    list_resp = client.get("/api/v1/projects")
    assert list_resp.status_code == 200
    assert any(p["id"] == project_id for p in list_resp.json())

    # Create a task under the project
    task_resp = client.post(
        f"/api/v1/projects/{project_id}/tasks",
        json={"title": "First task", "description": "testing"},
    )
    assert task_resp.status_code == 201, task_resp.text
    task_id = task_resp.json()["id"]

    # List tasks for project
    tasks_resp = client.get(f"/api/v1/projects/{project_id}/tasks")
    assert tasks_resp.status_code == 200
    assert any(t["id"] == task_id for t in tasks_resp.json())

    # Fetch task directly
    single_task = client.get(f"/api/v1/tasks/{task_id}")
    assert single_task.status_code == 200
    assert single_task.json()["title"] == "First task"

