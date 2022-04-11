from app.models.domain import (
                                base as _base,
                                product as _product_domain)
from app.models.schemas import product_detail as _product_detail_schemas
from typing import List, Dict
from pydantic import BaseModel, Field

class ProductCreate(
    _product_domain.ProductDetail,
    _product_domain.ProductMoney,
    _product_domain.ProductName
):
    product_detail: List[_product_detail_schemas.ProductDetailIn]

    class Config:
        orm_mode = True


class ProductCreateForm(
    _base.CategoryId,
    _base.GenderId,
    _product_domain.ProductDetail,
    _product_domain.ProductMoney,
    _product_domain.ProductName
):
    pass

class ProductDetailForm(
    _base.ProductId,
    _base.CategoryId,
    _base.GenderId,
    _product_domain.ProductDetail,
    _product_domain.ProductMoney,
    _product_domain.ProductName
):
    pass

    class Config:
        orm_mode = True

class ProductUpdateForm(
    _base.ProductId,
    _base.CategoryId,
    _base.GenderId,
    _product_domain.ProductDetail,
    _product_domain.ProductMoney,
    _product_domain.ProductName
):
    pass


class ProductFillter(BaseModel):
    list_id_category: List[int] = Field(None)
    list_id_color: List[int] =  Field(None)
    id_gender: int = Field(alias='id_gender')
    
    class Config:
                orm_mode = True