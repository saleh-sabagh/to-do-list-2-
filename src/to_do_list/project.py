import os
from dotenv import load_dotenv
load_dotenv()

class Project:
    
    MAX_PROJECTS = int(os.getenv("MAX_NUMBER_OF_PROJECT", 10))
    _projects_name = {}
    def __init__(self, name : str, description : str) -> None:
        self.name = name
        self.description = description

    def change_name(self, new_name : str):
        self.name = new_name
    
    def change_description(self, new_description : str):
        self.description = new_description
    
       
    
    