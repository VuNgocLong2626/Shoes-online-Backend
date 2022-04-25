from fastapi import APIRouter, Depends
from app.services.services import ServicesServices
from app.models.schemas import uesr_services as _user_services_schemas
from app.services.athu import get_current_admin, get_current_user
from typing import Optional


router = APIRouter(
    prefix="/services",
    tags=["Services"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_user_services_schemas.UserServiecesDetail)
async def create_services(_in: _user_services_schemas.ServicesInDB):
    respon = ServicesServices.create_services(_in)
    return respon


@router.get("/{id_user}")
async def get_id_user(id_user: int):
    respon = ServicesServices.get_id_user(id_user)
    return respon


@router.get("/get-unconfimred-all/")
async def get_unconfimred_all():
    respon = ServicesServices.get_unconfimred_all()
    return respon


@router.get("/get-confimred-all/")
async def get_confimred_all():
    respon = ServicesServices.get_confimred_all()
    return respon


@router.get("/get-all-by-condition/")
async def get_all_by_condition(condition: int):
    respon = ServicesServices.get_all_by_condition(condition)
    return respon


@router.put("/", response_model=_user_services_schemas.ServicesUpdate)
async def update_services(
    _in: _user_services_schemas.ServicesUpdate,
    user_in: dict = Depends(get_current_admin)
):
    respon = ServicesServices.update_services(_in, user_in)
    return respon


@router.get("/get-all-service-user/")
async def get_all_service_user(
    user_in: dict = Depends(get_current_user)
):
    respon = ServicesServices.get_all_re(user_in)
    return respon
