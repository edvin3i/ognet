from sqlalchemy import Column, Integer, String, Date
from app.db import Base

class Extinguisher(Base):
    __tablename__ = 'extinguisher'

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String, unique=True, index=True)
    location = Column(String)
    prev_check_date = Column(Date)
    next_check_date = Column(Date)
    created_at = Column(Date)
    updated_at = Column(Date)
    notes = Column(String, nullable=True)
