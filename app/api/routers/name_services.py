from fastapi import APIRouter, status, HTTPException
from typing import List
from app.services.name_services import NameServicesServices
from app.models.schemas import name_services as _nameser_schemas


router = router = APIRouter(
    prefix="/name-services",
    tags=["NameServices"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_nameser_schemas.NameServicesDetail)
async def create_nameser(
    nameser_in: _nameser_schemas.NameServicesCreate
):
    respon = NameServicesServices.create_nameser(nameser_in)
    if not respon:
        raise
    return respon


@router.get("/", response_model=List[_nameser_schemas.NameServicesDetail])
async def get_all_nameser():
    respon = NameServicesServices.get_all_nameser()
    return respon


@router.delete("/{id_nameser}")
async def delete_nameser(id_nameser: int):
    _ = NameServicesServices.delete_nameser(id_nameser)
    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail="Successfull"
    )


@router.put("/")
async def update_nameser(namser_in: _nameser_schemas.NameServicesUpdate):
    respon = NameServicesServices.update_nameser(namser_in)
    return respon
