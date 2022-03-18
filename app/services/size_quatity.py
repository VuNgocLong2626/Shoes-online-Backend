from sqlalchemy import false
from app.models.schemas import (
    size_quatity as _size_quatity_schemas)
from fastapi import HTTPException, status
from app.db.repositories.size_quantity.create_quantity import create_size_quatity
from app.db.repositories.size.get_by_id_size import get_by_id_size
from app.db.repositories.size_quantity.get_all_quantity import get_all_quantity
from app.db.repositories.size_quantity.update_quantity import update_quantity


class SizeQuantityService():

    def create_size_quatity(size_quatity_in: _size_quatity_schemas.SizeQuantityCreate):
        respon = create_size_quatity(size_quatity_in)
        if respon is None:
            raise get_size_quatity_create_exception()
        return respon

    def get_all_size_quatity():
        return get_all_quantity()

    def update_size_quantity(quantity_in: _size_quatity_schemas.SizeQuantityUpdate):
        respon = update_quantity(quantity_in)
        if respon is None:
            raise get_size_quatity_exception()
        return respon
        
            


def get_size_quatity_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_size_quatity_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_size_quatity_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception