from typing import List
from app.models.domain import (
                                base as _base,
                                bill as _bill_domain)
from app.models.schemas.billdetail import BillDetailInDB


class BillCreate(
    _base.UserId,
    _bill_domain.BillStatus,
    _bill_domain.BillCreate,
    _bill_domain.BillTotal,
    _bill_domain.BillMethod,
    _bill_domain.BillAddress
):
    list_bill_detail: List[BillDetailInDB]


class BillDetail(
    _base.VerifierId,
    _base.BillId,
    _base.UserId,
    _bill_domain.BillStatus,
    _bill_domain.BillCreate,
    _bill_domain.BillTotal,
    _bill_domain.BillMethod,
    _bill_domain.BillAddress
):
    pass

    class Config:
        orm_mode = True


class BillUpdate(
    _base.BillId,
    _base.VerifierId,
    _bill_domain.BillStatus,
):
    pass


class BillInDB(
    _base.UserId,
    _bill_domain.BillStatus,
    _bill_domain.BillCreate,
    _bill_domain.BillTotal,
    _bill_domain.BillMethod,
    _bill_domain.BillAddress
):
    pass

class GetBill(
    _base.UserId,
    _base.BillId
):
    pass