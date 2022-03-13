from app.models.domain import (
    base as _base,
    product_detail as _product_detail_domain
)


class ProductDetailCreate(
    _product_detail_domain.ProductQuantily,
    _product_detail_domain.ProductCurrentPrice
):
    pass


class ProductDetailDetail(
    _base.ProductDetailsId,
    _product_detail_domain.ProductQuantily,
    _product_detail_domain.ProductCurrentPrice
):
    pass

    class Config:
        orm_mode = True


class ProductDetailUpdate(
    _base.ProductDetailsId,
    _product_detail_domain.ProductQuantily,
    _product_detail_domain.ProductCurrentPrice
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