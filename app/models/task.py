from datetime import datetime, timezone
from typing import Literal, Union
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

    def change_description(self, new_description: str | None) -> None:
        if new_description is None:
            self.description = None
            return
        if len(new_description) > 150:
            raise ValueError("Task description must be <= 150 characters")
        self.description = new_description

    def change_status(self, new_status: Literal["todo", "doing", "done"]) -> None:
        if new_status not in ("todo", "doing", "done"):
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status

    def change_deadline(self, new_deadline: Union[datetime, str, None]) -> None:
        """
        Accept datetime objects or ISO date strings (YYYY-MM-DD).
        """
        if new_deadline:
            if isinstance(new_deadline, str):
                try:
                    deadline_date = datetime.strptime(new_deadline, "%Y-%m-%d")
                except ValueError as exc:
                    raise ValueError("Invalid date format. Use YYYY-MM-DD.") from exc
            elif isinstance(new_deadline, datetime):
                deadline_date = new_deadline
            else:
                raise ValueError("Deadline must be datetime, YYYY-MM-DD string, or None.")

            # Normalize timezone-aware datetimes to naive UTC to avoid comparison errors
            if deadline_date.tzinfo and deadline_date.tzinfo.utcoffset(deadline_date) is not None:
                deadline_date = deadline_date.astimezone(timezone.utc).replace(tzinfo=None)

            now = datetime.now()
            if deadline_date < now:
                raise ValueError("Deadline cannot be in the past.")
            self.deadline = deadline_date
        else:
            self.deadline = None

    def task_status(self) -> Literal["todo", "doing", "done"]:
        return self.status
