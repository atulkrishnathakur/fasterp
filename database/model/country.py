from database.dbconnection import Base
from sqlalchemy import Column, Integer, String

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String)