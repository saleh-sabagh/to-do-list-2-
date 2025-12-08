from sqlalchemy.orm import Session
from app.models.project import Project
from app.repositories.project_repository import IProjectRepository

class SQLAlchemyProjectRepository(IProjectRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save(self, project: Project) -> None:
        self.db_session.add(project)
        self.db_session.commit()

    def delete(self, project_id: str) -> None:
        project = self.db_session.get(Project, int(project_id))
        if project:
            self.db_session.delete(project)
            self.db_session.commit()

    def get_by_id(self, project_id: str) -> Project | None:
        return self.db_session.get(Project, int(project_id))

    def all(self, skip: int = 0, limit: int = 100) -> list[Project]:
        return (
            self.db_session.query(Project)
            .offset(int(skip))
            .limit(int(limit))
            .all()
        )
