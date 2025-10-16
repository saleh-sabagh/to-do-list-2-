def show_menu() -> None:
    """Display the main menu of the TO DO List Manager."""
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


def input_project_name() -> str:
    return input("Project name: ").strip()


def input_project_description() -> str:
    return input("Description: ").strip()


def input_task_title() -> str:
    return input("Task title: ").strip()


def input_task_description() -> str:
    return input("Description: ").strip()


def input_task_deadline() -> str:
    return input("Deadline: ").strip()


def input_choice(prompt: str = "Choose option: ") -> str:
    return input(prompt).strip()


def input_task_status() -> str:
    return input("Enter new status (todo, doing, done): ").strip()


def input_new_name() -> str:
    return input("Enter new name: ").strip()


def input_new_description() -> str:
    return input("Enter new description: ").strip()


def input_new_deadline() -> str:
    return input("Enter new deadline (YYYY-MM-DD): ").strip()
