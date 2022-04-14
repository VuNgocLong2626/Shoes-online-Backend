from app.models.domain import (
    base as _base,
    services as _services_domain)


class ServicesCreate(
    _base.NameServicesId,
    _services_domain.ServicesBook,
    _services_domain.ServicesCreate,
    _services_domain.ServicesStatus
):
    pass


class SevicesDetail(
    _base.ServicesId,
    _base.VerifierId,
    _base.NameServicesId,
    _services_domain.ServicesBook,
    _services_domain.ServicesCreate,
    _services_domain.ServicesStatus
):
    pass

    class Config:
        orm_mode = True


class ServicesUpdate(
    _base.ServicesId,
    _services_domain.ServicesStatus
):
    pass


class UserServicesCreate(
    _base.ServicesId,
    _base.UserId
):
    pass


class UserServiecesDetail(
    _base.ServicesId,
    _base.UserId
):

    pass

    class Config:
        orm_mode = True


class ServicesInDB(
    _base.NameServicesId,
    _base.UserId,
    _services_domain.ServicesBook,
    _services_domain.ServicesCreate,
    _services_domain.ServicesStatus,
):
    pass
