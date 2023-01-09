"""create initial tables

Revision ID: 65fe89558cbc
Revises: 
Create Date: 2023-01-08 15:03:32.318049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65fe89558cbc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the first table and define the columns
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('desc', sa.Unicode(200)),
    )


def downgrade() -> None:
    # this is the first revision - there is no downgrade
    pass
