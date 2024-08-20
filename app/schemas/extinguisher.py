from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExtinguisherBase(BaseModel):
    serial_number: str
    location: str
    next_check_date: date
    prev_check_date: date
    created_at: date
    updated_at: date
    notes: Optional[str] = None

class ExtinguisherCreate(ExtinguisherBase):
    pass

class ExtinguisherUpdate(ExtinguisherBase):
    pass

class ExtinguisherInDBBase(BaseModel):
    id: int

    class Config:
        from_attributes = True

class Extinguisher(ExtinguisherInDBBase):
    pass
