from fastapi import APIRouter
from typing import List
from app.services.rate import RateServices
from app.models.schemas import rate as _rate_schemas


router = APIRouter(
    prefix="/rate",
    tags=["Rate"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_rate_schemas.RateDetail)
async def create_rate(rate_in: _rate_schemas.RateCreate):
    respon = RateServices.create_rate(rate_in)
    return respon


@router.get("/", response_model=List[_rate_schemas.RateDetail])
async def get_all_rate():
    respon = RateServices.get_all_rate()
    return respon


@router.put("/")
async def update_rate(rate_in: _rate_schemas.RateUpdate):
    respon = RateServices.update_rate(rate_in)
    return respon


@router.delete("/{id_rate}")
async def delete_rate(id_rate: int):
    respon = RateServices.delete_rate(id_rate)
    return respon


@router.get("/average-start/{id_product}")
async def average_start(id_product: int):
    respon = RateServices.get_aver_id_product(id_product)
    return respon
