import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env for local development
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set. Check your .env file")

# Synchronous SQLAlchemy engine; keep echo configurable via env when debugging
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(
    DATABASE_URL,
    future=True,
    echo=os.getenv("SQL_ECHO", "false").lower() == "true",
    connect_args=connect_args,
)

# Session factory shared by CLI and API
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


@contextmanager
def get_db_session():
    """
    Context manager for CLI/scripts. Services manage commits; this only handles lifecycle.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_db_session_dependency():
    """
    FastAPI dependency that yields a database session per request.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
