from datetime import date
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    date_of_birth: date
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    date_of_birth: date

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str