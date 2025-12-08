from abc import ABC, abstractmethod
from typing import List , Dict
from app.models.project import Project

class IProjectRepository(ABC):
    """Abstract repository interface for projects."""

    @abstractmethod
    def save(self, project: Project) -> None:
        ...

    @abstractmethod
    def delete(self, project_id: str) -> None:
        ...

    @abstractmethod
    def get_by_id(self, project_id: str) -> Project | None:
        ...

    @abstractmethod
    def all(self, skip: int = 0, limit: int = 100) -> List[Project]:
        ...

class InMemoryProjectRepository(IProjectRepository):
    """In-memory implementation of project repository."""

    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.id_counter = 1

    def save(self, project: Project) -> None:
        self.projects[project.id] = project

    def delete(self, project_id: str) -> None:
        print(project_id)
        self.projects.pop(int(project_id), None)

    def get_by_id(self, project_id: str) -> Project | None:
        return self.projects.get(project_id)

    def all(self, skip: int = 0, limit: int = 100) -> List[Project]:
        projects = list(self.projects.values())
        return projects[skip : skip + limit]