from pydantic import BaseModel
from datetime import date

class VisitBase(BaseModel):
    date: date
    motive: str
    details: str | None = None

class VisitCreate(VisitBase):
    patient_id: int

class VisitRead(VisitBase):
    id: int
    patient_id: int

    model_config = {"from_attributes": True}
