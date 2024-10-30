from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped
from database.dbconnection import Base
from database.dbconfig import SCHEMA_SALES

class Country(Base):
    __tablename__ = 'countries'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='countries_pkey'),
        {'schema': SCHEMA_SALES} # schema is the postgresql schema
    )

    id: Mapped[BigInteger] = mapped_column('id',BigInteger,primary_key=True,autoincrement=True,nullable=False)
    countryname: Mapped[String] = mapped_column('country_name',String(255),nullable=False)
    status:Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    countrycode:Mapped[String] = mapped_column('country_code',String(255),nullable=True)
    created_at:Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at:Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
