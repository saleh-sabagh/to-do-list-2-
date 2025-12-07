from typing import List
from app.models.project import Project
from app.models.task import Task
from app.repositories.project_sql_repository import SQLAlchemyProjectRepository
from app.repositories.task_sql_repository import SQLAlchemyTaskRepository

class ProjectService:
    """Business logic for projects."""
    
    def __init__(self, project_repo: SQLAlchemyProjectRepository, task_repo: SQLAlchemyTaskRepository):
        self.project_repo = project_repo
        self.task_repo = task_repo

    def create_project(self, name: str, description: str) -> Project:
        project = Project(name=name, description=description)
        self.project_repo.save(project)
        return project

    def get_all_projects(self) -> List[Project]:
        return self.project_repo.all()

    def get_project(self, project_id: str) -> Project:
        project = self.project_repo.get_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        return project

    def delete_project(self, project_id: str) -> None:
        self.project_repo.delete(project_id)

    def add_task_to_project(self, project_id: str, title: str, description: str, deadline: str) -> Task:
        project = self.get_project(project_id)
        task = Task(title=title, description=description, deadline=deadline, project_id=project.id)
        self.task_repo.save(task)
        return task

    def remove_task_from_project(self, project_id: str, task_id: str) -> None:
        task = self.task_repo.get_by_id(task_id)
        if not task or task.project_id != int(project_id):
            raise ValueError("Task not found in this project")
        self.task_repo.delete(task_id)
