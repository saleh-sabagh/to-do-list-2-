from datetime import datetime
from typing import Literal

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
class Task(Base):
    """Represents a task with a title, description, deadline, and status."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), nullable=False)
    description = Column(String(150))
    deadline = Column(DateTime)
    status = Column(String(10), default="todo")
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", backref="tasks")
    
    def __init__(self, id: int, title: str, description: str, deadline: str) -> None:
        """Initialize a Task instance.

        Args:
            id (str): Unique identifier for the task.
            title (str): Title of the task (1-30 characters).
            description (str): Description of the task (1-150 characters).
            deadline (str): Deadline date in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If title or description lengths are invalid, 
                        if the deadline format is invalid, 
                        or if the deadline is in the past.
        """
        if not (1 <= len(title) <= 30):
            raise ValueError("task's title must be less than 30 characters and not empty")

        if not (len(description) <= 150):
            raise ValueError("task's description must be less than 150 characters!")

        if deadline:
            try:
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
                self.deadline: datetime = deadline_date

            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")

            if deadline_date < datetime.now():
                raise ValueError("Deadline cannot be in the past.")
        else:
            self.deadline = deadline
        self.id: str = id
        self.title: str = title
        self.description: str = description
        self.status: Literal["todo", "doing", "done"] = "todo"

    def change_title(self, new_title: str) -> None:
        """Change the task's title.

        Args:
            new_title (str): New title for the task (1-30 characters).

        Raises:
            ValueError: If new_title length is invalid.
        """
        if not (1 <= len(new_title) <= 30):
            raise ValueError("task's title must be less than 30 characters and not empty")
        self.title = new_title

    def change_description(self, new_description: str) -> None:
        """Change the task's description.

        Args:
            new_description (str): New description for the task (1-150 characters).

        Raises:
            ValueError: If new_description length is invalid.
        """
        if not (len(new_description) <= 150):
            raise ValueError("task's description must be less than 150 characters")
        self.description = new_description

    def change_status(self, new_status: Literal["todo", "doing", "done"]) -> None:
        """Change the task's status.

        Args:
            new_status (Literal["todo", "doing", "done"]): New status of the task.

        Raises:
            ValueError: If new_status is not one of "todo", "doing", or "done".
        """
        if new_status not in ("todo", "doing", "done"):
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status

    def change_deadline(self, new_deadline: str) -> None:
        """Change the task's deadline.

        Args:
            new_deadline (str): New deadline date in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the date format is invalid or the date is in the past.
        """
        
        if new_deadline:
            try:
                deadline_date = datetime.strptime(new_deadline, "%Y-%m-%d")
                self.deadline = deadline_date

            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")

            if deadline_date < datetime.now():
                raise ValueError("Deadline cannot be in the past.")
        else:
            self.deadline = new_deadline

    def task_status(self) -> Literal["todo", "doing", "done"]:
        """Return the current status of the task.

        Returns:
            Literal["todo", "doing", "done"]: Task's status.
        """
        return self.status
