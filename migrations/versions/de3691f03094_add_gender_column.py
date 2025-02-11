"""Add gender column

Revision ID: de3691f03094
Revises: 
Create Date: 2025-02-11 17:39:49.786317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de3691f03094'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Username', sa.String(length=255), nullable=False),
    sa.Column('Full_name', sa.String(length=255), nullable=False),
    sa.Column('Email', sa.String(length=255), nullable=False),
    sa.Column('PhoneNo', sa.String(length=15), nullable=False),
    sa.Column('user_password', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('PhoneNo'),
    sa.UniqueConstraint('Username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
