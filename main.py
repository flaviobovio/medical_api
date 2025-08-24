from fastapi import FastAPI
from app.routers import patients, visits, auth
from app.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical API (Pydantic v2 + JWT)")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(visits.router, prefix="/visits", tags=["visits"])
