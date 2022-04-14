from app.models.schemas import product_detail as _Size_schemas
from fastapi import HTTPException, status
from app.db.repositories.size.create_size import create_size
from app.db.repositories.size.get_by_id_size import get_by_id_size
from app.db.repositories.size.get_all_size import get_all_size
from app.db.repositories.size.delete_size import delete_size
from app.db.repositories.size.update_size import update_size


class SizeServices():

    def create_size(size_in: _Size_schemas.SizeCreate):
        # try:
        respon = create_size(size_in)
        if respon is None:
            raise get_size_create_exception()
        return respon
        # except:
        #     raise get_size_exception()

    def get_all_size():
        respon = get_all_size()
        return respon

    def delete_size(id_size: int):
        respon_size = get_by_id_size(id_size)
        if respon_size is None:
            raise get_size_exception
        delete_size(id_size)
        raise get_size_done()

    def update_size(size_in: _Size_schemas.ColorUpdate):
        respon = update_size(size_in)
        if respon is None:
            raise get_size_exception()
        return respon


def get_size_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_size_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_size_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
