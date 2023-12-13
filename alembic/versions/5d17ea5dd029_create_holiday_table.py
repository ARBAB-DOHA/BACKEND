"""create holiday table

Revision ID: 5d17ea5dd029
Revises: a08ae49e9fbd
Create Date: 2023-12-13 15:20:27.835952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d17ea5dd029'
down_revision = 'a08ae49e9fbd'
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