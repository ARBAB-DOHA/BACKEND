"""add_reset_columns

Revision ID: 8817e46cc2b9
Revises: e64a10a795ed
Create Date: 2023-12-05 13:34:36.141526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8817e46cc2b9'
down_revision = 'e64a10a795ed'
branch_labels = None
depends_on = None
def upgrade():
    # Add the new columns for reset token
    op.add_column('users', sa.Column('reset_token', sa.String(length=255)))
    op.add_column('users', sa.Column('reset_token_expiry', sa.DateTime()))

def downgrade():
    # Define the operations to undo the changes
    op.drop_column('users', 'reset_token')
    op.drop_column('users', 'reset_token_expiry')