"""Current version

Revision ID: 06105f5024f0
Revises: 
Create Date: 2024-07-12 15:57:34.857917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06105f5024f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)

    # ### end Alembic commands ###
