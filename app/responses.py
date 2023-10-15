from pydantic import BaseModel, EmailStr
from datetime import datetime


class Produce(BaseModel):
    id: int
    strProduce: str
    strDescription: str
    created_at: datetime
    strCategory: str
    strProduceThumb: str
    on_sale: bool

    class Config:
        orm_mode = True

    

class Admins(BaseModel):
    strUsername: str
    created_at: datetime

    class Config:
        orm_mode = True


class Categories(BaseModel):
    strCategory: str
    strCatDescription: str


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True