from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('recycling', sa.Column('materials_recycled', sa.String(length=100), nullable=False))

def downgrade():
    op.drop_column('recycling', 'materials_recycled')
