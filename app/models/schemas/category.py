from app.models.domain import (
    base as _base,
    category as _category_domain,
    promotion as _promotion_domain    
)


class CategoryCreate(
    _base.PromotionId,
    _category_domain.CategoryName
):
    pass


class CategoryDetail(
    _base.CategoryId,
    _base.PromotionId,
    _category_domain.CategoryName
):
    pass

    class Config:
        orm_mode = True


class CategoryUpdate(
    _base.CategoryId,
    _base.PromotionId,
    _category_domain.CategoryName
):
    pass

class CategoryDetailAll(
    _base.CategoryId,
    _base.PromotionId,
    _category_domain.CategoryName,
    _promotion_domain.PromotionName
):
    pass

    class Config:
        orm_mode = True