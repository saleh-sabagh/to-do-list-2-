from project import Project
from task import Task
from dotenv import load_dotenv
load_dotenv()

def show_menu():
    print("\n===== TO DO LIST MANAGER =====")
    print("1. Create new project")
    print("2. Add task to project")
    print("3. Add task to project")    
    print("4. Delete task from project")
    print("5. List all projects")
    print("6. List tasks in project")
    print("7. Delete project")
    print("0. Exit")
    print("==============================")
    
    
def get_project_by_name(name : str) -> Project:
    if name not in Project._projects_name:
        raise ValueError("Project not found.")
    return Project._projects_name[name]

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                name = input("Project name: ").strip()
                desc = input("Description: ").strip()
                Project(name, desc)
                print(f"✅ Project '{name}' created successfully.")

            elif choice == "2":
                print("List of projects: ")
                projects_name_id = [(p.id , p.name) for p in Project._projects_name.values()]
                for id , name in projects_name_id:
                    print(f"{id}. {name}")
                print("_____________________")
                p_id = int(input("Select project ID to add a task: ").strip())
                project_name = next(name for id , name in projects_name_id if p_id == id)
                project = get_project_by_name(project_name)
                title = input("Task title: ").strip()
                desc = input("Description: ").strip()
                deadline = input("Deadline: ").strip()
                project.add_task(title, desc, deadline)
                print(f"✅ Task '{title}' added to {project_name}.")
                
        except Exception as e:
            print(f"⚠️ Error: {e}")

