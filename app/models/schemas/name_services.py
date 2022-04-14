from app.models.domain import (
    base as _base,
    name_services as _name_services_domain
)


class NameServicesCreate(_name_services_domain.NameServicesName):
    pass


class NameServicesDetail(_base.NameServicesId,
                         _name_services_domain.NameServicesName
                         ):
    pass

    class Config:
        orm_mode = True


class NameServicesUpdate(_base.NameServicesId,
                         _name_services_domain.NameServicesName
                         ):
    pass
