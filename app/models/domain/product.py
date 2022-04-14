from pydantic import BaseModel, Field


class ProductName(BaseModel):
    name: str = Field(None, alias='name')


class ProductDetail(BaseModel):
    detail: str = Field(None, alias='detail')


class ProductMoney(BaseModel):
    money: str = Field(None, alias='money')


class ProductMSP(BaseModel):
    msp: str = Field(None, alias='msp')
