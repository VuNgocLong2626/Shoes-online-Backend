from app.models.schemas import product_detail as _Color_schemas
from fastapi import HTTPException, status
from app.db.repositories.color.create_color import create_color
from app.db.repositories.color.get_by_id_color import get_by_id_color
from app.db.repositories.color.get_all_color import get_all_color
from app.db.repositories.color.delete_color import delete_color
from app.db.repositories.color.update_color import update_color


class ColorServices():

    def create_color(color_in: _Color_schemas.ColorCreate):
        try:
            respon = create_color(color_in)
            if respon is None:
                raise get_color_create_exception()
            return respon
        except Exception:
            raise get_color_create_exception()

    def get_all_color():
        respon = get_all_color()
        return respon

    def delete_color(id_color: int):
        respon_color = get_by_id_color(id_color)
        if respon_color is None:
            raise get_color_exception()
        delete_color(id_color)
        raise get_color_done()

    def update_color(color_in: _Color_schemas.ColorUpdate):
        respon = update_color(color_in)
        if respon is None:
            raise get_color_exception()
        return respon


def get_color_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_color_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_color_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
