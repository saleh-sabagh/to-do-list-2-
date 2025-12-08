from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db_session_dependency
from app.repositories.project_sql_repository import SQLAlchemyProjectRepository
from app.repositories.task_sql_repository import SQLAlchemyTaskRepository
from app.services.project_service import ProjectService
from app.services.task_service import TaskService


def get_db(session: Session = Depends(get_db_session_dependency)) -> Session:
    return session


def get_project_repository(db: Session = Depends(get_db)) -> SQLAlchemyProjectRepository:
    return SQLAlchemyProjectRepository(db_session=db)


def get_task_repository(db: Session = Depends(get_db)) -> SQLAlchemyTaskRepository:
    return SQLAlchemyTaskRepository(db_session=db)


def get_project_service(
    project_repo: SQLAlchemyProjectRepository = Depends(get_project_repository),
    task_repo: SQLAlchemyTaskRepository = Depends(get_task_repository),
) -> ProjectService:
    return ProjectService(project_repo=project_repo, task_repo=task_repo)


def get_task_service(
    task_repo: SQLAlchemyTaskRepository = Depends(get_task_repository),
) -> TaskService:
    return TaskService(task_repo=task_repo)

