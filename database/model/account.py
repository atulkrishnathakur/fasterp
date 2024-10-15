from sqlalchemy import BigInteger, Column, PrimaryKeyConstraint, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='account_pkey'),
    )

    id = mapped_column(Integer)
    name = mapped_column('name',String(50),nullable=False)
    description = mapped_column('description',description, Unicode(200))  # Add the new column here