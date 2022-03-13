from pydantic import BaseModel, Field


class ImagePath(BaseModel):
    path: str = Field(alias='path')


class SizeNumber(BaseModel):
    size_number: int = Field(alias='size_number')


class ColorHex(BaseModel):
    hex: str = Field(alias='hex')


class ProductCurrentPrice(BaseModel):
    quantity_sold: str = Field(alias='current_price')


class ProductQuantily(BaseModel):
    quantily: str = Field(alias='quantily')