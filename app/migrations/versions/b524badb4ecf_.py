"""empty message

Revision ID: b524badb4ecf
Revises: 8ffb29ee7635
Create Date: 2016-11-24 17:14:55.498644

"""

# revision identifiers, used by Alembic.
revision = 'b524badb4ecf'
down_revision = '8ffb29ee7635'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('time_period', sa.String(length=64), nullable=True),
    sa.Column('company', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    ### end Alembic commands ###