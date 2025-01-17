"""source datetime col

Revision ID: a0e46fbf393c
Revises: e1f79621f43a
Create Date: 2025-01-17 08:41:29.556926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0e46fbf393c'
down_revision = 'e1f79621f43a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('datetime_column', sa.String(length=100), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_column('datetime_column')

    # ### end Alembic commands ###
