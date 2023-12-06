from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.orm import Session
import urllib
from app import email_utils

from app.config import settings
from .. import oauth2

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    
    # return token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}





@router.post("/request-password-reset")
def request_password_reset(email: EmailStr, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        reset_token = oauth2.generate_reset_token(email)
        reset_token_url = "http://127.0.0.1:8000/verify-password-reset?token=" + urllib.parse.quote(reset_token)
        user.reset_token = reset_token
        user.reset_token_expiry = datetime.utcnow() + timedelta(hours=settings.reset_token_expire_hours)
        db.commit()
        email_utils.send_password_reset_email(email, reset_token)
    return {"message": "Password reset request received"}

@router.post("/verify-password-reset")
def verify_password_reset(token: str, db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    email = oauth2.verify_reset_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user or not user.reset_token or user.reset_token_expiry < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Invalid reset token")

    return {"message": "Reset token is valid"}

@router.post("/reset-password")
def reset_password(token: str, new_password: str, db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    email = oauth2.verify_reset_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user or not user.reset_token or user.reset_token_expiry < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Invalid reset token")

    # Reset the user's password and update reset token fields
    user.password = new_password
    user.reset_token = None
    user.reset_token_expiry = None
    db.commit()

    return {"message": "Password reset successfully"}