"""empty message

Revision ID: 9c0d0556428c
Revises: 941cc2b697f8
Create Date: 2016-11-28 10:37:05.692808

"""

# revision identifiers, used by Alembic.
revision = '9c0d0556428c'
down_revision = '941cc2b697f8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('education', sa.Column('date', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('education', 'date')
    ### end Alembic commands ###
