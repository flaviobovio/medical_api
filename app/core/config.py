from datetime import timedelta
import os
from pydantic import BaseModel

SECRET_KEY = os.getenv("SECRET_KEY", "change_me_in_production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

def access_token_expires_delta() -> timedelta:
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

class TokenData(BaseModel):
    sub: str | None = None
