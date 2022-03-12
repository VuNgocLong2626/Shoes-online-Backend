from app.models.domain import (
                                base as _base,
                                gender as _gender_domain)


class GenderCreate(
    _gender_domain.GenderName
):
    pass


class GenderDetail(
    _base.GenderId,
    _gender_domain.GenderName
):
    pass

    class Config:
        orm_mode = True


class GenderUpdate(
    _base.GenderId,
    _gender_domain.GenderName
):
    pass