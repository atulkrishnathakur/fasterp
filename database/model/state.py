from database.dbconnection import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
from datetime import datetime

class State(Base):
    __tablename__ = 'states'
    
    id = Column('id',Integer, primary_key=True, index=True)
    state_name = Column('state_name',String(255),nullable=False)
    countries_id = Column('countries_id',Integer,ForeignKey('countries.id'),nullable=True)
    status = Column('status',Integer,default=1,nullable=True)
    created_at = Column('created_at',DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column('updated_at',DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=True)
    state = relationship('Country', back_populates='country')