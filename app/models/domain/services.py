from pydantic import BaseModel, Field
from datetime import date


class ServicesBook(BaseModel):
    booking_date: date = Field(None, alias='booking_date')


class ServicesCreate(BaseModel):
    date_create: date = Field(alias='date_create')


class ServicesStatus(BaseModel):
    status: str = Field(min_length=2,
                        max_length=250,
                        alias='status')
