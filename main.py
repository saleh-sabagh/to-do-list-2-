import warnings

from app.cli.console import (
    add_task_cli,
    create_project_cli,
    delete_project_cli,
    delete_task_cli,
    edit_project_cli,
    edit_task_cli,
    input_choice,
    list_projects_cli,
    list_tasks_cli,
    show_menu,
)
from app.db.session import get_db_session
from app.repositories.project_sql_repository import SQLAlchemyProjectRepository
from app.repositories.task_sql_repository import SQLAlchemyTaskRepository
from app.services.project_service import ProjectService
from app.services.task_service import TaskService

def main():
    warnings.warn(
        "The CLI is deprecated and will be removed in a future phase. "
        "Please migrate to the FastAPI service at /api/v1.",
        DeprecationWarning,
        stacklevel=1,
    )
    # ================= DI: ایجاد Session و Repositoryها =================
    with get_db_session() as session:
        project_repo = SQLAlchemyProjectRepository(db_session=session)
        task_repo = SQLAlchemyTaskRepository(db_session=session)

        # ================= DI: ایجاد Serviceها =================
        project_service = ProjectService(project_repo=project_repo, task_repo=task_repo)
        task_service = TaskService(task_repo=task_repo)

        # ================= CLI Loop =================
        while True:
            show_menu()
            choice = input_choice()

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
                print("👋 Exiting... Bye!")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
