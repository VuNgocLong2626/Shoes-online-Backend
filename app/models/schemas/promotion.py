from app.models.domain import (
    base as _base,
    promotion as _promotion_domain)


class PromotionCreate(
    _promotion_domain.PromotionName,
    _promotion_domain.PromotionDetail,
    _promotion_domain.PromotionReduction
):
    pass


class PromotionDetail(
    _base.PromotionId,
    _promotion_domain.PromotionName,
    _promotion_domain.PromotionDetail,
    _promotion_domain.PromotionReduction
):
    pass

    class Config:
        orm_mode = True


class PromotionUpdate(
    _base.PromotionId,
    _promotion_domain.PromotionName,
    _promotion_domain.PromotionDetail,
    _promotion_domain.PromotionReduction
):
    pass
