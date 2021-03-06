"""Add comment model and relationships

Revision ID: 715c2610ab3f
Revises: 6baad84874d0
Create Date: 2022-03-14 13:59:40.315269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '715c2610ab3f'
down_revision = '6baad84874d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
