"""updated price and tables

Revision ID: b3502cfa1303
Revises: fe345a75fc9b
Create Date: 2024-01-30 18:08:16.417912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3502cfa1303'
down_revision = 'fe345a75fc9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apartment', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('bedrooms',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apartment', schema=None) as batch_op:
        batch_op.alter_column('bedrooms',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###
