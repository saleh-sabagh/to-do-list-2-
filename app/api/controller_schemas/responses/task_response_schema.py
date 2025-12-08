from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    status: str
    closed_at: Optional[datetime] = None
    project_id: int

