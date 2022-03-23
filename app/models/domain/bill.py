from pydantic import BaseModel, Field
from datetime import date


class BillStatus(BaseModel):
    status: str = Field(None, alias='status')


class BillCreate(BaseModel):
    date_create: date = Field(None, alias='date_create')


class BillTotal(BaseModel):
    total: str = Field(None, alias='total')


class BillMethod(BaseModel):
    method: str = Field(None, alias='method')