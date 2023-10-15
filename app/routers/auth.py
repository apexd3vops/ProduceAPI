from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from .. import models, utils, oauth2, responses

router = APIRouter(
    prefix="/Oauth2",
    tags=['Authentication']
)


@router.post("/admins", response_model=responses.Token)
def login_admin(login_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), ):

    admin = db.query(models.Admins).filter(
        models.Admins.username == login_credentials.username).first()

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")

    if not utils.authentication(login_credentials.password, admin.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")

    access_token = oauth2.create_access_token(
        data={"strUsername": admin.username})

    return {"access_token": access_token, "token_type": "bearer"}
