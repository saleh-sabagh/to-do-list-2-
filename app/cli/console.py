from typing import Optional
from app.services.project_service import ProjectService
from app.services.task_service import TaskService

def show_menu() -> None:
    print("\n" + "=" * 35)
    print("      📝 TO DO LIST MANAGER 📝      ")
    print("=" * 35)
    print("1️⃣  Create new project")
    print("2️⃣  Add task to project")
    print("3️⃣  Edit project")
    print("4️⃣  Edit task")
    print("5️⃣  Delete task from project")
    print("6️⃣  List all projects")
    print("7️⃣  List tasks in project")
    print("8️⃣  Delete project")
    print("0️⃣  Exit")
    print("=" * 35)

def input_choice(prompt: str = "Choose option: ") -> str:
    return input(prompt).strip()

def input_project_name() -> str:
    return input("Project name: ").strip()

def input_project_description() -> str:
    return input("Project description: ").strip()

def input_task_title() -> str:
    return input("Task title: ").strip()

def input_task_description() -> str:
    return input("Task description: ").strip()

def input_task_deadline() -> str:
    return input("Task deadline (YYYY-MM-DD): ").strip()

def input_task_status() -> str:
    return input("Enter new status (todo, doing, done): ").strip()

def input_project_id() -> str:
    return input("Enter project ID: ").strip()

def input_task_id() -> str:
    return input("Enter task ID: ").strip()


# ===================== Project CLI =====================
def create_project_cli(project_service: ProjectService):
    name = input_project_name()
    description = input_project_description()
    project = project_service.create_project(name, description)
    print(f"✅ Project '{project.name}' created successfully with ID {project.id}.")

def list_projects_cli(project_service: ProjectService):
    projects = project_service.get_all_projects()
    if not projects:
        print("⚠️  There are no projects yet!")
        return
    print("\n📂 Your Projects:")
    print("=" * 50)
    for project in projects:
        print(f"🆔 ID         : {project.id}")
        print(f"📁 Name       : {project.name}")
        print(f"📝 Description: {project.description}")
        print("-" * 50)

def edit_project_cli(project_service: ProjectService):
    project_id = input_project_id()
    try:
        project = project_service.get_project(project_id)
    except ValueError as e:
        print(f"⚠️ {e}")
        return

    new_name = input("Enter new name (leave empty to keep current): ").strip()
    if new_name:
        project.name = new_name

    new_desc = input("Enter new description (leave empty to keep current): ").strip()
    if new_desc:
        project.description = new_desc

    project_service.project_repo.save(project)
    print(f"✅ Project '{project.name}' updated successfully.")


def delete_project_cli(project_service: ProjectService):
    list_projects_cli(project_service)
    project_id = input_project_id()
    try:
        project_service.delete_project(project_id)
        print("✅ Project deleted successfully!")
    except ValueError as e:
        print(f"⚠️ {e}")


# ===================== Task CLI =====================
def add_task_cli(project_service: ProjectService):
    list_projects_cli(project_service)
    project_id = input_project_id()
    title = input_task_title()
    description = input_task_description()
    deadline = input_task_deadline()
    try:
        task = project_service.add_task_to_project(int(project_id), title, description, deadline)
        print(f"✅ Task '{task.title}' added successfully with ID {task.id}.")
    except ValueError as e:
        print(f"⚠️ {e}")

def list_tasks_cli(project_service: ProjectService):
    list_projects_cli(project_service)
    project_id = input_project_id()
    try:
        project = project_service.get_project(int(project_id))
    except ValueError as e:
        print(f"⚠️ {e}")
        return

    tasks = project.tasks  
    if not tasks:
        print("⚠️  There are no tasks in this project.")
        return

    print(f"\n📋 Tasks in Project '{project.name}':")
    print("=" * 50)
    for task in tasks:
        short_desc = task.description if task.description and len(task.description) < 100 else (task.description[:100] + "..." if task.description else "")
        print(f"🆔 Task ID     : {task.id}")
        print(f"📌 Title       : {task.title}")
        print(f"📝 Description : {short_desc}")
        print(f"🕒 Deadline    : {task.deadline}")
        print(f"📊 Status      : {task.status}")
        print("-" * 50)

def edit_task_cli(project_service: ProjectService ,task_service: TaskService):
    list_tasks_cli(project_service)
    task_id = input_task_id()
    try:
        task = task_service.get_task(int(task_id))
    except ValueError as e:
        print(f"⚠️ {e}")
        return
    try:
        new_title = input("Enter new title (leave empty to keep current): ").strip()
        if new_title:
            task_service.update_task_title(task.id, new_title)

        new_desc = input("Enter new description (leave empty to keep current): ").strip()
        if new_desc:
            task_service.update_task_description(task.id, new_desc)

        new_deadline = input("Enter new deadline (YYYY-MM-DD) (leave empty to keep current): ").strip()
        if new_deadline:
            task_service.update_task_deadline(task.id, new_deadline)

        new_status = input("Enter new status (todo, doing, done) (leave empty to keep current): ").strip()
        if new_status:
            task_service.update_task_status(task.id, new_status)

        print(f"✅ Task '{task.title}' updated successfully.")
    except ValueError:
        print("invalid deadline format")
def delete_task_cli(project_service: ProjectService):
    list_projects_cli(project_service)
    project_id = input_project_id()
    list_tasks_cli(project_service)
    task_id = input_task_id()
    try:
        project_service.remove_task_from_project(int(project_id), int(task_id))
        print("✅ Task deleted successfully!")
    except ValueError as e:
        print(f"⚠️ {e}")
