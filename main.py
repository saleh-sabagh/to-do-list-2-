from dotenv import load_dotenv

from app.cli.console import (
    show_menu,
    input_choice,
    create_project_cli,
    list_projects_cli,
    edit_project_cli,
    delete_project_cli,
    add_task_cli,
    list_tasks_cli,
    edit_task_cli,
    delete_task_cli,
)

from app.repositories.project_repository import InMemoryProjectRepository
from app.repositories.task_repository import InMemoryTaskRepository
from app.services.project_service import ProjectService
from app.services.task_service import TaskService


def create_services() -> tuple[ProjectService, TaskService]:
    """Initialize repositories and services and return them."""

    project_repo = InMemoryProjectRepository()
    task_repo = InMemoryTaskRepository()

    project_service = ProjectService(project_repo, task_repo)
    task_service = TaskService(task_repo)

    return project_service, task_service


def main() -> None:
    """Run the main loop of the TO DO List Manager."""

    load_dotenv()

    project_service, task_service = create_services()

    while True:
        show_menu()
        choice = input_choice()

        try:
            if choice == "1":
                create_project_cli(project_service)

            elif choice == "2":
                add_task_cli(project_service)

            elif choice == "3":
                edit_project_cli(project_service)

            elif choice == "4":
                edit_task_cli(project_service, task_service)

            elif choice == "5":
                delete_task_cli(project_service)

            elif choice == "6":
                list_projects_cli(project_service)

            elif choice == "7":
                list_tasks_cli(project_service)

            elif choice == "8":
                delete_project_cli(project_service)

            elif choice == "0":
                print("👋 Goodbye!")
                break

            else:
                print("⚠️ Invalid choice. Please try again.")

        except Exception as e:
            print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    main()
