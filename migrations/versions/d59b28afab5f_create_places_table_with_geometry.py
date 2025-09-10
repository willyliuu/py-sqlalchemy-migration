"""create places table with geometry

Revision ID: d59b28afab5f
Revises: 
Create Date: 2025-09-10 08:48:13.858748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision: str = 'd59b28afab5f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")

    # Create table
    op.create_table(
        "places",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("location", Geometry(geometry_type="POINT", srid=4326)),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("places")
    op.execute("DROP EXTENSION IF EXISTS postgis")
