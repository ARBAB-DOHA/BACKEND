"""add column

Revision ID: 7238abb56ad9
Revises: ade97e449c9b
Create Date: 2023-11-26 19:23:57.218531

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7238abb56ad9'
down_revision = 'ade97e449c9b'

branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass