"""add column to keys

Revision ID: d71601e22de1
Revises: 
Create Date: 2021-04-26 19:23:30.644184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd71601e22de1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('keys', sa.Column('scan_status', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('keys', 'scan_status')
    # ### end Alembic commands ###
