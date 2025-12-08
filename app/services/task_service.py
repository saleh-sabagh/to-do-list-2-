from datetime import datetime
from typing import List, Optional

from app.models.task import Task
from app.repositories.task_sql_repository import SQLAlchemyTaskRepository

class TaskService:
    """Business logic for tasks."""

    def __init__(self, task_repo: SQLAlchemyTaskRepository):
        self.task_repo = task_repo

    def get_task(self, task_id: int) -> Task:
        task = self.task_repo.get_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        return task

    def update_task_title(self, task_id: int, new_title: str) -> Task:
        task = self.get_task(task_id)
        task.change_title(new_title)
        self.task_repo.save(task)
        return task

    def update_task_description(self, task_id: int, new_description: str) -> Task:
        task = self.get_task(task_id)
        task.change_description(new_description)
        self.task_repo.save(task)
        return task

    def update_task_deadline(self, task_id: int, new_deadline: datetime | str | None) -> Task:
        task = self.get_task(task_id)
        task.change_deadline(new_deadline)
        self.task_repo.save(task)
        return task

    def update_task_status(self, task_id: int, new_status: str) -> Task:
        task = self.get_task(task_id)
        task.change_status(new_status)
        self.task_repo.save(task)
        return task

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        deadline: datetime | str | None = None,
        status: Optional[str] = None,
        title_provided: bool = False,
        description_provided: bool = False,
        deadline_provided: bool = False,
        status_provided: bool = False,
    ) -> Task:
        task = self.get_task(task_id)

        if title_provided:
            if title is None:
                raise ValueError("Title cannot be null")
            task.change_title(title)
        if description_provided:
            if description is None:
                task.description = None
            else:
                task.change_description(description)
        if deadline_provided:
            task.change_deadline(deadline)
        if status_provided:
            if status is None:
                raise ValueError("Status cannot be null")
            task.change_status(status)

        self.task_repo.save(task)
        return task

    def delete_task(self, task_id: int) -> None:
        self.get_task(task_id)
        self.task_repo.delete(task_id)

    def get_all_tasks(self, skip: int = 0, limit: int = 100) -> List[Task]:
        return self.task_repo.all(skip=skip, limit=limit)

    def get_tasks_by_project(self, project_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        return self.task_repo.get_by_project(project_id, skip=skip, limit=limit)
