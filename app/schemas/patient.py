from pydantic import BaseModel, computed_field
from datetime import date

class PatientBase(BaseModel):
    name: str
    document: str
    gender: str
    birth_date: date
    address: str | None = None
    city: str | None = None
    state: str | None = None
    phone: str | None = None
    personal_history: str | None = None
    family_history: str | None = None

class PatientCreate(PatientBase):
    pass

class PatientRead(PatientBase):
    id: int

    model_config = {"from_attributes": True}

    @computed_field
    @property
    def age(self) -> int:
        today = date.today()
        return (
            today.year - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
