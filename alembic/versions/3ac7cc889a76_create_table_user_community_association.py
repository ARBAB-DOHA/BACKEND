"""create table user_community_association

Revision ID: 3ac7cc889a76
Revises: 1be11127b387
Create Date: 2023-12-04 15:35:35.931380

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer,Column,ForeignKey


# revision identifiers, used by Alembic.
revision = '3ac7cc889a76'
down_revision = '1be11127b387'
branch_labels = None
depends_on = None




def upgrade():
     op.create_table(
        'user_community_association',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('community_id', sa.Integer, sa.ForeignKey('community.id')),
        sa.PrimaryKeyConstraint('user_id', 'community_id'),
        sa.ForeignKey('user_id','community_id'))


def downgrade():
     op.drop_table('user_community_association')