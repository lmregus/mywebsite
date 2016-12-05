"""empty message

Revision ID: 61f20ad4a437
Revises: 977bb6ada425
Create Date: 2016-11-28 12:11:33.868682

"""

# revision identifiers, used by Alembic.
revision = '61f20ad4a437'
down_revision = '977bb6ada425'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('end_date', sa.DateTime(), nullable=True))
    op.add_column('job', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.drop_column('job', 'time_period')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('time_period', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.drop_column('job', 'start_date')
    op.drop_column('job', 'end_date')
    ### end Alembic commands ###