"""create table join request

Revision ID: 34f83cf0a9a5
Revises: 7238abb56ad9
Create Date: 2023-11-28 09:25:08.660344

"""
from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision = '34f83cf0a9a5'
down_revision = '7238abb56ad9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
   op.create_table(
        'join_requests',
        sa.Column('id', sa.Integer(), nullable=False,primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('community_id', sa.Integer(), sa.ForeignKey('community.id'), nullable=False),

    )

def downgrade():
    op.drop_table('join_requests')
