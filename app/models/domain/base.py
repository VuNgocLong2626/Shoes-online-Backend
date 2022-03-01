from pydantic import BaseModel, Field


class UserId(BaseModel):
    id_user: int = Field(alias='id_user')


class NameServicesId(BaseModel):
    id_name_services: int = Field(alias='id_name_services')


class ServicesId(BaseModel):
    id_services: int = Field(alias='id_services')


class BillId(BaseModel):
    id_bill: int = Field(alias='id_bill')


class Info(BaseModel):
    id_info: int = Field(alias='id_info')


class PermissionId(BaseModel):
    id_permission: int = Field(alias='id_permission')


class CommentsId(BaseModel):
    id_comments: int = Field(alias='id_comments')


class BillDetailsId(BaseModel):
    id_bill_details: int = Field(alias='id_bill_details')


class ProductId(BaseModel):
    id_product: int = Field(alias='id_product')


class CategoryId(BaseModel):
    id_category: int = Field(alias='id_category')


class PromotionId(BaseModel):
    id_promotion: int = Field(alias='id_promotion')


class GenderId(BaseModel):
    id_gender: int = Field(alias='id_gender')


class SizeId(BaseModel):
    id_size: int = Field(alias='id_size')


class ImageId(BaseModel):
    id_image: int = Field(alias='id_image')


class ColorId(BaseModel):
    id_color: int = Field(alias='id_color')


class ProductDetailsId(BaseModel):
    id_product: int = Field(alias='id_product')


class RateId(BaseModel):
    id_rate: int = Field(alias='id_rate')


class CommentsId(BaseModel):
    id_comments: int = Field(alias='id_comments')


class RateProductId(BaseModel):
    id_rate_product: int = Field(alias='id_rate_product')