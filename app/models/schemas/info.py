from app.models.domain import (
                                base as _base,
                                info as _info_domain)

class InfoCreate(
    _info_domain.InfoFullName, _info_domain.InfoEmail,
    _info_domain.InfoPhone, _info_domain.InfoDOB
):
    pass


class InfoDetail(
    _base.InfoId, _info_domain.InfoFullName,
    _info_domain.InfoEmail, _info_domain.InfoPhone,
    _info_domain.InfoDOB
):
    pass

    class Config:
        orm_mode = True


class InfoUpdate(
    _info_domain.InfoFullName,
    _info_domain.InfoEmail, _info_domain.InfoPhone,
    _info_domain.InfoDOB
):
    pass
