
from pydantic import BaseModel, Field


class BillDetailQuantity(BaseModel):
    quantily: int = Field(alias='quantily')


class BillDetailCurrentPrice(BaseModel):
    current_price: int = Field(alias='current_price')


class BillDetailIdProductDetail(BaseModel):
    id_product_detail: int = Field(alias='id_product_detail')


class BillDetailIdSizeQuantity(BaseModel):
    id_size_quantity: int = Field(alias='id_size_quantity')