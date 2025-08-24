from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.models.visit import Visit
from app.schemas.visit import VisitCreate, VisitRead
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=VisitRead, dependencies=[Depends(get_current_user)])
def create_visit(visit: VisitCreate, db: Session = Depends(get_db)):
    db_visit = Visit(**visit.model_dump())
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit

@router.get("/", response_model=List[VisitRead], dependencies=[Depends(get_current_user)])
def list_visits(db: Session = Depends(get_db)):
    return db.query(Visit).all()

@router.get("/{visit_id}", response_model=VisitRead, dependencies=[Depends(get_current_user)])
def get_visit(visit_id: int, db: Session = Depends(get_db)):
    visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
    return visit

@router.delete("/{visit_id}", dependencies=[Depends(get_current_user)])
def delete_visit(visit_id: int, db: Session = Depends(get_db)):
    visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
    db.delete(visit)
    db.commit()
    return {"message": "Visit deleted"}
