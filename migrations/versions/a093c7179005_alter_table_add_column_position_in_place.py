"""alter table add column position in place

Revision ID: a093c7179005
Revises: fcd3e14de562
Create Date: 2025-09-11 09:29:41.827225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision: str = 'a093c7179005'
down_revision: Union[str, Sequence[str], None] = 'fcd3e14de562'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "places",
        sa.Column("position", Geometry(geometry_type="POINT", srid=4326))
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("places", "position")
