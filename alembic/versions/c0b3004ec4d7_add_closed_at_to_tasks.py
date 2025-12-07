"""add closed_at to tasks

Revision ID: add_closed_at_to_tasks
Revises: 26e0239a97e0
Create Date: 2025-12-07 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "add_closed_at_to_tasks"
down_revision = "26e0239a97e0"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("tasks", sa.Column("closed_at", sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column("tasks", "closed_at")
