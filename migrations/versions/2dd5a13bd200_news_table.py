"""news table

Revision ID: 2dd5a13bd200
Revises: fc4d0fda4b63
Create Date: 2018-12-17 10:54:53.919570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dd5a13bd200'
down_revision = 'fc4d0fda4b63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('status', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'status')
    # ### end Alembic commands ###
