from fastapi import APIRouter, Response, status, HTTPException
from sqlalchemy import null
from typing import List
from app.services.gender import GenderServices
from app.models.schemas import gender as _gender_schemas


router = APIRouter(
    prefix="/gender",
    tags=["Gender"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_gender_schemas.GenderDetail)
async def create_gender(gender_in: _gender_schemas.GenderCreate):
    respon = GenderServices.create_gender(gender_in)
    return respon

@router.get("/", response_model = List[_gender_schemas.GenderDetail])
async def get_all_gender():
    respon = GenderServices.get_all_gender()
    return respon

@router.delete("/{id_gender}")
async def delete_gender(id_gender: int):
    respon = GenderServices.delete_gender(id_gender)
    return respon

@router.put("/")
async def update_gender(gender_in: _gender_schemas.GenderUpdate):
    respon = GenderServices.update_gender(gender_in)
    return respon