"""add new column 'surname' for 'Users' table

Revision ID: cdb737a01fc8
Revises: 
Create Date: 2025-11-03 11:09:21.012076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdb737a01fc8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Users', 
                  sa.Column('surname', sa.String(50), nullable=False))

def downgrade() -> None:
    op.drop_column('Users', 'surname')
