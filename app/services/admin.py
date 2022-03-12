from sqlalchemy import false
from app.models.schemas import (
    user as _admin_schemas,
    info as _info_schemas
)
from app.services.athu import (
                                get_password_hash, 
                                create_access_token,
                                verify_password)
from fastapi import HTTPException, status
from app.db.repositories.admin.get_admin import get_admin
from app.db.repositories.user.create_user import create_user

from app.db.repositories.permission.get_by_id_permission import get_by_id_permission
from app.db.repositories.info.create_info import create_info
from app.db.repositories.info.update_info import update_info
from app.db.repositories.info.get_by_id_info import get_by_id_info


class AdminServices():

    def get_admin(admin_in: _admin_schemas.UserLogin):
        respon_admin = get_admin(admin_in)
        respon_permission = get_by_id_permission(respon_admin.id_permission)
        if respon_permission.name == "KhachHang":
            raise get_user_exception()

        athu = verify_password(admin_in.password, respon_admin.password)
        if not athu:
            raise get_user_exception()

        admin_token = _admin_schemas.UserToken(**{
                "id_user": respon_admin.id_user,
                "id_info": respon_admin.id_info,
                "id_permission": respon_admin.id_permission,
                "account": respon_admin.account
            })
        token = create_access_token(admin_token)
        return token

    def create_admin(admin_in: _admin_schemas.UserToken, admin_create: _admin_schemas.UserCreate):
        respon_permission = get_by_id_permission(admin_in.id_permission)
        if respon_permission.name != "Admin":
            raise get_user_exception()
        
        new_info = _info_schemas.InfoCreate(**admin_create.info.dict())
        info_out = create_info(new_info)

        hash_password = get_password_hash(admin_create.password)
        new_user = _admin_schemas.UserInDB(**{
                "id_info": info_out.id_info,
                "id_permission": admin_create.id_permission,
                "account": admin_create.account,
                "password": hash_password
            })
        user_out = create_user(new_user)
        raise get_user_done()
    
    def update_admin_info(admin_in: _admin_schemas.UserToken, admin_info: _info_schemas.InfoUpdate):
        respon_permission = get_by_id_permission(admin_in.id_permission)
        if respon_permission.name == "KhachHang":
            raise get_user_exception()

        respon = update_info(admin_in, admin_info)
        if respon is None:
            raise get_user_exception()
        else:
            return respon

    def get_info_admin_by_id(admin_in: _admin_schemas.UserToken):
        response = get_by_id_info(admin_in.id_info)
        return response



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