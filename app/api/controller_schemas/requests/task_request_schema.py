from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=30)
    description: Optional[str] = Field(None, max_length=150)
    deadline: Optional[datetime] = None
    status: Literal["todo", "doing", "done"] = Field(default="todo")


class TaskCreate(TaskBase):
    """Schema for creating a new task."""


class TaskUpdate(BaseModel):
    """Schema for replacing a task (PUT)."""

    title: str = Field(..., min_length=1, max_length=30)
    description: Optional[str] = Field(None, max_length=150)
    deadline: Optional[datetime] = None
    status: Literal["todo", "doing", "done"]


class TaskPartialUpdate(BaseModel):
    """Schema for partially updating a task (PATCH)."""

    title: Optional[str] = Field(None, min_length=1, max_length=30)
    description: Optional[str] = Field(None, max_length=150)
    deadline: Optional[datetime] = None
    status: Optional[Literal["todo", "doing", "done"]] = None

