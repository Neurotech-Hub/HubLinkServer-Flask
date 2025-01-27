"""added Source model

Revision ID: efdec8479fda
Revises: 1bf0761ba535
Create Date: 2024-11-28 09:32:03.008700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efdec8479fda'
down_revision = '1bf0761ba535'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('file_filter', sa.String(length=200), nullable=False),
    sa.Column('include_columns', sa.String(length=500), nullable=False),
    sa.Column('data_points', sa.Integer(), nullable=False),
    sa.Column('tail_only', sa.Boolean(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('source')
    # ### end Alembic commands ###
