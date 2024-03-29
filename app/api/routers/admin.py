from fastapi import APIRouter, Depends
from app.services.admin import AdminServices
from fastapi.security import OAuth2PasswordRequestForm
from app.models.schemas import (
                                user as _admin_schemas,
                                info as _info_schemas
                                )
from app.services.athu import get_current_user, get_current_admin


router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}}
)

@router.post("/login-form")
async def login_form(form_data: OAuth2PasswordRequestForm = Depends()):
    respon = AdminServices.login_form_admin(form_data)
    return respon

@router.post("/login")
async def get_admin(admin_in: _admin_schemas.UserLogin):
    respon = AdminServices.get_admin(admin_in)
    return respon

@router.post("/create-account")
async def create_admin(admin_create: _admin_schemas.UserCreate, admin_in: dict = Depends(get_current_admin)):
    respon = AdminServices.create_admin(admin_in, admin_create)
    return respon

@router.put("/update-account-info")
async def create_admin(admin_info: _info_schemas.InfoUpdate, admin_in: dict = Depends(get_current_admin)):
    respon = AdminServices.update_admin_info(admin_in, admin_info)
    return respon

@router.get("/get-account-info")
async def create_admin(admin_in: dict = Depends(get_current_admin)):
    respon = AdminServices.get_info_admin_by_id(admin_in)
    return respon

@router.get("/")
async def get_admin(admin_in: dict = Depends(get_current_admin)):

    return admin_in

@router.get("/get-all-admin")
async def get_all_admin(admin_in: dict = Depends(get_current_admin)):
    respon = AdminServices.get_all_admin()
    return respon
