"""empty message

Revision ID: 1609ee0434be
Revises: None
Create Date: 2017-04-03 20:42:53.532902

"""

# revision identifiers, used by Alembic.
revision = '1609ee0434be'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_entry', sa.Column('entry_name', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_entry', 'entry_name')
    ### end Alembic commands ###