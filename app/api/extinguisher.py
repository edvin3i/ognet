from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import extinguisher as crud_extinguisher
from app.schemas.extinguisher import ExtinguisherCreate, ExtinguisherUpdate
from app.db import get_db

router = APIRouter

@router.post("/", response_model=ExtinguisherCreate)
def create_extinguisher(extinguisher: ExtinguisherCreate, db: Session = Depends(get_db)):
    return crud_extinguisher.create_extinguisher(db=db, extinguisher=extinguisher)

@router.get("/{extinguisher_id}", response_model=ExtinguisherUpdate)
def read_extinguisher(extingisher_id: int, db: Session = Depends(get_db)):
    db_extinguisher = crud_extinguisher.get_extinguisher(db, extinguisher_id=extingisher_id)
    if db_extinguisher is None:
        raise HTTPException(status_code=404, detail="Огнетушитель не найден!")
    return db_extinguisher

@router.put("/{extinguisher_id}", response_model=ExtinguisherUpdate)
def update_extinguisher(extinguisher_id: int, extinguisher: ExtinguisherUpdate, db: Session = Depends(get_db)):
    return crud_extinguisher.update_extinguisher(db=db, extinguisher_id=extinguisher_id, extinguisher=extinguisher)

@router.delete("/{extinguisher_id}", response_model=ExtinguisherUpdate)
def delete_extinguisher(extinguisher_id: int, db: Session = Depends(get_db)):
    return crud_extinguisher.delete_extinguisher(db=db, extinguisher_id=extinguisher_id)
