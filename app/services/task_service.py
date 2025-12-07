from typing import List
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

    def update_task_title(self, task_id: int, new_title: str) -> None:
        task = self.get_task(task_id)
        task.change_title(new_title)
        self.task_repo.save(task)

    def update_task_description(self, task_id: int, new_description: str) -> None:
        task = self.get_task(task_id)
        task.change_description(new_description)
        self.task_repo.save(task)

    def update_task_deadline(self, task_id: int, new_deadline: str) -> None:
        task = self.get_task(task_id)
        
        task.change_deadline(new_deadline)
        self.task_repo.save(task)

    def update_task_status(self, task_id: int, new_status: str) -> None:
        task = self.get_task(task_id)
        task.change_status(new_status)
        self.task_repo.save(task)

    def get_all_tasks(self) -> List[Task]:
        return self.task_repo.all()
