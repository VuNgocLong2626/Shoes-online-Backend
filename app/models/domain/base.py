from pydantic import BaseModel, Field
from typing import Optional


class UserId(BaseModel):
    id_user: int = Field(None, alias='id_user')


class NameServicesId(BaseModel):
    id_name_services: int = Field(None, alias='id_name_services')


class ServicesId(BaseModel):
    id_services: int = Field(alias='id_services')


class BillId(BaseModel):
    id_bill: int = Field(None, alias='id_bill')


class InfoId(BaseModel):
    id_info: int = Field(None, alias='id_info')


class PermissionId(BaseModel):
    id_permission: int = Field(None, alias='id_permission')


class CommentsId(BaseModel):
    id_comments: int = Field(alias='id_comments')


class BillDetailsId(BaseModel):
    id_bill_details: int = Field(alias='id_bill_details')


class ProductId(BaseModel):
    id_product: int = Field(alias='id_product')


class CategoryId(BaseModel):
    id_category: int = Field(None, alias='id_category')


class PromotionId(BaseModel):
    id_promotion: Optional[int] = Field(None, alias='id_promotion')


class GenderId(BaseModel):
    id_gender: int = Field(alias='id_gender')


class SizeId(BaseModel):
    id_size: int = Field(None, alias='id_size')


class ImageId(BaseModel):
    id_image: int = Field(alias='id_image')


class ColorId(BaseModel):
    id_color: int = Field(None, alias='id_color')


class ProductDetailsId(BaseModel):
    id_product_detail: int = Field(alias='id_product_detail')


class RateId(BaseModel):
    id_rate: int = Field(alias='id_rate')


# class CommentsId(BaseModel):
#     id_comments: int = Field(alias='id_comments')


class RateProductId(BaseModel):
    id_rate_product: int = Field(alias='id_rate_product')


class SizeQuantityId(BaseModel):
    id_size_quantity: int = Field(alias='id_size_quantity')


class BillDetailId(BaseModel):
    id_bill_detail: int = Field(alias='id_bill_detail')


class VerifierId(BaseModel):
    id_verifier: int = Field(None, alias='id_verifier')
