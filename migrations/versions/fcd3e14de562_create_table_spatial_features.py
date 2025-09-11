"""create table spatial features

Revision ID: fcd3e14de562
Revises: ede582ab94b5
Create Date: 2025-09-11 09:13:11.084497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision: str = 'fcd3e14de562'
down_revision: Union[str, Sequence[str], None] = 'ede582ab94b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "spatial_features",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("point", Geometry(geometry_type="POINT", srid=4326)),
        sa.Column("line", Geometry(geometry_type="LINESTRING", srid=4326)),
        sa.Column("polygon", Geometry(geometry_type="POLYGON", srid=4326)),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("spatial_features")
