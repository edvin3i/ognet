from sqlalchemy.orm import Session
from app.models.extinguisher import Extinguisher
from app.schemas.extinguisher import ExtinguisherCreate, ExtinguisherUpdate

def get_extinguisher(db: Session, extinguisher_id: int):
    return db.query(Extinguisher).filter(Extinguisher.id == extinguisher_id).first()

def get_extinguishers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Extinguisher).offset(skip).limit(limit).all()

def create_extinguisher(db: Session, extinguisher: ExtinguisherCreate):
    db_extinguisher = Extinguisher(**extinguisher.model_dump( ))
    db.add(db_extinguisher)
    db.commit()
    db.refresh(db_extinguisher)
    return db_extinguisher

def update_extinguisher(db: Session, extinguisher_id: int, extinguisher: ExtinguisherUpdate ):
    db_extinguisher = get_extinguisher(db, extinguisher_id)
    if db_extinguisher:
        for key, value in extinguisher.dicd(exclude_unset=True).items():
            setattr(db_extinguisher, key, value)
        db.commit()
        db.refresh(db_extinguisher)
    return db_extinguisher

def delete_extinguisher(db: Session, extinguisher_id: int):
    db_extinguisher = get_extinguisher(db, extinguisher_id)
    if db_extinguisher:
        db.delete(db_extinguisher)
        db.commit()
    return db_extinguisher
