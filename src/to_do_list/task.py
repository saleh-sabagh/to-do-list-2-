from datetime import datetime
from typing import Literal


class Task:
    """Represents a task with a title, description, deadline, and status."""

    def __init__(self, id: str, title: str, description: str, deadline: str) -> None:
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

        if not (1 <= len(description) <= 150):
            raise ValueError("task's description must be less than 150 characters and not empty")

        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if deadline_date < datetime.now():
            raise ValueError("Deadline cannot be in the past.")

        self.id: str = id
        self.title: str = title
        self.description: str = description
        self.deadline: datetime = deadline_date
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
        if not (1 <= len(new_description) <= 150):
            raise ValueError("task's description must be less than 150 characters and not empty")
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
        try:
            deadline_date = datetime.strptime(new_deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if deadline_date < datetime.now():
            raise ValueError("Deadline cannot be in the past.")

        self.deadline = deadline_date

    def task_status(self) -> Literal["todo", "doing", "done"]:
        """Return the current status of the task.

        Returns:
            Literal["todo", "doing", "done"]: Task's status.
        """
        return self.status

    def __repr__(self) -> str:
        """Return a string representation of the task.

        Returns:
            str: Representation showing task id and title.
        """
        return f"Task(id='{self.id}', title='{self.title}')"
