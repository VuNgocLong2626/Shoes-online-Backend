from pydantic import BaseModel, Field


class SizeQuantitySold(BaseModel):
    quantity_sold: int = Field(None, alias='quantity_sold')


class ProductQuantityQuantity(BaseModel):
    quantity: int = Field(None, alias='quantity')
