from sqlalchemy import false
from app.models.schemas import rate as _rate_schemas
from fastapi import HTTPException, status
from app.db.repositories.rate.create_rate import create_rate
from app.db.repositories.rate.delete_rate import delete_rate
from app.db.repositories.rate.update_rate import update_rate
from app.db.repositories.rate.get_all_rate import get_all_rate


class RateServices():

    def create_rate(rate_in: _rate_schemas.RateCreate):
        respon = create_rate(rate_in)
        if respon is None:
            raise get_rate_create_exception()
        return respon

    def update_rate(rate_in: _rate_schemas.RateUpdate):
        respon = update_rate(rate_in)
        if respon is None:
            raise get_rate_exception()
        return respon

    def delete_rate(id_rate: int):
        try:
            respon = delete_rate(id_rate)
            raise get_rate_done()
        except:
            raise get_rate_exception()

    def get_all_rate():
        respon = get_all_rate()
        return respon


def get_rate_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_rate_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_rate_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception