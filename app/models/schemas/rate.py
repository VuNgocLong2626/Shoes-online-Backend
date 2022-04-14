from app.models.domain import (
    base as _base,
    rate as _rate_domain)


class RateCreate(
    _rate_domain.RateStart
):
    pass


class RateDetail(
    _base.RateId,
    _rate_domain.RateStart
):
    pass

    class Config:
        orm_mode = True


class RateUpdate(
    _base.RateId,
    _rate_domain.RateStart
):
    pass
