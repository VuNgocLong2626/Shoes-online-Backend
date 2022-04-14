from fastapi import APIRouter
from typing import List, Optional
from app.services.category import CategoryServices
from app.models.schemas import category as _category_schemas


router = APIRouter(
    prefix="/category",
    tags=["Category"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_category_schemas.CategoryDetail)
async def create_category(category_in: _category_schemas.CategoryCreate):
    respon = CategoryServices.create_category(category_in)
    return respon


@router.get("/", response_model=List[_category_schemas.CategoryDetail])
async def get_all(name_category: Optional[str] = None):
    if name_category is None:
        respon = CategoryServices.get_all_category()
        return respon
    else:
        respon = CategoryServices.get_by_name(name_category)
        return respon


@router.put("/")
async def update_category(category_in: _category_schemas.CategoryUpdate):
    respon = CategoryServices.update_category(category_in)
    return respon


@router.delete("/{id_category}")
async def delete_category(id_category: int):
    respon = CategoryServices.delete_category(id_category)
    return respon
