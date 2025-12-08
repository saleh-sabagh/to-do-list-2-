from typing import Optional

from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    description: Optional[str] = Field(None, max_length=150)


class ProjectCreate(ProjectBase):
    """Schema for creating a project."""


class ProjectUpdate(ProjectBase):
    """Schema for replacing a project."""


class ProjectPartialUpdate(BaseModel):
    """Schema for partially updating a project."""

    name: Optional[str] = Field(None, min_length=1, max_length=30)
    description: Optional[str] = Field(None, max_length=150)

