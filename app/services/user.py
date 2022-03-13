from urllib import response
from sqlalchemy import false
from app.models.schemas import (
    user as _user_schemas,
    info as _info_schemas
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status, Depends
from app.services.athu import (
                                get_password_hash, 
                                create_access_token,
                                verify_password)

from app.db.repositories.user.create_user import create_user
from app.db.repositories.user.get_user import get_user
from app.db.repositories.user.update_password import update_password

from app.db.repositories.info.create_info import create_info
from app.db.repositories.info.get_by_id_info import get_by_id_info
from app.db.repositories.info.update_info import update_info
from app.models.schemas.user import UserToken as _usertoken_schemas


class UserServices():

    def create_user(user_in: _user_schemas.UserCreate):
        try:
            new_info = _info_schemas.InfoCreate(**user_in.info.dict())
            info_out = create_info(new_info)

            hash_password = get_password_hash(user_in.password)
            new_user = _user_schemas.UserInDB(**{
                "id_info": info_out.id_info,
                "id_permission": user_in.id_permission,
                "account": user_in.account,
                "password": hash_password
            })
            user_out = create_user(new_user)

            user_token = _usertoken_schemas(**{
                "id_user": user_out.id_user,
                "id_info": user_out.id_info,
                "id_permission": user_out.id_permission,
                "account": user_out.account
            })
            token = create_access_token(user_token)
            return token
        except:
            raise get_user_exception()

    def get_user(user_in: _user_schemas.UserLogin):
        respon_user = get_user(user_in)
        if not respon_user:
            raise get_user_exception()

        athu_password = verify_password(user_in.password, respon_user.password)
        if not athu_password:
            raise get_user_exception()

        # Check permission

        user_token = _usertoken_schemas(**{
                "id_user": respon_user.id_user,
                "id_info": respon_user.id_info,
                "id_permission": respon_user.id_permission,
                "account": respon_user.account
            })
        token = create_access_token(user_token)
        return token

    def get_info_user(user_in: _user_schemas.UserToken):
        response = get_by_id_info(user_in.id_info)
        return response

    def update_info_user(user_in: _user_schemas.UserToken, info_in: _info_schemas.InfoUpdate):
        respon = update_info(user_in, info_in)
        if respon is None:
            raise get_user_exception()
        else:
            return respon

    def update_password(user_in: _user_schemas.UserToken, passw: _user_schemas.UserChangePassword):
        hash_password = get_password_hash(passw.password)
        respon = update_password(user_in, hash_password)
        if respon is None:
            raise get_user_exception()
        raise get_user_done()
    
    def login_form(form_data: OAuth2PasswordRequestForm = Depends()):
        user_in = _user_schemas.UserLogin(**{
            "account": form_data.username,
            "password": form_data.password
        })

        respon_user = get_user(user_in)
        if not respon_user:
            raise get_user_exception()

        athu_password = verify_password(user_in.password, respon_user.password)
        if not athu_password:
            raise get_user_exception()

        # Check permission

        user_token = _usertoken_schemas(**{
                "id_user": respon_user.id_user,
                "id_info": respon_user.id_info,
                "id_permission": respon_user.id_permission,
                "account": respon_user.account
            })
        token = create_access_token(user_token)
        return token

def get_user_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_user_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception