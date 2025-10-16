from datetime import datetime
from typing import Literal


class Task:

    def __init__(self, id: str, title: str, description: str, deadline: str) -> None:
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
        if not (1 <= len(new_title) <= 30):
            raise ValueError("task's title must be less than 30 characters and not empty")
        self.title = new_title

    def change_description(self, new_description: str) -> None:
        if not (1 <= len(new_description) <= 150):
            raise ValueError("task's description must be less than 150 characters and not empty")
        self.description = new_description

    def change_status(self, new_status: Literal["todo", "doing", "done"]) -> None:
        if new_status not in ("todo", "doing", "done"):
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status

    def change_deadline(self, new_deadline: str) -> None:
        try:
            deadline_date = datetime.strptime(new_deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        if deadline_date < datetime.now():
            raise ValueError("Deadline cannot be in the past.")
        self.deadline = deadline_date

    def task_status(self) -> Literal["todo", "doing", "done"]:
        return self.status

   