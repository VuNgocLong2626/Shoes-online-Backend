from app.models.schemas import category as _category_schemas
from fastapi import HTTPException, status
from app.db.repositories.category.create_category import create_category
from app.db.repositories.category.get_all_category import get_all_category
from app.db.repositories.category.get_by_id_category import get_by_id_category
from app.db.repositories.category.delete_category import delete_category
from app.db.repositories.category.update_category import update_category
from app.db.repositories.category.get_by_name import get_by_name_category
from app.db.repositories.promotion.get_by_id_promotion \
    import get_by_id_promotion


class CategoryServices():

    def create_category(category_in: _category_schemas.CategoryCreate):
        respon = create_category(category_in)
        if respon is None:
            raise get_category_create_exception()
        return respon

    def get_all_category():
        all_category = get_all_category()
        respon = []
        for category in all_category:
            _category = {**category.__dict__}
            id_promotion = _category.get("id_promotion")
            if id_promotion:
                _promotion = get_by_id_promotion(id_promotion)
                _category.update({"name_promotion": _promotion.name})
                respon.append(_category)
            else:
                _category.update({"name_promotion": "null"})
                respon.append(_category)
        return respon

    def delete_category(id_category: int):
        respon_category = get_by_id_category(id_category)
        if respon_category is None:
            raise get_category_exception()
        delete_category(id_category)
        raise get_category_done()

    def update_category(category_in: _category_schemas.CategoryUpdate):
        respon = update_category(category_in)
        if respon is None:
            raise get_category_exception()
        return respon

    def get_by_name(name: str):
        all_category = get_by_name_category(name)
        respon = []
        for category in all_category:
            _category = {**category.__dict__}
            id_promotion = _category.get("id_promotion")
            if id_promotion:
                _promotion = get_by_id_promotion(id_promotion)
                _category.update({"name_promotion": _promotion.name})
                respon.append(_category)
            else:
                _category.update({"name_promotion": "null"})
                respon.append(_category)
        return respon


def get_category_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_category_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_category_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
