from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    return payload


def require_teacher(user: dict = Depends(get_current_user)):
    if user.get("role") != "teacher":
        raise HTTPException(status_code=403, detail="Teacher access required")
    return user