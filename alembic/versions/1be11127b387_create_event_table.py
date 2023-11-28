"""create event table

Revision ID: 1be11127b387
Revises: 34f83cf0a9a5
Create Date: 2023-11-28 15:38:49.140800

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import TIMESTAMP


# revision identifiers, used by Alembic.
revision = '1be11127b387'
down_revision = '34f83cf0a9a5'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'event',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.Text),
        sa.Column('date_time', TIMESTAMP, nullable=False),
        sa.Column('community_id', sa.Integer, sa.ForeignKey('community.id', ondelete='CASCADE'), nullable=False),
    )

def downgrade():
    op.drop_table('event')