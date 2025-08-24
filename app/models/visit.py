from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database.database import Base

class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    date = Column(Date, nullable=False)
    motive = Column(String(100), nullable=False)
    details = Column(Text)

    patient = relationship("Patient", back_populates="visits")
