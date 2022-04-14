from fastapi import APIRouter
from typing import List
from app.services.color import ColorServices
from app.models.schemas import product_detail as _Color_schemas


router = APIRouter(
    prefix="/color",
    tags=["Color"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_Color_schemas.ColorDetail)
async def create_color(color_in: _Color_schemas.ColorCreate):
    respon = ColorServices.create_color(color_in)
    return respon


@router.get("/", response_model=List[_Color_schemas.ColorDetail])
async def get_all():
    respon = ColorServices.get_all_color()
    return respon


@router.put("/")
async def update_color(color_in: _Color_schemas.ColorUpdate):
    respon = ColorServices.update_color(color_in)
    return respon


@router.delete("/{id_color}")
async def delete_color(id_color: int):
    respon = ColorServices.delete_color(id_color)
    return respon
