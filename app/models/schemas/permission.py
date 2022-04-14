from app.models.domain import (
    base as _base,
    permission as _permission_domain
)


class PermissionCreate(_permission_domain.PermissionName):
    pass


class PermissionDetail(
    _base.PermissionId,
    _permission_domain.PermissionName
):
    pass

    class Config:
        orm_mode = True


class PermissionUpdate(
    _base.PermissionId,
    _permission_domain.PermissionName
):
    pass
