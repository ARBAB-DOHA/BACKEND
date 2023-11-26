"""create post table

Revision ID: 695c0e197c58
Revises: 
Create Date: 2023-11-25 10:14:42.496651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '695c0e197c58'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass



def downgrade():
    op.drop_table('posts')
    pass
