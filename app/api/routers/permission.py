from fastapi import APIRouter, Response, status, HTTPException
from typing import List
from app.services.permission import PermissionService
from app.models.schemas import permission as _permission_schemas


router = router = APIRouter(
    prefix="/permission",
    tags=["permission"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_permission_schemas.PermissionDetail)
async def create_permission(
    permission_in: _permission_schemas.PermissionCreate,
    res: Response
):
    respon = PermissionService.create_permission(permission_in)
    if not respon:
        raise
    return respon


@router.get("/", response_model=List[_permission_schemas.PermissionDetail])
async def get_all_permission():
    respon = PermissionService.get_all_permission()
    return respon


@router.delete("/{id_permission}")
async def delete_permission(id_permission: int):
    respon = PermissionService.delete_permission(id_permission)
    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail="Successfull"
    )


@router.put("/")
async def update_permission(
    permission_in: _permission_schemas.PermissionUpdate
):
    respone = PermissionService.update_permission(permission_in)
    return respone
