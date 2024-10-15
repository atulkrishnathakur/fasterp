"""create account table

Revision ID: 33f75298723e
Revises: 84af06e88411
Create Date: 2024-10-14 11:26:56.240932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33f75298723e'
down_revision: Union[str, None] = '84af06e88411'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade() -> None:
    op.drop_table('account')
