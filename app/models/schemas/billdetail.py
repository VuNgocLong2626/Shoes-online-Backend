from app.models.domain import (
                                base as _base,
                                bill_detail as _bill_detail_domain)


class BillDetailCreate(
    _base.BillId,
    _base.ProductId,
    _bill_detail_domain.BillDetailQuantity,
    _bill_detail_domain.BillDetailCurrentPrice,
    _bill_detail_domain.BillDetailIdProductDetail,
    _bill_detail_domain.BillDetailIdSizeQuantity    
):
    pass


class BillDetailDetail(
    _base.BillDetailId,
    _base.BillId,
    _base.ProductId,
    _bill_detail_domain.BillDetailQuantity,
    _bill_detail_domain.BillDetailCurrentPrice,
    _bill_detail_domain.BillDetailIdProductDetail,
    _bill_detail_domain.BillDetailIdSizeQuantity    
):

    class Config:
        orm_mode = True


class BillDetailUpdate(
    _base.BillDetailId,
    _base.BillId,
    _base.ProductId,
    _bill_detail_domain.BillDetailQuantity,
    _bill_detail_domain.BillDetailCurrentPrice,
    _bill_detail_domain.BillDetailIdProductDetail,
    _bill_detail_domain.BillDetailIdSizeQuantity    
):
    pass


class BillDetailInDB(
    _base.ProductId,
    _bill_detail_domain.BillDetailQuantity,
    _bill_detail_domain.BillDetailCurrentPrice,
    _bill_detail_domain.BillDetailIdProductDetail,
    _bill_detail_domain.BillDetailIdSizeQuantity    
):
    pass