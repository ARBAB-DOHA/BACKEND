"""Create holidays table

Revision ID: a08ae49e9fbd
Revises: 8817e46cc2b9
Create Date: 2023-12-13 14:47:16.470510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a08ae49e9fbd'
down_revision = '8817e46cc2b9'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'holidays',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('date', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('holidays')