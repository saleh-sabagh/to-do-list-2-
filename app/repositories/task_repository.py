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
    def all(self) -> List[Task]:
        """Return all tasks."""
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

    def all(self) -> List[Task]:
        """Return all tasks."""
        return list(self.tasks.values())