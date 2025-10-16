import os
from collections import OrderedDict
from datetime import datetime
from typing import ClassVar, OrderedDict as OrderedDictType

from task import Task


class Project:
    MAX_PROJECTS: ClassVar[int] = int(os.getenv("MAX_NUMBER_OF_PROJECT", 10))
    _projects_name: ClassVar[OrderedDictType[str, "Project"]] = OrderedDict()
    _id_counter: ClassVar[int] = 1

    def __init__(self, name: str, description: str) -> None:
        if name in Project._projects_name:
            raise ValueError(f"Project with name '{name}' already exists!")
        if len(Project._projects_name) >= Project.MAX_PROJECTS:
            raise ValueError(f"Cannot create more than {Project.MAX_PROJECTS} projects!")
        if len(name) > 30 or len(name) < 1:
            raise ValueError("Project name must be less than 30 characters and not empty.")
        if len(description) > 150 or len(description) < 1:
            raise ValueError("Project description must be less than 150 characters and not empty.")

        self.name: str = name
        Project._projects_name[name] = self
        self.description: str = description
        self.id: int = Project._id_counter
        Project._id_counter += 1
        self._task_counter: int = 1
        self.tasks: OrderedDictType[str, Task] = OrderedDict()
        self.MAX_TASKS: int = int(os.getenv("MAX_NUMBER_OF_TASK", 10))

    @classmethod
    def delete_project(cls, name: str) -> None:
        if name in cls._projects_name:
            del cls._projects_name[name]
        else:
            print("No project found with that name.")

    def change_name(self, new_name: str) -> None:
        type(self)._projects_name.pop(self.name)
        type(self)._projects_name[new_name] = self
        self.name = new_name

    def change_description(self, new_description: str) -> None:
        self.description = new_description

    def generate_task_id(self) -> str:
        tid: str = f"p{self.id}-t{self._task_counter}"
        self._task_counter += 1
        return tid

    def add_task(self, title: str, description: str, deadline: datetime) -> None:
        if len(self.tasks) >= self.MAX_TASKS:
            raise ValueError(f"Cannot create more than {self.MAX_TASKS} tasks!")
        task_id: str = self.generate_task_id()
        task: Task = Task(task_id, title, description, deadline)
        self.tasks[task.id] = task

    def remove_task(self, task_id: str) -> None:
        if task_id not in self.tasks:
            raise ValueError(f"No task with id '{task_id}'.")
        del self.tasks[task_id]

    @classmethod
    def all_projects(cls) -> OrderedDictType[str, "Project"]:
        return cls._projects_name

    def all_project_tasks(self) -> OrderedDictType[str, Task]:
        return self.tasks

    def get_project_id(self) -> int:
        return self.id

    def get_project_name(self) -> str:
        return self.name

    def get_number_of_tasks(self) -> int:
        return len(self.tasks)
