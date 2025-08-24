from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from app.database.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    document = Column(String(20), nullable=False, unique=True)
    gender = Column(String(1), nullable=False)
    birth_date = Column(Date, nullable=False)
    address = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    phone = Column(String(25))
    personal_history = Column(Text)
    family_history = Column(Text)

    visits = relationship("Visit", back_populates="patient", cascade="all, delete-orphan")
