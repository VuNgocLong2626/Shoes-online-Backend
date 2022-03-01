from matplotlib.pyplot import cla
from pydantic import BaseModel, Field
import datetime as date


class BillStatus(BaseModel):
    status: str = Field(alias='status')


class BillCreate(BaseModel):
    date_create: date = Field(alias='date_create')


class BillTotal(BaseModel):
    total: str = Field(alias='total')


class BillMethod(BaseModel):
    method: str = Field(alias='method')