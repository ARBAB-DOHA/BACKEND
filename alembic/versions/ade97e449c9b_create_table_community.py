"""create table community

Revision ID: ade97e449c9b
Revises: 2ee8021f3b6f
Create Date: 2023-11-25 20:10:13.040051

"""
from alembic import op
from typing import Sequence, Union
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ade97e449c9b'
down_revision = '2ee8021f3b6f'

branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table('community',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('community_name',sa.String(),nullable=False),
                    sa.Column('admin_email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('admin_email')
                    )
    pass


def downgrade():
    op.drop_table('community')
    pass