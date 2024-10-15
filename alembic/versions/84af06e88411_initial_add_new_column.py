"""initial add new column

Revision ID: 84af06e88411
Revises: 4f6d19b3053b
Create Date: 2024-10-14 11:06:55.899661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84af06e88411'
down_revision: Union[str, None] = '4f6d19b3053b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('country', sa.Column('code', sa.BigInteger))

def downgrade() -> None:
    op.drop_column('country', 'code')
