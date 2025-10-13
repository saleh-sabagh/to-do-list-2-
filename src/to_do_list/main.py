from project import Project
from task import Task
from dotenv import load_dotenv
load_dotenv()

def show_menu():
    print("\n===== TO DO LIST MANAGER =====")
    print("1. Create new project")
    print("2. Add task to project")
    print("3. Delete task from project")
    print("4. List all projects")
    print("5. List tasks in project")
    print("6. Delete project")
    print("0. Exit")
    print("==============================")
    

