"""Removed Location

Revision ID: 72d879641efe
Revises: d9eec5d24fea
Create Date: 2024-07-28 12:25:18.792171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d879641efe'
down_revision = 'd9eec5d24fea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.VARCHAR(length=255), nullable=True))

    op.create_table('events',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('summary', sa.VARCHAR(length=255), nullable=False),
    sa.Column('location', sa.VARCHAR(length=255), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('start_datetime', sa.DATETIME(), nullable=False),
    sa.Column('end_datetime', sa.DATETIME(), nullable=False),
    sa.Column('meet_link', sa.VARCHAR(length=255), nullable=True),
    sa.Column('group_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
