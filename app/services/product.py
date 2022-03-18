from sqlalchemy import false
from app.models.schemas import (
    product_detail as _product_detail_schemas,
    product as _product_schemas)
from fastapi import HTTPException, status, UploadFile
from typing import List
from app.utils import (
    file_utils as _file_utils,
    image_utils as _image_utils
)
from app.db.repositories.product.create_product import create_product
from app.db.repositories.product.get_all_product_basic import get_all_product_basic
from app.db.repositories.product.update_product import update_product_basic
from app.db.repositories.product.get_by_name import get_by_name
from app.db.repositories.product_detail.create_produc_detail import create_product_detail
from app.db.repositories.product_detail.get_all_product_detail import get_all_product_detail
from app.db.repositories.image.create_image import create_image
from app.db.repositories.image.get_image_by_id_product import get_image_by_id_product




class ProductServices():

    def create_product():
        return "ahihih"

    def create_product_basic(product_new: _product_schemas.ProductCreateForm):
        respon = create_product(product_new)
        if respon is None:
            raise get_product_exception()
        
        return respon
        
    def get_all_product_basic():
        respon = get_all_product_basic()
        return respon

    def update_product_basic(product: _product_schemas.ProductUpdateForm):

        product_name = get_by_name(product.id_product)
        if product_name is None:
            raise get_product_exception()

        respon = update_product_basic(product)
        if respon is None:
            raise get_product_exception()
        
        return respon
 
    def create_produc_detail(    
        id_product: int,
        id_color: int,
        files: List[UploadFile]):

        product_detail = _product_detail_schemas.ProductDetailCreate(**{
            "id_color": id_color,
            "id_product": id_product
        })

        respon_product_detail = create_product_detail(product_detail)
        if respon_product_detail is None:
            raise get_product_exception()

        image_responses = []
        for index, file in enumerate(files, start=1):
            image_db = _image_utils.create_product_image(
                id_product, file,
                index
            )
            image_responses.append(image_db)
            create_image(image_db, respon_product_detail.id_product_detail)

        return respon_product_detail

    def get_all_product_detail():
        respon_product_details = get_all_product_detail()
        respon = []
        for product_detail in respon_product_details:
            respon_image = get_image_by_id_product(product_detail.id_product_detail)
            detail = _product_detail_schemas.ProductDetailAll(**{
                "id_product_detail": product_detail.id_product_detail,
                "id_color": product_detail.id_color,
                "id_product": product_detail.id_product,
                "list_image": respon_image
            })
            respon.append(detail)

        return respon




def get_product_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_product_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception