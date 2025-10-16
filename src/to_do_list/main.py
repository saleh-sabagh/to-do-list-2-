from project import Project
from task import Task
from dotenv import load_dotenv

load_dotenv()


def show_menu() -> None:
    """Display the main menu of the TO DO List Manager with clear formatting."""
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


def get_project_by_name(name: str) -> Project:
    """Retrieve a Project instance by its name.

    Args:
        name (str): Name of the project.

    Raises:
        ValueError: If the project does not exist.

    Returns:
        Project: The project instance with the given name.
    """
    projects = Project.all_projects()
    if name not in projects:
        raise ValueError("Project not found.")
    return projects[name]


def choose_project() -> tuple[Project | None, str | None]:
    """Prompt the user to choose a project and display projects in a nice table format."""
    projects = [(p.id, p.name) for p in Project.all_projects().values()]
    if projects:
        print("\n📂 List of Projects:")
        print("-" * 35)
        for pid, name in projects:
            print(f"ID: {pid:<3} | Name: {name}")
        print("-" * 35)
    else:
        print("⚠️  There are no projects yet!")
        return None, None

    try:
        p_id = int(input("Select project's ID: ").strip())
        project_name = next(name for pid, name in projects if p_id == pid)
        return get_project_by_name(project_name), project_name
    except (ValueError, StopIteration):
        print("❌ Invalid project ID!")
        return None, None



def choose_task(project: Project) -> Task | None:
    """Prompt the user to choose a task from the project and display tasks neatly."""
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
    """Edit the title or description of a project.

    Args:
        project (Project): The project to edit.
    """
    print("What do you want to change?\n1. Title\n2. Description")
    try:
        choice = int(input("Choose option: ").strip())
    except ValueError:
        print("Invalid choice.")
        return

    if choice == 1:
        new_name = input("Enter new name: ").strip()
        project.change_name(new_name)
        print("✅ Name updated.")
    elif choice == 2:
        new_desc = input("Enter new description: ").strip()
        project.change_description(new_desc)
        print("✅ Description updated.")
    else:
        print("Invalid option.")


def edit_task(task: Task) -> None:
    """Edit the title, description, deadline, or status of a task.

    Args:
        task (Task): The task to edit.
    """
    print("What do you want to change?\n1. Title\n2. Description\n3. Deadline\n4. Status")
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
    elif choice == 4:
        new_status = input("Enter new status (todo, doing, done): ").strip()
        try:
            task.change_status(new_status)
            print("✅ Status updated.")
        except ValueError:
            print(f"Invalid status: {new_status}")
    else:
        print("Invalid option.")


def main() -> None:
    """Run the main loop of the TO DO List Manager."""
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
                project, _ = choose_project()
                if not project:
                    continue
                title = input("Task title: ").strip()
                desc = input("Description: ").strip()
                deadline = input("Deadline: ").strip()
                project.add_task(title, desc, deadline)
                print(f"✅ Task '{title}' added to {project.name}.")

            elif choice == "3":
                project, _ = choose_project()
                if not project:
                    continue
                edit_project(project)

            elif choice == "4":
                project, _ = choose_project()
                if not project:
                    continue
                task = choose_task(project)
                if not task:
                    continue
                edit_task(task)

            elif choice == "5":
                project, _ = choose_project()
                if not project:
                    continue
                task = choose_task(project)
                if not task:
                    continue
                project.remove_task(task.id)
                print("✅ Task deleted successfully!!")

            elif choice == "6":
                projects = [(p.id, p.name, p.description) for p in Project.all_projects().values()]
                if projects:
                    print("\n📂 Your Projects:")
                    print("=" * 50)
                    for pid, name, desc in projects:
                        print(f"🆔 ID         : {pid}")
                        print(f"📁 Name       : {name}")
                        print(f"📝 Description: {desc}")
                        print("-" * 50)
                else:
                    print("⚠️  There are no projects yet!")
                print("_____________________")

            elif choice == "7":
                project, _ = choose_project()
                if not project:
                    continue

                tasks = [(t.id, t.title, t.description, t.status) for t in project.all_project_tasks().values()]

                if tasks:
                    print("\n📋 Tasks in Project:")
                    print("=" * 50)
                    for tid, title, desc, status in tasks:
                        short_desc = desc if len(desc) < 100 else desc[:100] + "..."
                        print(f"🆔 Task ID     : {tid}")
                        print(f"📌 Title       : {title}")
                        print(f"📝 Description : {short_desc}")
                        print(f"📊 Status      : {status}")
                        print("-" * 50)
                else:
                    print("⚠️  There are no tasks in this project.")
                print()

            elif choice == "8":
                project, project_name = choose_project()
                if not project:
                    continue
                Project.delete_project(project_name)
                print("✅ Project deleted successfully!")

            elif choice == "0":
                print("👋 Goodbye!")
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    main()
