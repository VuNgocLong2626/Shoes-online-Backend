from app.models.schemas import promotion as _promotion_schemas
from fastapi import HTTPException, status
from app.db.repositories.promotion.create_promotion import create_promotion
from app.db.repositories.promotion.get_all_promotion import get_all_promotion
from app.db.repositories.promotion.get_by_id_promotion \
    import get_by_id_promotion
from app.db.repositories.promotion.update_promotion import update_promotion
from app.db.repositories.promotion.delete_promotion import delete_promotion
from app.db.repositories.promotion.get_by_name import get_by_name


class PromotionServices():

    def create_promotion(promotion_in: _promotion_schemas.PromotionCreate):
        try:
            respon = create_promotion(promotion_in)
            if respon is None:
                raise get_promotion_create_exception()
            return respon
        except Exception:
            raise get_promotion_exception()

    def get_all_promotion():
        respon = get_all_promotion()
        return respon

    def update_promotion(prommotion_in: _promotion_schemas.PromotionUpdate):
        respon = update_promotion(prommotion_in)
        if respon is None:
            raise get_promotion_exception()
        return respon

    def delete_promotion(id_promotion: int):
        respon_promotion = get_by_id_promotion(id_promotion)
        if respon_promotion is None:
            raise get_promotion_exception()
        delete_promotion(id_promotion)
        raise get_promotion_done()

    def get_by_name(name: str):
        respon = get_by_name(name)
        return respon


def get_promotion_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_promotion_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_promotion_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
