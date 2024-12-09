"""rm success and add state to source

Revision ID: 75f13ca35deb
Revises: 20f8cb4ccb98
Create Date: 2024-12-05 17:18:59.328647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75f13ca35deb'
down_revision = '20f8cb4ccb98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('state', sa.String(length=50), nullable=False, server_default=''))
        batch_op.drop_column('success')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('success', sa.BOOLEAN(), server_default=sa.text("'0'"), nullable=False))
        batch_op.drop_column('state')

    # ### end Alembic commands ###
