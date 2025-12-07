from datetime import datetime
from typing import Literal
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), nullable=False)
    description = Column(String(150))
    deadline = Column(DateTime)
    status = Column(String(10), default="todo")
    closed_at = Column(DateTime, nullable=True)   
    project_id = Column(Integer, ForeignKey("projects.id"))

    # رابطه با پروژه
    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, project_id={self.project_id})>"

    def change_title(self, new_title: str) -> None:
        if not (1 <= len(new_title) <= 30):
            raise ValueError("Task title must be 1-30 characters")
        self.title = new_title

    def change_description(self, new_description: str) -> None:
        if len(new_description) > 150:
            raise ValueError("Task description must be <= 150 characters")
        self.description = new_description

    def change_status(self, new_status: Literal["todo", "doing", "done"]) -> None:
        if new_status not in ("todo", "doing", "done"):
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status

    def change_deadline(self, new_deadline: datetime) -> None:
        if new_deadline:
            try:
                deadline_date = datetime.strptime(new_deadline, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            if deadline_date < datetime.now():
                raise ValueError("Deadline cannot be in the past.")
            self.deadline = deadline_date
        else:
            self.deadline = None

    def task_status(self) -> Literal["todo", "doing", "done"]:
        return self.status
