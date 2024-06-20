"""Add date_tracked column to ImpactMetric model

Revision ID: 6f684ab2933d
Revises: 864a3ae9ac30
Create Date: 2024-06-20 12:01:47.455899

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f684ab2933d'
down_revision = '864a3ae9ac30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('impact_metric', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_tracked', sa.DateTime(), nullable=False))
        batch_op.drop_column('date_posted')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('impact_metric', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_posted', mysql.DATETIME(), nullable=False))
        batch_op.drop_column('date_tracked')

    # ### end Alembic commands ###