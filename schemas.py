from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    fist_name: str = Field(..., max_length=25)
    second_name: str
    age: int = Field(..., gt=15, lt=90, description='error must be more 15 and less then 90')

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15 > 90:
    #         raise ValueError('error value')
    #     return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summery: str
    genres: List[Genre] = []
    pages: int


class BookOut(Book):
    id: int