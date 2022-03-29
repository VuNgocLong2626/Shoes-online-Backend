from sqlalchemy import false
from app.models.schemas import (
    uesr_services as _user_services_schemas,
    user as _user_schemas
)
from fastapi import HTTPException, status

from app.db.repositories.services.create_services import create_services
from app.db.repositories.services.get_id_user_join_user_services import get_by_id_user_join_user_services
from app.db.repositories.services.get_chua_join_user_services import get_by_chua_join_user_services
from app.db.repositories.services.update_services import update_services
from app.db.repositories.services.get_notchua_join_user_services import get_by_notchua_join_user_services

from app.db.repositories.user_services.create_user_services import create_user_services


class ServicesServices():
    def create_services(_in: _user_services_schemas.ServicesInDB):
        services = _user_services_schemas.ServicesCreate(**_in.dict())
        respon_services = create_services(services)
        if respon_services is None: 
            raise get_services_create_exception()

        user_services = _user_services_schemas.UserServicesCreate(**{
            "id_services": respon_services.id_services,
            "id_user": _in.id_user
        })
        respon_user_services = create_user_services(user_services)
        return respon_user_services

    def get_id_user(id_user: int):
        try:
            respon = get_by_id_user_join_user_services(id_user)
            return respon
        except:
            raise get_services_exception()
    
    def get_unconfimred_all():
        respon = get_by_chua_join_user_services()
        return respon

    def update_services(_in: _user_services_schemas.ServicesUpdate, user_in: _user_schemas.UserToken):
        respon = update_services(_in, user_in)
        return respon

    def get_confimred_all():
        respon = get_by_notchua_join_user_services()
        return respon


def get_services_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_services_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_services_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception