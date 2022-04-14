from app.models.schemas import gender as _gender_schemas
from fastapi import HTTPException, status
from app.db.repositories.gender.create_gender import create_gender
from app.db.repositories.gender.get_all_gender import get_all_gender
from app.db.repositories.gender.delete_gender import delete_gender
from app.db.repositories.gender.get_by_id_gender import get_by_id_gender
from app.db.repositories.gender.update_gender import update_gender


class GenderServices():

    def create_gender(gender_in: _gender_schemas.GenderCreate):
        respon = create_gender(gender_in)
        if respon is None:
            raise get_gender_create_exception()
        return respon

    def get_all_gender():
        respon = get_all_gender()
        return respon

    def delete_gender(id_gender: int):
        respon_gender = get_by_id_gender(id_gender)
        if respon_gender is None:
            raise get_gender_exception()
        delete_gender(id_gender)
        raise get_gender_done()

    def update_gender(gender_in: _gender_schemas.GenderUpdate):
        respon = update_gender(gender_in)
        if respon is None:
            raise get_gender_exception()
        return respon


def get_gender_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_gender_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_gender_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
