from pydantic import BaseModel, Field


class ImagePath(BaseModel):
    path: str = Field(alias='path')


class SizeNumber(BaseModel):
    size_number: int = Field(alias='size_number')


class ColorHex(BaseModel):
    hex: str = Field(alias='hex')
