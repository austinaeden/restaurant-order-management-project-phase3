"""created tables

Revision ID: 490bcd233988
Revises: 632954d8d037
Create Date: 2023-09-06 22:31:11.866305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '490bcd233988'
down_revision = '632954d8d037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('res_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('res_id')
    )
    op.create_table('menu_item',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.res_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.cus_id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.res_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('ordered_item',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('menu_item_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menu_item_id'], ['menu_item.item_id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.order_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ordered_item')
    op.drop_table('order')
    op.drop_table('menu_item')
    op.drop_table('restaurant')
    # ### end Alembic commands ###
