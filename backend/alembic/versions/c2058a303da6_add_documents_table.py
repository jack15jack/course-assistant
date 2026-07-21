"""add documents table

Revision ID: c2058a303da6
Revises: 4f75648302a3
Create Date: 2026-07-21 10:52:06.871416

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c2058a303da6"
down_revision: Union[str, Sequence[str], None] = "4f75648302a3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "documents",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "course_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "filename",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "filepath",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "file_type",
            sa.String(),
            nullable=False
        ),

        sa.Column(
            "status",
            sa.String(),
            nullable=True
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=True
        ),

        sa.ForeignKeyConstraint(
            ["course_id"],
            ["courses.id"]
        ),

        sa.PrimaryKeyConstraint(
            "id"
        )
    )


def downgrade() -> None:
    op.drop_table("documents")