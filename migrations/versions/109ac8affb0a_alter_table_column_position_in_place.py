"""alter table column position in place

Revision ID: 109ac8affb0a
Revises: a093c7179005
Create Date: 2025-09-11 09:31:29.959620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '109ac8affb0a'
down_revision: Union[str, Sequence[str], None] = 'a093c7179005'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Alter column SRID using PostGIS function
    op.execute("""
        ALTER TABLE places
        ALTER COLUMN position TYPE geometry(Point, 3857)
        USING ST_Transform(position, 3857)
    """)


def downgrade() -> None:
    """Downgrade schema."""
    # Revert column SRID back to original using PostGIS function
    op.execute("""
        ALTER TABLE places
        ALTER COLUMN position TYPE geometry(Point, 4326)
        USING ST_Transform(position, 4326)
    """)
