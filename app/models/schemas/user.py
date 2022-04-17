from app.models.domain import (
    base as _base,
    user as _user_domain)
from app.models.schemas import info as _info_shemas
from pydantic import Field, BaseModel


class UserCreate(
    _user_domain.UserAccount,
    _user_domain.UserPassword,
    _base.PermissionId
):
    info: _info_shemas.InfoCreate

    class Config:
        orm_mode = True


class UserDetail(
    _base.UserId,
    _base.InfoId,
    _base.PermissionId,
    _user_domain.UserAccount
):
    info: _info_shemas.InfoCreate

    class Config:
        orm_mode = True


class UserChangePassword(
    _user_domain.UserPassword
):
    pass


class UserInDB(
    _base.InfoId,
    _base.PermissionId,
    _user_domain.UserAccount,
    _user_domain.UserPassword
):
    pass

    class Config:
        orm_mode = True


class UserToken(
    _base.UserId,
    _base.InfoId,
    _base.PermissionId,
    _user_domain.UserAccount
):
    pass


class UserLogin(
    _user_domain.UserAccount,
    _user_domain.UserPassword
):
    pass

    class Config:
        orm_mode = True


class UserCheckPassWord(BaseModel):
    password: str = Field(alias='password')
    password_old: str = Field(alias='password_old')
