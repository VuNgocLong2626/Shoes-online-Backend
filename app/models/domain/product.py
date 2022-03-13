from pydantic import BaseModel, Field


class ProductName(BaseModel):
    name: str = Field(alias='name')


class ProductDetail(BaseModel):
    detail: str = Field(alias='detail')


class ProductMoney(BaseModel):
    money: str = Field(alias='money')

