"""empty message

Revision ID: a484002ec844
Revises: 37c38fc7e288
Create Date: 2023-09-01 15:00:27.078737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a484002ec844'
down_revision = '37c38fc7e288'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.alter_column('personaje_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.alter_column('personaje_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
