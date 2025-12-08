from datetime import datetime
from typing import List, Optional

from app.models.project import Project
from app.models.task import Task
from app.repositories.project_sql_repository import SQLAlchemyProjectRepository
from app.repositories.task_sql_repository import SQLAlchemyTaskRepository
class ProjectService:
    """Business logic for projects."""
    
    def __init__(self, project_repo: SQLAlchemyProjectRepository, task_repo: SQLAlchemyTaskRepository):
        self.project_repo = project_repo
        self.task_repo = task_repo

    def create_project(self, name: str, description: str | None) -> Project:
        project = Project(name=name, description=description)
        self.project_repo.save(project)
        return project

    def get_all_projects(self, skip: int = 0, limit: int = 100) -> List[Project]:
        return self.project_repo.all(skip=skip, limit=limit)

    def get_project(self, project_id: int) -> Project:
        project = self.project_repo.get_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        return project

    def update_project(
        self,
        project_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Project:
        project = self.get_project(project_id)

        if name is not None:
            project.change_name(name)
        if description is not None:
            project.change_description(description)

        self.project_repo.save(project)
        return project

    def delete_project(self, project_id: int) -> None:
        project = self.project_repo.get_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        self.project_repo.delete(project_id)

    def add_task_to_project(
        self,
        project_id: int,
        title: str,
        description: str | None,
        deadline: datetime | str | None,
        status: str = "todo",
    ) -> Task:
        project = self.get_project(project_id)

        task = Task(
            title=title,
            description=description,
            deadline=None,
            project_id=project.id,
            status=status or "todo",
        )
        task.change_status(status or "todo")
        if deadline is not None:
            task.change_deadline(deadline)
        self.task_repo.save(task)
        return task

    def remove_task_from_project(self, project_id: int, task_id: int) -> None:
        task = self.task_repo.get_by_id(task_id)
        if not task or task.project_id != int(project_id):
            raise ValueError("Task not found in this project")
        self.task_repo.delete(task_id)

    def list_tasks_for_project(self, project_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        self.get_project(project_id)
        return self.task_repo.get_by_project(project_id, skip=skip, limit=limit)
