"""empty message

Revision ID: 941cc2b697f8
Revises: 15c168b5623e
Create Date: 2016-11-24 18:39:53.590261

"""

# revision identifiers, used by Alembic.
revision = '941cc2b697f8'
down_revision = '15c168b5623e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('school', sa.String(length=128), nullable=True),
    sa.Column('_type', sa.String(length=64), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('time_period', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('education')
    ### end Alembic commands ###
