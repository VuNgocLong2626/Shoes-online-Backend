from app.models.schemas import (
    uesr_services as _user_services_schemas,
    user as _user_schemas
)
from fastapi import HTTPException, status

from app.db.repositories.services.create_services import create_services
from app.db.repositories.services.get_id_user_join_user_services \
    import get_by_id_user_join_user_services
from app.db.repositories.services.get_chua_join_user_services \
    import get_by_chua_join_user_services
from app.db.repositories.services.update_services import update_services
from app.db.repositories.services.get_notchua_join_user_services \
    import get_by_notchua_join_user_services

from app.db.repositories.user_services.create_user_services \
    import create_user_services
from app.db.repositories.services.get_all_by_condition \
    import get_all_by_condition
from app.db.repositories.user.get_info_by_id_user\
    import get_info_by_id_user
from app.db.repositories.name_services.get_all_nameser_by_id\
    import get_all_nameser_by_id
from app.models.schemas.user import UserToken as _usertoken_schemas
from app.db.repositories.user_services.get_all_service_by_id import get_all_service_by_id


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
        except Exception:
            raise get_services_exception()

    def get_unconfimred_all():
        respon = get_by_chua_join_user_services()
        return respon

    def update_services(
        _in: _user_services_schemas.ServicesUpdate,
        user_in: _user_schemas.UserToken
    ):
        respon = update_services(_in, user_in)
        return respon

    def get_confimred_all():
        respon = get_by_notchua_join_user_services()
        return respon

    def get_all_by_condition(condition: int):
        uesr_service_all = get_all_by_condition(condition)
        respon = []
        for uesr_service in uesr_service_all:
            service = {
                "id_services": uesr_service.Services.id_services,
                "id_name_services": uesr_service.Services.id_name_services,
                "date_create": uesr_service.Services.date_create,
                "booking_date": uesr_service.Services.booking_date,
                "status": uesr_service.Services.status,
                "id_verifier": uesr_service.Services.id_verifier
            }
            name_service = get_all_nameser_by_id(
                uesr_service.Services.id_name_services
            )
            name_user = get_info_by_id_user(uesr_service.UserServices.id_user)
            service.update({
                "name_service": name_service.name,
                "name_user": name_user.full_name
            })
            if uesr_service.Services.id_verifier:
                name_verifier = get_info_by_id_user(
                    uesr_service.Services.id_verifier
                )
                service.update({"name_verifier": name_verifier.full_name})
            else:
                service.update({"name_verifier": "null"})
            respon.append(service)

        return respon

    def get_all_re(user_in: _usertoken_schemas):
        all_service = get_all_service_by_id(user_in.id_user)
        respon = []
        for service in all_service:
            name_service = get_all_nameser_by_id(service.Services.id_name_services)
            sv = {
                "booking_date": service.Services.booking_date,
                "date_create": service.Services.date_create,
                "status": service.Services.status,
                "name_service": name_service.name
            }
            respon.append(sv)
        return respon

def get_services_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_services_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_services_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
