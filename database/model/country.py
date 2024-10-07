from database.dbconnection import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column('id',Integer, primary_key=True, index=True)
    country_name = Column('country_name',String(255),nullable=False)
    status = Column('status',Integer,default=1,nullable=True)
    created_at = Column('created_at',DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column('updated_at',DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=True)
    country = relationship('Country', back_populates='state')