"""empty message

Revision ID: 623d6cbb2009
Revises: 
Create Date: 2018-07-28 15:47:33.125907

"""
from alembic import op
import sqlalchemy as sa

import bot_constants as const


# revision identifiers, used by Alembic.
revision = '623d6cbb2009'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link_provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=False),
    sa.Column('image', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('site_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invitation_description', sa.String(length=256), nullable=False),
    sa.Column('order_description', sa.String(length=256), nullable=False),
    sa.Column('admin_tm', sa.String(length=32), nullable=True),
    sa.Column('admin_email', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    site_settings_table = sa.table('site_settings',
                                   sa.column('id', sa.Integer),
                                   sa.column('invitation_description', sa.String),
                                   sa.column('order_description', sa.String),
                                   sa.column('admin_tm', sa.String),
                                   sa.column('admin_email', sa.String))
    op.bulk_insert(site_settings_table,
                   [
                       {'id': 1, 'invitation_description': const.DEFAULT_INVITATION_DESCRIPTION,
                        'order_description': const.DEFAULT_ORDER_DESCRIPTION},
                   ])
    op.create_table('steps',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('step', sa.Integer(), nullable=False),
    sa.Column('entered_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('chat_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=32), nullable=False),
    sa.Column('last_name', sa.String(length=32), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('invited_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['invited_by_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_name'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('tm_name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'chat_id', name='_user_chat_uc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_details')
    op.drop_table('user')
    op.drop_table('steps')
    op.drop_table('site_settings')
    op.drop_table('link_provider')
    # ### end Alembic commands ###
