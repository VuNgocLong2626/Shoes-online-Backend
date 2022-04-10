from fastapi import APIRouter, Depends
from sqlalchemy import null
from typing import List, Optional
from app.services.bill import BillServices
from app.models.schemas import bill as _bill_schemas
from app.services.athu import get_current_user, get_current_admin
from app.db.repositories.bill.get_count_bill import get_count_bill


router = APIRouter(
    prefix="/bill",
    tags=["Bill"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_bill_schemas.BillDetail)
async def create_bill(bill_in: _bill_schemas.BillCreate):
    respon = BillServices.create_bill(bill_in)
    return respon

@router.get("/get-bill/")
async def get_bill(user_in: dict = Depends(get_current_user), id_bill: Optional[int]=None):
    respon = BillServices.get_bill(user_in, id_bill)
    return respon

@router.get("/admin-get-bill/")
async def get_bill(user_in: dict = Depends(get_current_admin), id_bill: Optional[int]=None):
    respon = BillServices.get_bill_all(id_bill)
    return respon

@router.put("/")
async def update_bill(bill_in: _bill_schemas.BillUpdate, user_in: dict = Depends(get_current_admin)):
    respon = BillServices.update_bill(user_in, bill_in)
    return respon

@router.get("/get-count-bill/")
async def get_count_bil():
    respon = get_count_bill() + 1
    return respon