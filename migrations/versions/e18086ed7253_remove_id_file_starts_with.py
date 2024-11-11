"""remove id_file_starts_with

Revision ID: e18086ed7253
Revises: cf0ae58170bd
Create Date: 2024-11-11 07:46:23.255065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e18086ed7253'
down_revision = 'cf0ae58170bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('setting', schema=None) as batch_op:
        batch_op.drop_column('id_file_starts_with')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('setting', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_file_starts_with', sa.VARCHAR(length=100), nullable=False))

    # ### end Alembic commands ###