"""add content column to posts table

Revision ID: bfa13b8c32e5
Revises: dba03ef2cc66
Create Date: 2022-11-14 20:11:01.675477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfa13b8c32e5'
down_revision = 'dba03ef2cc66'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
