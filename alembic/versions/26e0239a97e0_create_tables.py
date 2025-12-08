"""create tables

Revision ID: 26e0239a97e0
Revises: 
Create Date: 2025-12-07 21:39:50.004958

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision: str = "26e0239a97e0"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    inspector = inspect(bind)
    tables = inspector.get_table_names()

    if "projects" not in tables:
        op.create_table(
            "projects",
            sa.Column("id", sa.Integer(), primary_key=True, index=True),
            sa.Column("name", sa.String(length=30), nullable=False),
            sa.Column("description", sa.String(length=150), nullable=True),
        )

    if "tasks" not in tables:
        op.create_table(
            "tasks",
            sa.Column("id", sa.Integer(), primary_key=True, index=True),
            sa.Column("title", sa.String(length=30), nullable=False),
            sa.Column("description", sa.String(length=150), nullable=True),
            sa.Column("deadline", sa.DateTime(), nullable=True),
            sa.Column("status", sa.String(length=10), nullable=True, default="todo"),
            sa.Column("project_id", sa.Integer(), sa.ForeignKey("projects.id")),
        )

    if "tasks" in tables:
        existing_columns = {col["name"] for col in inspector.get_columns("tasks")}
        if "status" in existing_columns:
            op.alter_column(
                "tasks",
                "status",
                existing_type=sa.VARCHAR(length=10),
                nullable=True,
            )


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    inspector = inspect(bind)
    tables = inspector.get_table_names()

    if "tasks" in tables:
        op.alter_column(
            "tasks",
            "status",
            existing_type=sa.VARCHAR(length=10),
            nullable=False,
        )
