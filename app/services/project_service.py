import uuid
from typing import List
from app.models.project import Project
from app.repositories.project_repository import IProjectRepository
from app.repositories.task_repository import ITaskRepository
from app.models.task import Task

class ProjectService:
    """Business logic for projects."""
    
    def __init__(self, project_repo: IProjectRepository, task_repo: ITaskRepository):
        self.project_repo = project_repo
        self.task_repo = task_repo
        self.all_projects_counter = 0
        
    def create_project(self, name: str, description: str) -> Project:
        project_id = self.all_projects_counter + 1
        project = Project(id=project_id, name=name, description=description)
        self.project_repo.save(project)
        self.all_projects_counter+=1
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

    def add_task_to_project(
        self, project_id: str, title: str, description: str, deadline: str
    ) -> Task:
        project = self.get_project(project_id)
        task_id = project.get_project_tasks_counter() + 1
        task = Task(id=task_id, title=title, description=description, deadline=deadline)
        project.add_task(task)
        self.task_repo.save(task)
        self.project_repo.save(project)  # update project
        return task

    def remove_task_from_project(self, project_id: str, task_id: str) -> None:
        project = self.get_project(project_id)
        project.remove_task(task_id)
        self.task_repo.delete(task_id)
        self.project_repo.save(project)  # update project
