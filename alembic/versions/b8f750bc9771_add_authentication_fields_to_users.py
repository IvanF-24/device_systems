"""add authentication fields to users

Revision ID: b8f750bc9771
Revises: 4e2f28e9c33e
Create Date: 2026-06-24 21:05:44.864778
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b8f750bc9771"
down_revision: Union[str, Sequence[str], None] = "4e2f28e9c33e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "users",
        sa.Column(
            "hashed_password",
            sa.String(),
            nullable=False,
            server_default="temporal_password"
        )
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("users", "hashed_password")