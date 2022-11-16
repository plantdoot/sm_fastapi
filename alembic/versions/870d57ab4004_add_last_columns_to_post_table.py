"""add last columns to post table

Revision ID: 870d57ab4004
Revises: c5b0b2d5712e
Create Date: 2022-11-15 19:05:55.936838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '870d57ab4004'
down_revision = 'c5b0b2d5712e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
