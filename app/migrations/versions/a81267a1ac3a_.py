"""empty message

Revision ID: a81267a1ac3a
Revises: 44e6c42c7c4e
Create Date: 2025-01-16 13:11:10.477127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a81267a1ac3a'
down_revision: Union[str, None] = '44e6c42c7c4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
