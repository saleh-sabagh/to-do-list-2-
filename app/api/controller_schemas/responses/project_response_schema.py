from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class ProjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str] = None


class ProjectWithTasks(ProjectRead):
    tasks: List["TaskRead"] = []


from app.api.controller_schemas.responses.task_response_schema import TaskRead  # noqa: E402

