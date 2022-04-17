from pydantic import BaseModel
from sqlalchemy import true
from app.models.domain import (
    user as _user_domain,
    base as _base,
    info as _info_domain,
)


class token(BaseModel):
    access_token: str
    token_type: str


class User(
    _base.UserId, _user_domain.UserAccount,
    _info_domain.InfoEmail, _info_domain.InfoFullName,
    _info_domain.InfoDOB, _info_domain.InfoPhone,
):

    class Config:
        orm_mode = true


class UserInDB(BaseModel):
    hash_password: str
