"""added plot model

Revision ID: 2e415b799ff0
Revises: 0bb3458ad04b
Create Date: 2024-11-30 10:16:09.846633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e415b799ff0'
down_revision = '0bb3458ad04b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('x_column', sa.String(length=100), nullable=False),
    sa.Column('y_column', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plot')
    # ### end Alembic commands ###
