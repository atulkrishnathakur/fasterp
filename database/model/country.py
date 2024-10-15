from sqlalchemy import BigInteger, Column, PrimaryKeyConstraint, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='country_pkey'),
    )

    id = mapped_column(BigInteger)
    name = mapped_column(Text)
    code = mapped_column(Text, nullable=True)  # Add the new column here