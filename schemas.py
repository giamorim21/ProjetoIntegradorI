from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BaseModel):
    id: int
    title: str
    author: str

    class Config:
        orm_mode = True

class ReadingHistoryCreate(BaseModel):
    user_id: int
    book_id: int
