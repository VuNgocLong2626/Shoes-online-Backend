from app.models.domain import (
    base as _base,
    product_detail as _product_detail_domain
)
from app.models.schemas import size_quatity as _size_quatity_schemas
from typing import List


class ProductDetailIn(
    _base.ColorId
):
    size_quantity: List[_size_quatity_schemas.SizeQuantityIn]

    class Config:
        orm_mode = True


class ProductDetailCreate(
    _base.ColorId,
    _base.ProductId
):
    pass


class ProductDetailDetail(
    _base.ProductDetailsId,
    _base.ColorId,
    _base.ProductId
):
    pass

    class Config:
        orm_mode = True


class ProductDetailAll(
    _base.ProductDetailsId,
    _base.ColorId,
    _base.ProductId
):
    list_image: List[_product_detail_domain.ImagePath]


class ProductDetailUpdate(
    _base.ProductDetailsId,
    _base.ColorId,
    _base.ProductId
):
    pass


class ColorCreate(
    _product_detail_domain.ColorHex
):
    pass


class ColorDetail(
    _base.ColorId,
    _product_detail_domain.ColorHex
):
    pass

    class Config:
        orm_mode = True


class ColorUpdate(
    _base.ColorId,
    _product_detail_domain.ColorHex
):
    pass


class SizeCreate(
    _product_detail_domain.SizeNumber
):
    pass


class SizeDetail(
    _base.SizeId,
    _product_detail_domain.SizeNumber
):
    pass

    class Config:
        orm_mode = True


class SizeUpdate(    
    _base.SizeId,
    _product_detail_domain.SizeNumber
):
    pass


class ImageCreate(
    _product_detail_domain.ImagePath,
    _base.ProductDetailsId
):
    pass

class ImageOutDB(
    _product_detail_domain.ImagePath
):
    pass

    class Config:
        orm_mode = True

class ImageDetail(
    _base.ImageId,
    _base.ProductDetailsId,
    _product_detail_domain.ImagePath
):
    pass

    class Config:
        orm_mode = True


class ImageUpdate(
    _base.ImageId,
    _base.ProductDetailsId,
    _product_detail_domain.ImagePath
):
    pass