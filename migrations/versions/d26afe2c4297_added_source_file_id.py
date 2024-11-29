"""added source file_id

Revision ID: d26afe2c4297
Revises: 780b996940f0
Create Date: 2024-11-29 10:12:14.344655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd26afe2c4297'
down_revision = '780b996940f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_source_file', 'file', ['file_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_constraint('fk_source_file', type_='foreignkey')
        batch_op.drop_column('file_id')

    # ### end Alembic commands ###