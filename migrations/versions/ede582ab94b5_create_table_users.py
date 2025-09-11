"""create table users

Revision ID: ede582ab94b5
Revises: d59b28afab5f
Create Date: 2025-09-11 08:26:28.942653

"""
import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ede582ab94b5'
down_revision: Union[str, Sequence[str], None] = 'd59b28afab5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("created_at", sa.Date, default=datetime.date.today)
    )



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
