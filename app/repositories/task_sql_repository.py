from sqlalchemy.orm import Session
from app.models.task import Task
from app.repositories.task_repository import ITaskRepository

class SQLAlchemyTaskRepository(ITaskRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save(self, task: Task) -> None:
        self.db_session.add(task)
        self.db_session.commit()

    def delete(self, task_id: str) -> None:
        task = self.db_session.get(Task, int(task_id))
        if task:
            self.db_session.delete(task)
            self.db_session.commit()

    def get_by_id(self, task_id: str) -> Task | None:
        return self.db_session.get(Task, int(task_id))

    def all(self) -> list[Task]:
        return self.db_session.query(Task).all()
