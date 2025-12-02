import os
from collections import OrderedDict
from datetime import datetime
from typing import ClassVar, OrderedDict as OD
from app.models.task import Task
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Project:
    """
    Represents a project that contains multiple tasks.

    Each project has a unique ID, name, description, and a list of tasks.
    The number of projects and tasks per project is limited by environment variables.
    """
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    description = Column(String(150))
    MAX_TASKS: ClassVar[int] = int(os.getenv("MAX_NUMBER_OF_TASK", 10))

    def __init__(self,id: str, name: str, description: str) -> None:

        if len(name) > 30 or len(name) < 1:
            raise ValueError("Project name must be less than 30 characters and not empty.")
        if len(description) > 150:
            raise ValueError("Project description must be less than 150 characters.")

        self.id = id
        self.name: str = name
        self.description: str = description
        self.tasks = OD()
        self.tasks_counter = 0

    def change_name(self, new_name: str) -> None:
        if len(new_name) > 30 or len(new_name) < 1:
            raise ValueError("Project name must be less than 30 characters and not empty.")
        self.name = new_name

    def change_description(self, new_description: str) -> None:
        """
        Update the project description.

        Args:
            new_description (str): The new description for the project.
        """
        self.description = new_description


    def add_task(self, task : Task) -> None:
        """
        Add a new task to this project.

        Args:
            title (str): The title of the task.
            description (str): The task description.
            deadline (datetime): The task deadline.

        Raises:
            ValueError: If the number of tasks exceeds the maximum allowed.
        """
        if len(self.tasks) >= self.MAX_TASKS:
            raise ValueError(f"Cannot create more than {self.MAX_TASKS} tasks!")
        self.tasks_counter+=1
        self.tasks[task.id] = task

    def remove_task(self, task_id: str) -> None:
        """
        Remove a task from this project.

        Args:
            task_id (str): The ID of the task to remove.

        Raises:
            ValueError: If no task exists with the given ID.
        """
        if task_id not in self.tasks:
            raise ValueError(f"No task with id '{task_id}'.")
        del self.tasks[task_id]

    

    def all_project_tasks(self) -> OD[str, Task]:
        """
        Get all tasks belonging to this project.

        Returns:
            OrderedDict[str, Task]: All tasks for the current project.
        """
        return self.tasks

    def get_project_id(self) -> int:
        """
        Get the project's unique ID.

        Returns:
            int: The project ID.
        """
        return self.id

    def get_project_name(self) -> str:
        """
        Get the project's name.

        Returns:
            str: The project name.
        """
        return self.name

    def get_number_of_tasks(self) -> int:
        """
        Get the total number of tasks in this project.

        Returns:
            int: The number of tasks.
        """
        return len(self.tasks)

    def get_project_tasks_counter(self):
        return self.tasks_counter