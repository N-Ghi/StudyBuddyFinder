"""corrected mistakes

Revision ID: 28560aea6b4e
Revises: 06105f5024f0
Create Date: 2024-07-12 16:16:19.230222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28560aea6b4e'
down_revision = '06105f5024f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('strong_subject', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('weak_subject', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.drop_column('weak_subject')
        batch_op.drop_column('strong_subject')

    # ### end Alembic commands ###
