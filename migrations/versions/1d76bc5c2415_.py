"""empty message

Revision ID: 1d76bc5c2415
Revises: 5aec2b50a422
Create Date: 2022-02-07 16:28:19.639591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d76bc5c2415'
down_revision = '5aec2b50a422'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instructions', sa.Column('stepTitle', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('instructions', 'stepTitle')
    # ### end Alembic commands ###
