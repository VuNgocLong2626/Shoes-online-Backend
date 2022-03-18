from sqlalchemy import false
from app.models.schemas import name_services as _nameser_schemas
from fastapi import HTTPException, status
from app.db.repositories.name_services.create_nameser import create_nameser
from app.db.repositories.name_services.get_all_nameser import get_all_nameser
from app.db.repositories.name_services.delete_nameser import delete_nameser
from app.db.repositories.name_services.update_nameser import update_nameser


class NameServicesServices():

    def create_nameser(nameser_in: _nameser_schemas.NameServicesCreate):
        respon = create_nameser(nameser_in)
        if respon is None:
            raise get_namser_create_exception()
        return respon

    def get_all_nameser():
        respon = get_all_nameser()
        return respon

    def delete_nameser(id_nameser: int):
        respon = delete_nameser(id_nameser)
        return respon

    def update_nameser(nameser_in: _nameser_schemas.NameServicesUpdate):
        respon = update_nameser(nameser_in)
        return respon


def get_namser_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_namser_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception