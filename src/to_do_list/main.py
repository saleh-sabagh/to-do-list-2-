from project import Project
from task import Task
from dotenv import load_dotenv
load_dotenv()

def show_menu():
    print("\n===== TO DO LIST MANAGER =====")
    print("1. Create new project")
    print("2. Add task to project")
    print("3. Edit task")    
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


def choose_project():
    print("List of projects:")
    projects = [(p.id, p.name) for p in Project._projects_name.values()]
    for pid, name in projects:
        print(f"{pid}. {name}")
    print("_____________________")

    try:
        p_id = int(input("Select project's ID: ").strip())
        project_name = next(name for pid, name in projects if p_id == pid)
        return get_project_by_name(project_name)
    except (ValueError, StopIteration):
        print("Invalid project ID!")
        return None


def choose_task(project):
    tasks = [(t.id, t.title, t) for t in project.all_project_tasks().values()]
    if not tasks:
        print("There are no tasks in this project.")
        return None
    print("List of tasks:")
    for tid, title, _ in tasks:
        print(f"{tid}. {title}")
    print("_____________________")

    try:
        t_id = input("Enter task ID: ").strip()
        
        return next(t for tid, _, t in tasks if tid == t_id)
    except (ValueError, StopIteration):
        print("Invalid task ID!")
        return None


def edit_task(task):
    print("What do you want to change?\n"
          "1. Title\n"
          "2. Description\n"
          "3. Deadline")
    try:
        choice = int(input("Choose option: ").strip())
    except ValueError:
        print("Invalid choice.")
        return

    if choice == 1:
        new_title = input("Enter new title: ").strip()
        task.change_title(new_title)
        print("✅ Title updated.")
    elif choice == 2:
        new_desc = input("Enter new description: ").strip()
        task.change_description(new_desc)
        print("✅ Description updated.")
    elif choice == 3:
        new_deadline = input("Enter new deadline (YYYY-MM-DD): ").strip()
        task.change_deadline(new_deadline)
        print("✅ Deadline updated.")
    else:
        print("Invalid option.")

def show_projects():
    print("List of projects:")
    projects = [(p.id, p.name) for p in Project._projects_name.values()]
    for pid, name in projects:
        print(f"{pid}. {name}")
    print("_____________________")
    
    
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
                project = choose_project()
                if not project:
                    continue
                title = input("Task title: ").strip()
                desc = input("Description: ").strip()
                deadline = input("Deadline: ").strip()
                project.add_task(title, desc, deadline)
                print(f"✅ Task '{title}' added to {project.name}.")
                
            elif choice == "3":
                project = choose_project()
                if not project:
                    continue
                task = choose_task(project)
                if not task:
                    continue
                edit_task(task)
                
            elif choice == "4":
                project = choose_project()
                if not project:
                    continue
                task = choose_task(project)
                if not task:
                    continue
                project.remove_task(task.id)
                print(f"✅ Task deleted successfully!!")

            elif choice == "5":
                show_projects()
            
                 
                

            elif choice == "0":
                print("👋 Goodbye!")
                break
            
            else:
                print("Invalid choice.")
                
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
    