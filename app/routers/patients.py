from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientRead
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=PatientRead, dependencies=[Depends(get_current_user)])
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/", response_model=List[PatientRead], dependencies=[Depends(get_current_user)])
def list_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

@router.get("/{patient_id}", response_model=PatientRead, dependencies=[Depends(get_current_user)])
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.delete("/{patient_id}", dependencies=[Depends(get_current_user)])
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return {"message": "Patient deleted"}
