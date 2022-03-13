from fastapi import APIRouter, Response, status, HTTPException
from sqlalchemy import null
from typing import List, Optional
from app.services.size import SizeServices
from app.models.schemas import product_detail as _size_schemas


router = APIRouter(
    prefix="/size",
    tags=["Size"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_size_schemas.SizeDetail)
async def create_size(size_in: _size_schemas.SizeCreate):
    respon = SizeServices.create_size(size_in)
    return respon

@router.get("/", response_model=List[_size_schemas.SizeDetail])
async def get_all():
    respon = SizeServices.get_all_size()
    return respon

@router.put("/")
async def update_size(size_in: _size_schemas.SizeUpdate):
    respon = SizeServices.update_size(size_in)
    return respon

@router.delete("/{id_color}")
async def delete_size(id_size: int):
    respon = SizeServices.delete_size(id_size)
    return respon