from typing import Optional
from pydantic import BaseModel, EmailStr


# Schemas
class Base(BaseModel):
    username: str
    password: str
    email: EmailStr 


class Produce(BaseModel):
    strProduce: str
    strDescription: str
    strContact: str
    strProduceThumb: str
    on_sale: bool = False
    strCategory: str

class Categories(BaseModel):
    strCategory: str
    strCatDescription: str

class Admins(BaseModel):
    strUsername: str
    strPassword: str

class Login(BaseModel):
    username: str
    password: str

# response models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
