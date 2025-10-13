import os
from dotenv import load_dotenv
load_dotenv()
from collections import OrderedDict

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
        Project._id_counter+=1

    def change_name(self, new_name : str):
        self.name = new_name
    
    def change_description(self, new_description : str):
        self.description = new_description
    
       
if __name__ == "__main__":
    p1 = Project("todolist", "implementarion of todolist in cli")
    print(p1.description)
    p1.change_description("jdugu vf vhj jh vjh jhd vvd")
    print(p1.description)
    p2 = Project("portolio", "implementation of site")
    print(Project._projects_name["portolio"])
    