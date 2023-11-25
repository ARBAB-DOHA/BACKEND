"""add content column to posts table

Revision ID: 6c7aa42573d6
Revises: 695c0e197c58
Create Date: 2023-11-25 11:09:21.758230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c7aa42573d6'
down_revision: Union[str, None] = '695c0e197c58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    pass
