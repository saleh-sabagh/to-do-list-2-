from abc import ABC, abstractmethod
from typing import List, Dict
from app.models.task import Task

class ITaskRepository(ABC):
    """Abstract repository interface for tasks."""

    @abstractmethod
    def save(self, task: Task) -> None:
        """Save or update a task."""
        ...

    @abstractmethod
    def delete(self, task_id: str) -> None:
        """Delete a task by its ID."""
        ...

    @abstractmethod
    def get_by_id(self, task_id: str) -> Task | None:
        """Retrieve a task by its ID."""
        ...

    @abstractmethod
    def all(self, skip: int = 0, limit: int = 100) -> List[Task]:
        """Return all tasks."""
        ...
    
    @abstractmethod
    def get_by_project(self, project_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        """Return tasks for a given project."""
        ...
        
class InMemoryTaskRepository(ITaskRepository):
    """In-memory implementation of task repository."""

    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def save(self, task: Task) -> None:
        """Save or update a task."""
        self.tasks[task.id] = task

    def delete(self, task_id: str) -> None:
        """Delete a task by ID."""
        self.tasks.pop(task_id, None)

    def get_by_id(self, task_id: str) -> Task | None:
        """Retrieve a task by ID."""
        return self.tasks.get(task_id)

    def all(self, skip: int = 0, limit: int = 100) -> List[Task]:
        """Return all tasks."""
        tasks = list(self.tasks.values())
        return tasks[skip : skip + limit]
    
    def get_by_project(self, project_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        project_tasks = [task for task in self.tasks.values() if task.project_id == project_id]
        return project_tasks[skip : skip + limit]