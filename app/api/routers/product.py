from fastapi import APIRouter, UploadFile, Form
from sqlalchemy import null
from typing import List, Optional
from app.services.product import ProductServices
from app.services.size_quatity import SizeQuantityService
from app.models.schemas import (
    product as _product_schemas,
    size_quatity as _size_quatity_schemas
)


router = APIRouter(
    prefix="/product",
    tags=["Product"],
    responses={404: {"description": "Not found"}}
)

@router.post("/")       
async def create_product(product_in: _product_schemas.ProductCreate):
    # respon = ProductServices.create_product()
    return product_in

@router.post("/create-product-basic", response_model=_product_schemas.ProductDetailForm)
async def create_product_basic(product_in: _product_schemas.ProductCreateForm):
    respon = ProductServices.create_product_basic(product_in)
    return respon

@router.get("/all-product-basic", response_model=List[_product_schemas.ProductDetailForm])
async def get_all_product_basic():
    respon = ProductServices.get_all_product_basic()
    return respon

@router.put("/update-product-basic")
async def update_product_basic(product_in: _product_schemas.ProductUpdateForm):
    respon = ProductServices.update_product_basic(product_in)
    return respon

@router.post("/create-product-detail")
async def create_produc_deatil(
    id_product: int,
    id_color: int ,
    file: List[UploadFile] 
):
    respon = ProductServices.create_produc_detail(id_product, id_color, file)
    return respon

@router.get("/all-product-detail")
async def get_all_product_detail():
    respon = ProductServices.get_all_product_detail()
    return respon

# deficient upate product detail

@router.post("/create-size-quantity", response_model=_size_quatity_schemas.SizeQuantityDetail)
async def create_size_quantity(size_quatity_in: _size_quatity_schemas.SizeQuantityCreate):
    respon = SizeQuantityService.create_size_quatity(size_quatity_in)
    return respon

@router.get("/all-size-quantity")
async def get_size_quantity():
    return SizeQuantityService.get_all_size_quatity()

@router.put("/update-size-quantity")
async def update_size_quantity(quantity_in: _size_quatity_schemas.SizeQuantityDetail):
    respon = SizeQuantityService.update_size_quantity(quantity_in)
    return respon

@router.get("/all-product")
async def get_all_product(id_gender: Optional[int] = None):
    respon = ProductServices.get_all_product(id_gender)
    return respon

@router.post("/filter-product")
async def get_filter_product(filter_in: _product_schemas.ProductFillter):
    respon = ProductServices.get_filter_product(filter_in)
    return respon

@router.get("/test/")
async def get(id: int):
    respon = ProductServices.test(id)
    return respon