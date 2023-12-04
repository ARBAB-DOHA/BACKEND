"""Create comments table

Revision ID: e64a10a795ed
Revises: 3ac7cc889a76
Create Date: 2023-12-04 16:54:01.098499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e64a10a795ed'
down_revision = '3ac7cc889a76'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True, index=True,nullable=True),
        sa.Column('content', sa.String, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('post_id', sa.Integer, sa.ForeignKey('posts.id')),
        sa.Column('event_id', sa.Integer, sa.ForeignKey('event.id')),
        sa.Column('parent_comment_id', sa.Integer, sa.ForeignKey('comments.id')),
        
    )

def downgrade():
    op.drop_table('comments')