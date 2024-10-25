"""Initial migration for all models

Revision ID: 2a37b371a5c2
Revises: 
Create Date: 2024-10-23 09:52:52.607394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a37b371a5c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=200), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('last_modified', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('setting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('aws_access_key_id', sa.String(length=200), nullable=True),
    sa.Column('aws_secret_access_key', sa.String(length=200), nullable=True),
    sa.Column('bucket_name', sa.String(length=200), nullable=True),
    sa.Column('dt_rule', sa.String(length=50), nullable=False),
    sa.Column('max_file_size', sa.Integer(), nullable=False),
    sa.Column('use_cloud', sa.Boolean(), nullable=False),
    sa.Column('delete_scans', sa.Boolean(), nullable=False),
    sa.Column('delete_scans_days_old', sa.Integer(), nullable=True),
    sa.Column('delete_scans_percent_remaining', sa.Integer(), nullable=True),
    sa.Column('device_name_includes', sa.String(length=100), nullable=True),
    sa.Column('id_file_starts_with', sa.String(length=100), nullable=True),
    sa.Column('alert_email', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('setting')
    op.drop_table('file')
    op.drop_table('account')
    # ### end Alembic commands ###