from fastapi import APIRouter, Depends
from app.services.user import UserServices
from app.models.schemas import (
                                user as _user_schemas,
                                info as _info_schemas
                                )
from app.services.athu import get_current_user


router = router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}}
)


@router.post("/log_in")
async def get_user(user_in: _user_schemas.UserLogin):
    respon = UserServices.get_user(user_in)
    return respon

@router.post("/sgin_up")
async def create_user(user_in: _user_schemas.UserCreate):
    respon = UserServices.create_user(user_in)
    return respon

@router.get("/")
async def get_token(user: dict = Depends(get_current_user)):
    return user

@router.get("/info_user/", response_model=_info_schemas.InfoDetail)
async def get_info_user(user: dict = Depends(get_current_user)):
    respon = UserServices.get_info_user(user)
    return respon

@router.put("/info_user/")
async def update_info_user(info_in: _info_schemas.InfoUpdate, user: dict = Depends(get_current_user)):
    respon = UserServices.update_info_user(user,info_in)
    return respon

@router.put("/change_password/")
def update_password(passw: _user_schemas.UserChangePassword, user: dict = Depends(get_current_user)):
    respon = UserServices.update_password(user, passw)
    return respon