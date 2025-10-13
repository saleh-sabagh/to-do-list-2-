import os
from dotenv import load_dotenv
load_dotenv()

class Project:
    MAX_PROJECTS = int(os.getenv("MAX_NUMBER_OF_PROJECT", 10))
    _projects_name = {}
    
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

    def change_name(self, new_name : str):
        self.name = new_name
    
    def change_description(self, new_description : str):
        self.description = new_description
    
       
    
    