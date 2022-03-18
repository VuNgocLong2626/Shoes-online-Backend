from app.models.domain import (
                                base as _base,
                                size_quatity as _size_quatity_domain)


class SizeQuantityIn(
    _base.SizeId,
    _size_quatity_domain.SizeQuantitySold,
    _size_quatity_domain.ProductQuantityQuantity
):
    pass


class SizeQuantityCreate(
    _base.SizeId,
    _base.ProductDetailsId,
    _size_quatity_domain.SizeQuantitySold,
    _size_quatity_domain.ProductQuantityQuantity
):
    pass 


class SizeQuantityDetail(
    _base.ProductDetailsId,
    _base.SizeId,
    _base.SizeQuantityId,
    _size_quatity_domain.SizeQuantitySold,
    _size_quatity_domain.ProductQuantityQuantity
):
    pass 

    class Config:
        orm_mode = True


class SizeQuantityUpdate(
    _base.ProductDetailsId,
    _base.SizeId,
    _base.SizeQuantityId,
    _size_quatity_domain.SizeQuantitySold,
    _size_quatity_domain.ProductQuantityQuantity
):
    pass 

