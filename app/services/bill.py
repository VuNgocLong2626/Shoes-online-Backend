from app.models.schemas import (
    bill as _bill_schemas,
    billdetail as _bill_detail_schemas,
    user as _user_schemas,
    size_quatity as _size_quatity_schemas)
from fastapi import HTTPException, status
from typing import Optional
from app.db.repositories.bill.create_bill import create_bill
from app.db.repositories.bill.get_by_id_user import get_by_id_user
from app.db.repositories.bill.get_by_id_user_and_bill \
    import get_by_id_user_and_bill
from app.db.repositories.bill.update_bill import update_bill
from app.db.repositories.bill.get_bil_all import get_bill_all
from app.db.repositories.bill.get_bill_id_bill import get_by_id_bill


from app.db.repositories.bill_detail.create_bill_detail \
    import create_bill_detail
from app.db.repositories.bill_detail.get_bill_detail_by_id_bill \
    import get_bill_detail_by_id_bill

from app.db.repositories.product_detail.get_all_john_image \
    import get_all_john_image
from app.db.repositories.size_quantity.get_quantity_by_id_size_quantity \
    import get_quantity_by_id_size_quantity
from app.db.repositories.permission.get_by_id_permission \
    import get_by_id_permission
from app.db.repositories.size_quantity.update_quantity_buy \
    import update_quantity_buy
from app.db.repositories.product.get_by_id_product \
    import get_by_id_product


class BillServices():

    def create_bill(bill_in: _bill_schemas.BillCreate):
        bill = _bill_schemas.BillInDB(**bill_in.dict())
        bill_respon = create_bill(bill)
        if bill_respon is None:
            raise get_bill_create_exception()

        bill_details = bill_in.list_bill_detail
        for detail in bill_details:

            size_quantity = get_quantity_by_id_size_quantity(
                detail.id_size_quantity
            ).SizeQuantity
            quantity = size_quantity.quantity - detail.quantily
            quantity_sold = size_quantity.quantity_sold + detail.quantily
            size_quantity_in = _size_quatity_schemas.\
                SizeQuantityUpdateQuantity(**{
                    "id_size_quantity": detail.id_size_quantity,
                    "quantity_sold": quantity_sold,
                    "quantity": quantity
                })
            update_quantity_buy(size_quantity_in)

            bill_detail = {**detail.__dict__}
            bill_detail.update({"id_bill": bill_respon.id_bill})
            bill_detail_in = _bill_detail_schemas.BillDetailCreate(
                **bill_detail)
            _ = create_bill_detail(bill_detail_in)

        return bill_respon

    def get_bill(
        user_in: _user_schemas.UserToken,
        id_bill: Optional[int] = None
    ):
        if id_bill is None:
            bill_all = get_by_id_user(user_in.id_user)
            return bill_all
        bill = get_by_id_user_and_bill(user_in.id_user, id_bill)
        if bill is None:
            raise get_bill_exception()

        list_bill_detail = []
        bill_details = get_bill_detail_by_id_bill(bill.id_bill)
        for detail in bill_details:
            respon_detail = {
                "current_price": detail.current_price,
                "quantily": detail.quantily,
                "id_product": detail.id_product,
            }
            # print()
            image_color = get_first_image_by_id_product(
                detail.id_product_detail)
            size = get_quantity_by_id_size_quantity(detail.id_size_quantity)
            product = get_by_id_product(detail.id_product)
            respon_detail.update({
                "path": image_color.Image.path,
                "hex": image_color.Color.hex,
                "size": size.Size.size_number,
                "name": product.name
            })
            list_bill_detail.append(respon_detail)

        respon = {**bill.__dict__}
        respon.update({"list_product_details": list_bill_detail})
        return respon

    def update_bill(
        user_in: _user_schemas.UserToken,
        bill_in: _bill_schemas.BillUpdate
    ):
        respon_permission = get_by_id_permission(user_in.id_permission)
        if respon_permission.name == "KhachHang":
            raise get_bill_exception()

        respon = update_bill(bill_in)
        if respon is None:
            raise get_bill_exception()
        return respon

    def get_bill_all(id_bill: Optional[int] = None):
        if id_bill is None:
            bill_all = get_bill_all()
            return bill_all
        bill = get_by_id_bill(id_bill)
        if bill is None:
            raise get_bill_exception()

        list_bill_detail = []
        bill_details = get_bill_detail_by_id_bill(bill.id_bill)
        for detail in bill_details:
            respon_detail = {
                "current_price": detail.current_price,
                "quantily": detail.quantily,
                "id_product": detail.id_product,
            }
            # print()
            image_color = get_first_image_by_id_product(
                detail.id_product_detail)
            size = get_quantity_by_id_size_quantity(detail.id_size_quantity)
            product = get_by_id_product(detail.id_product)
            respon_detail.update({
                "path": image_color.Image.path,
                "hex": image_color.Color.hex,
                "size": size.Size.size_number,
                "name": product.name
            })
            list_bill_detail.append(respon_detail)

        respon = {**bill.__dict__}
        respon.update({"list_product_details": list_bill_detail})
        return respon


def get_first_image_by_id_product(id_product_detail: int):
    respon = get_all_john_image(id_product_detail)
    return respon


def get_bill_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_bill_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_bill_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
