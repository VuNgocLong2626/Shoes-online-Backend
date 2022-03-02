from urllib import response
from sqlalchemy import false
from app.models.schemas import permission as _permission_schemas
from app.db.repositories.permission.create_permission import create_permission
from app.db.repositories.permission.get_all import get_all
from app.db.repositories.permission.delete_permission import delete_permission
from app.db.repositories.permission.update_permission import update_permission
from fastapi import HTTPException, status


class PermissionService():

    def create_permission(permission_in: _permission_schemas.PermissionCreate):
        response = create_permission(permission_in)
        if response == false:
            raise get_user_exception()
        return response

    def get_all_permission():
        respon = get_all()
        return respon

    def delete_permission(id: int):
        try:
            respon = delete_permission(id)
            return respon
        except:
            raise get_user_exception()

    def update_permission(permission_in: _permission_schemas.PermissionUpdate):
        response = update_permission(permission_in)
        return response


def get_user_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception