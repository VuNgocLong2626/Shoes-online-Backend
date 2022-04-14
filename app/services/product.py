
from app.models.schemas import (
    product_detail as _product_detail_schemas,
    product as _product_schemas)
from fastapi import HTTPException, status, UploadFile
from typing import List, Optional
from app.utils import image_utils as _image_utils
from app.db.repositories.product.create_product import create_product
from app.db.repositories.product.get_all_product_basic import \
    get_all_product_basic
from app.db.repositories.product.update_product import update_product_basic
from app.db.repositories.product.get_by_name import get_by_name
from app.db.repositories.product_detail.create_produc_detail import \
    create_product_detail
from app.db.repositories.product_detail.get_all_product_detail import \
    get_all_product_detail
from app.db.repositories.image.create_image import create_image
from app.db.repositories.image.get_image_by_id_product import \
    get_image_by_id_product
from app.db.repositories.color.get_by_id_color import \
    get_by_id_color
from app.db.repositories.product_detail.get_by_id_product_detail import \
    get_by_id_product_detail
from app.db.repositories.size_quantity.get_quantity_by_id_product_detail\
    import get_quantity_by_id_product_detail
from app.db.repositories.category.get_promotion_by_id_category import \
    get_promotion_by_id_category
from app.db.repositories.product.get_by_in_id_category import \
    get_by_in_id_category
from app.db.repositories.product.get_by_in_id_color import get_by_in_id_color
from app.db.repositories.product.get_by_in_id_category_and_color import \
    get_by_in_id_category_and_color
from app.db.repositories.product.get_product_by_name import get_product_by_name
from app.db.repositories.product_detail.update_product_detail import \
    update_product_detail
from app.db.repositories.image.delete_all_image import delete_all_image
from app.db.repositories.product.get_by_id_product import get_by_id_product
from app.db.repositories.promotion.get_category_by_id_promotion import \
    get_category_by_id_promotion
from app.db.repositories.product.get_by_list_id_category import \
    get_by_list_id_category
from app.db.repositories.product.get_by_in_id_color_and_gender import \
    get_by_in_id_color_and_gender
from app.db.repositories.product.get_by_in_id_category_and_gender import \
    get_by_in_id_category_and_gender
from app.db.repositories.product.get_by_in_id_category_and_color_and_gender \
    import get_by_in_id_category_and_color_and_gender
from app.db.repositories.product.get_product_by_id_poduct_and_detail import \
    get_product_by_id_poduct_and_detail
from app.db.repositories.product_detail.get_first_by_id_product import \
    get_first_by_id_product
from app.db.repositories.size_quantity.get_first_size_by_id_product import \
    get_first_size_by_id_product


