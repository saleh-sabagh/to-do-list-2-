import os
from typing import ClassVar
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    description = Column(String(150))

    # رابطه با Task
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

    MAX_TASKS: ClassVar[int] = int(os.getenv("MAX_NUMBER_OF_TASK", 10))

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name})>"

    def change_name(self, new_name: str) -> None:
        if len(new_name) < 1 or len(new_name) > 30:
            raise ValueError("Project name must be 1-30 characters")
        self.name = new_name

    def change_description(self, new_description: str | None) -> None:
        if new_description is None:
            self.description = None
            return
        if len(new_description) > 150:
            raise ValueError("Project description must be <= 150 characters")
        self.description = new_description
