from project import Project
from task import Task
from typing import Tuple

def get_project_by_name(name: str) -> Project:
    """Retrieve a Project instance by its name."""
    projects = Project.all_projects()
    if name not in projects:
        raise ValueError("Project not found.")
    return projects[name]


def choose_project() -> Tuple[Project | None, str | None]:
    """Prompt the user to choose a project."""
    projects = [(p.id, p.name) for p in Project.all_projects().values()]
    if not projects:
        print("⚠️  There are no projects yet!")
        return None, None

    print("\n📂 List of Projects:")
    print("-" * 35)
    for pid, name in projects:
        print(f"ID: {pid:<3} | Name: {name}")
    print("-" * 35)

    try:
        p_id = int(input("Select project's ID: ").strip())
        project_name = next(name for pid_, name in projects if p_id == pid_)
        return get_project_by_name(project_name), project_name
    except (ValueError, StopIteration):
        print("❌ Invalid project ID!")
        return None, None


def choose_task(project: Project) -> Task | None:
    """Prompt the user to choose a task from the project."""
    tasks = [(t.id, t.title, t) for t in project.all_project_tasks().values()]
    if not tasks:
        print("⚠️  There are no tasks in this project.")
        return None

    print("\n📋 List of Tasks:")
    print("-" * 35)
    for tid, title, _ in tasks:
        print(f"ID: {tid:<3} | Title: {title}")
    print("-" * 35)

    try:
        t_id = input("Enter task ID: ").strip()
        return next(t for tid, _, t in tasks if tid == t_id)
    except (ValueError, StopIteration):
        print("❌ Invalid task ID!")
        return None


def edit_project(project: Project) -> None:
    """Edit a project's title or description."""
    print("What do you want to change?\n1. Title\n2. Description")
    try:
        choice = int(input("Choose option: ").strip())
    except ValueError:
        print("Invalid choice.")
        return

    if choice == 1:
        from cli import input_new_name
        project.change_name(input_new_name())
        print("✅ Name updated.")
    elif choice == 2:
        from cli import input_new_description
        project.change_description(input_new_description())
        print("✅ Description updated.")
    else:
        print("Invalid option.")


def edit_task(task: Task) -> None:
    """Edit a task's title, description, deadline, or status."""
    print("What do you want to change?\n1. Title\n2. Description\n3. Deadline\n4. Status")
    try:
        choice = int(input("Choose option: ").strip())
    except ValueError:
        print("Invalid choice.")
        return

    from cli import input_task_status, input_task_deadline, input_task_title, input_task_description

    if choice == 1:
        task.change_title(input_task_title())
        print("✅ Title updated.")
    elif choice == 2:
        task.change_description(input_task_description())
        print("✅ Description updated.")
    elif choice == 3:
        task.change_deadline(input_task_deadline())
        print("✅ Deadline updated.")
    elif choice == 4:
        try:
            task.change_status(input_task_status())
            print("✅ Status updated.")
        except ValueError:
            print("❌ Invalid status")
    else:
        print("Invalid option.")
