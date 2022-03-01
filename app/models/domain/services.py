from pydantic import BaseModel, Field
import datetime as date


class ServicesBook(BaseModel):
    booking_date: date = Field(None, alias='booking_date')


class ServicesCreate(BaseModel):
    data_create: date = Field(None, alias='data_create')


class ServicesStatus(BaseModel):
    status:str = Field(min_length=2,
                        max_length=250,
                        alias='status')