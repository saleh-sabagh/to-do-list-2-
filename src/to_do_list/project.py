import os
from dotenv import load_dotenv
load_dotenv()
from collections import OrderedDict
from task import Task
from datetime import datetime

class Project:
    MAX_PROJECTS = int(os.getenv("MAX_NUMBER_OF_PROJECT", 10))
    _projects_name = OrderedDict()
    _id_counter = 1
    
    def __init__(self, name : str, description : str) -> None:
        if name in Project._projects_name:
            raise ValueError(f"Projec with name {name} already exists!")
        if len(Project._projects_name) >= Project.MAX_PROJECTS:
            raise ValueError(f"Cannot create more than {Project.MAX_PROJECTS} projects!")
        if len(name) > 30 or len(name) < 1:            
            raise ValueError("project's name must be less than 30 characters and not empty")
        if len(description) > 150 or len(description) < 1:            
            raise ValueError("project's description must be less than 150 characters and not empty")
        self.name = name
        Project._projects_name[name] = self
        self.description = description
        self.id = Project._id_counter
        Project._id_counter += 1
        self._task_counter = 1
        self.tasks = OrderedDict()
    
    def change_name(self, new_name : str) -> None:
        self.name = new_name
    
    def change_description(self, new_description : str) -> None:
        self.description = new_description
    
    def generate_task_id(self) -> str:
        tid = f"P{self.id}-T{self._task_counter}"
        self._task_counter += 1
        return tid
    
    def add_task(self, title : str, description : str, deadline : datetime) -> Task:
        task_id = self.generate_task_id()
        task = Task(task_id, title, description, deadline)
        self.tasks[task.id] = task
        return task
    
    def remove_task(self, task_id : str) -> None:
        if task_id not in self.tasks:
            raise ValueError(f"No task with id {task_id}")
        del self.tasks[task_id]
    
if __name__ == "__main__":
    p1 = Project("todolist", "implementarion of todolist in cli")
    print(p1.description)
    p1.change_description("jdugu vf vhj jh vjh jhd vvd")
    print(p1.description)
    p2 = Project("portolio", "implementation of site")
    print(Project._projects_name["portolio"])
    