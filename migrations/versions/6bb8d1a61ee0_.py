"""empty message

Revision ID: 6bb8d1a61ee0
Revises: de2b3e99f529
Create Date: 2025-01-04 19:44:55.008232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bb8d1a61ee0'
down_revision = 'de2b3e99f529'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.drop_column('episode_id')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_column('is_active')
        batch_op.drop_column('homeworld')

    with op.batch_alter_table('species', schema=None) as batch_op:
        batch_op.drop_column('homeworld')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('species', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld', sa.VARCHAR(length=80), autoincrement=False, nullable=False))

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))

    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.add_column(sa.Column('episode_id', sa.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###