class ProductServices():

    def create_product():
        return "ahihih"

    def create_product_basic(product_new: _product_schemas.ProductCreateForm):
        respon = create_product(product_new)
        # if respon is None:
        #     raise get_product_create_exception()

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
            raise get_product_create_exception()

        image_responses = []
        for index, file in enumerate(files, start=1):
            image_db = _image_utils.create_product_image(
                id_product, file,
                index
            )
            image_responses.append(image_db)
            image_in = f'http://127.0.0.1:8000/file/?image_path={image_db}'
            # print(image_in)
            create_image(image_in, respon_product_detail.id_product_detail)

        return respon_product_detail

    def update_produc_detail(
        id_product_detail: int,
        id_product: int,
        id_color: int,
        files: List[UploadFile]
    ):
        product_detail = _product_detail_schemas.ProductDetailUpdate(**{
            "id_product_detail": id_product_detail,
            "id_color": id_color,
            "id_product": id_product
        })

        respon_product_detail = update_product_detail(product_detail)
        if respon_product_detail is None:
            raise get_product_create_exception()
        _image_utils.delete_product_image(id_product)
        delete_all_image(id_product_detail)

        image_responses = []
        for index, file in enumerate(files, start=1):
            image_db = _image_utils.create_product_image(
                id_product, file,
                index
            )
            image_responses.append(image_db)
            image_in = f'http://127.0.0.1:8000/file/?image_path={image_db}'
            # print(image_in)
            create_image(image_in, respon_product_detail.id_product_detail)

        return respon_product_detail

    def get_all_product_detail():
        respon_product_details = get_all_product_detail()
        respon = []
        for product_detail in respon_product_details:
            respon_image = get_image_by_id_product(
                product_detail.id_product_detail)
            detail = _product_detail_schemas.ProductDetailAll(**{
                "id_product_detail": product_detail.id_product_detail,
                "id_color": product_detail.id_color,
                "id_product": product_detail.id_product,
                "list_image": respon_image
            })
            respon.append(detail)

        return respon

    def get_all_product(id_gender: Optional[int] = None):
        product_all = get_all_product_basic(id_gender)
        respon = get_all_main(product_all)
        return respon

    def get_all_product_user(id_gender: Optional[int] = None):
        product_all = get_all_product_basic(id_gender)
        respon = get_all_main_user(product_all)
        return respon

    def get_filter_product(fillter_in: _product_schemas.ProductFillter):
        if fillter_in.id_gender == 0:
            if fillter_in.list_id_category is not None:
                # Not Done
                if (fillter_in.list_id_color is None):
                    product_all = get_by_in_id_category(
                        fillter_in.list_id_category)
                    respon_not_color = get_all_main(product_all)
                    return respon_not_color
                product_all = get_by_in_id_category_and_color(
                    fillter_in.list_id_category, fillter_in.list_id_color)
                respon = get_all_main(product_all)
                return respon
            product_all = get_by_in_id_color(fillter_in.list_id_color)
            respon_not_category = get_all_main(product_all)
            return respon_not_category
        else:
            if fillter_in.list_id_category is not None:
                if fillter_in.list_id_color is None:
                    product_all = get_by_in_id_category_and_gender(
                        fillter_in.list_id_category, fillter_in.id_gender)
                    respon_not_color = get_all_main(product_all)
                    return respon_not_color
                product_all = get_by_in_id_category_and_color_and_gender(
                    fillter_in.list_id_category,
                    fillter_in.list_id_color,
                    fillter_in.id_gender)
                respon = get_all_main(product_all)
                return respon
            product_all = get_by_in_id_color_and_gender(
                fillter_in.list_id_color, fillter_in.id_gender)
            respon_not_category = get_all_main(product_all)
            return respon_not_category

    def get_id_product(id_product: int):
        product_in = []
        product = get_by_id_product(id_product)
        product_in.append(product)
        respon = get_all_main(product_in)
        return respon[0]

    def search_product_by_name(name: str):
        product_all = get_product_by_name(name)
        respon = get_all_main(product_all)
        return respon

    def get_all_product_by_id_promotion(id: int):
        respon = get_category_by_id_promotion(id)
        list_id_category = []
        for category in respon:
            list_id_category.append(category.id_category)
        product_all = get_by_list_id_category(list_id_category)
        respon = get_all_main(product_all)
        return respon

    def get_product_cart(produc_in: List[_product_schemas.ProductCart]):
        respon = []
        for product in produc_in:
            result = get_product_by_id_poduct_and_detail(product)
            respon.append(result)
        return respon


def get_list_by_id_product_detail(id_product: int):
    detail_all = get_by_id_product_detail(id_product)
    respon = []
    for detail in detail_all:
        detail = {**detail.__dict__}
        list_image = get_list_path_by_id_product_detail(
            detail.get("id_product_detail"))
        detail.update({"list_image": list_image})
        list_size = get_quantity_by_id_product_detail(
            detail.get("id_product_detail"))
        detail.update({"list_size": list_size})
        hex = get_hex_color_by_id_color(detail.get("id_color"))
        detail.update({"hex": hex})
        respon.append(detail)
    return respon


def get_list_path_by_id_product_detail(id_product_detail: int):
    list_image = get_image_by_id_product(id_product_detail)
    list_path = []
    for image in list_image:
        list_path.append(image.path)
    return list_path


def get_discount(id_category: int):
    respon = get_promotion_by_id_category(id_category)
    return respon


def get_all_main(product_all, list_id_color: Optional[List[int]] = None):
    respon = []
    for products in product_all:
        product = {**products.__dict__}
        reduction = get_discount(products.id_category)
        if reduction is None:
            reduction = 0
        else:
            reduction = reduction.reduction

        discount = products.money * (1 - reduction/100)
        product.update({"discount": discount})
        product.update({"reduction": reduction})
        product_detail = get_list_by_id_product_detail(
            product.get("id_product"))
        product.update({"list_color": product_detail})
        respon.append(product)
    return respon


def get_all_main_user(product_all, list_id_color: Optional[List[int]] = None):
    respon = []
    for products in product_all:
        product = {**products.__dict__}

        check_product = get_first_by_id_product(product.get("id_product"))
        if check_product is None:
            continue
        check_size = get_first_size_by_id_product(
            check_product.id_product_detail)
        if check_size is None:
            continue

        reduction = get_discount(products.id_category)
        if reduction is None:
            reduction = 0
        else:
            reduction = reduction.reduction

        product_detail = get_list_by_id_product_detail(
            product.get("id_product"))
        discount = products.money * (1 - reduction/100)
        product.update({"discount": discount})
        product.update({"reduction": reduction})
        product.update({"list_color": product_detail})
        respon.append(product)
    return respon
# def get


def get_hex_color_by_id_color(id_color: int):
    color = get_by_id_color(id_color).hex
    return color


def get_product_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_product_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_product_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
