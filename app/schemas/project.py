from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    description: Optional[str] = Field(None, max_length=150)


class ProjectCreate(ProjectBase):
    """Schema for creating a project."""


class ProjectUpdate(ProjectBase):
    """Schema for replacing a project (PUT)."""


class ProjectPartialUpdate(BaseModel):
    """Schema for partially updating a project (PATCH)."""

    name: Optional[str] = Field(None, min_length=1, max_length=30)
    description: Optional[str] = Field(None, max_length=150)


class ProjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str] = None


class ProjectWithTasks(ProjectRead):
    tasks: List["TaskRead"] = []


# Late import to avoid circular dependency
from app.schemas.task import TaskRead  # noqa: E402

