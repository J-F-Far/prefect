"""empty message

Revision ID: dc729e5c0448
Revises: 7201de756d85
Create Date: 2022-12-05 18:45:19.631375

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "dc729e5c0448"
down_revision = "7201de756d85"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("flow", sa.Column("description", sa.TEXT(), nullable=True))


def downgrade():
    with op.batch_alter_table("flow", schema=None) as batch_op:
        batch_op.drop_column("description")
