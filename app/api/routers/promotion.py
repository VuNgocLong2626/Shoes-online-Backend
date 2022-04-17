from fastapi import APIRouter
from typing import Optional
from app.services.promotion import PromotionServices
from app.models.schemas import promotion as _promotion_schemas


router = APIRouter(
    prefix="/promotion",
    tags=["Promotion"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_promotion_schemas.PromotionDetail)
async def create_promotion(promotion_in: _promotion_schemas.PromotionCreate):
    respon = PromotionServices.create_promotion(promotion_in)
    return respon


@router.get("/")
async def get_all_promotion(name_promotion: Optional[str] = None):
    if name_promotion is None:
        respon = PromotionServices.get_all_promotion()
        return respon
    else:
        respon = PromotionServices.get_by_name(name_promotion)
        return respon


@router.put("/")
async def update_promotion(promotion_in: _promotion_schemas.PromotionUpdate):
    respon = PromotionServices.update_promotion(promotion_in)
    return respon


@router.delete("/{id_promotion}")
async def delete_promotion(id_promotion: int):
    respon = PromotionServices.delete_promotion(id_promotion)
    return respon


@router.delete("/update-category/{id_promotion}")
async def delete_update_category(id_promotion: int):
    respon = PromotionServices.delete_update_category(id_promotion)
    return respon


# @router.get("/")
# async def get_by_name(name_promotion: str):
#     # respon = PromotionServices.get_by_name(name_promotion)
#     return name_promotion
