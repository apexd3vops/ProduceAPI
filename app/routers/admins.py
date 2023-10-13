from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
from app import oauth2

from ..database import get_db
from .. import models, responses, schemas


#
#
router = APIRouter(
    prefix="/admins",
    tags=['Admins']
)



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=responses.Admins)
def create_produce(new_admin: schemas.Admins, db: Session = Depends(get_db)):
    new_admin.strPassword = utils.hash(new_admin.strPassword)
    admin = models.Admins(**new_admin.dict())
    db.add(admin)
    db.commit()
    db.refresh(admin)

    return admin


@router.get("/{id}", response_model=responses.Admins)
def get_admin(id: int, db: Session = Depends(get_db)):
    admin = db.query(models.Admins).filter(models.Admins.id == id).first()

    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Farm does not exist")

    return admin