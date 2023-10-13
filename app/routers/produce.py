from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
from app import oauth2

from ..database import get_db
from .. import models, responses, schemas


#
#
router = APIRouter(
    prefix="/produce",
    tags=['Produce']
)


@router.get('/', response_model=responses.Produce)
def get_all_produce(db: Session = Depends(get_db), limit: Optional[int] = None, search: Optional[str] = ''):
    produce = db.query(models.Produce).limit(limit).all()
    return produce 


@router.get("/{id}", response_model=responses.Produce)
def get_produce(id: int, db: Session = Depends(get_db)):
    produce = db.query(models.Produce).filter(models.Produce.id == id).first()

    if not produce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Produce with id({id}) does not exist")

    return produce

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=responses.Produce)
def create_produce(post: schemas.Produce, db: Session = Depends(get_db)):
    
    new_produce = models.Produce(**post.dict())

    db.add(new_produce)
    db.commit()
    db.refresh(new_produce)

    return new_produce

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    produce = db.query(models.Produce).filter(models.Produce.id == id).first()

    if produce == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,)
    
    
    db.delete(produce)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT, )


@router.put("/{id}", response_model=responses.Produce)
def update_post(
    id: int,
    updated_post: schemas.Produce,
    db: Session = Depends(get_db),
):
    produce = db.query(models.Produce).filter(models.Produce.id == id).first()

    if produce is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")

    db.query(models.Produce).filter(models.Produce.id == id).update(updated_post.dict())
    db.commit()
    updated_produce = db.query(models.Produce).filter(models.Produce.id == id).first()

    return updated_produce