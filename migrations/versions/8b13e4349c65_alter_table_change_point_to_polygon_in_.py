"""alter table change point to polygon in column position in table place

Revision ID: 8b13e4349c65
Revises: 109ac8affb0a
Create Date: 2025-09-11 09:34:18.132479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b13e4349c65'
down_revision: Union[str, Sequence[str], None] = '109ac8affb0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Alter column type using PostGIS function
    op.execute("""
        ALTER TABLE places
        ALTER COLUMN position TYPE geometry(Polygon, 4326)
        USING ST_MakePolygon(position)
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE places
        ALTER COLUMN position TYPE geometry(Point, 4326)
        USING ST_PointFromText(ST_AsText(position), 4326)
    """)
