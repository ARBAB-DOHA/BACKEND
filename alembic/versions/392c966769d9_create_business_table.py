"""create_business_table

Revision ID: 392c966769d9
Revises: 5d17ea5dd029
Create Date: 2023-12-26 10:46:54.871258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '392c966769d9'
down_revision = '5d17ea5dd029'
branch_labels = None
depends_on = None


BusinessApprovalStatusEnum = sa.Enum('pending', 'approved', 'rejected', name='business_approval_status')

def upgrade():
    # Create the 'businesses' table
    op.create_table('businesses',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('community_id', sa.Integer, sa.ForeignKey('community.id'), nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('services', sa.String, nullable=False),
        sa.Column('approval_status', BusinessApprovalStatusEnum, default='pending', nullable=False),
        # Add other columns as needed
    )

def downgrade():
    # Drop the 'businesses' table
    op.drop_table('businesses')