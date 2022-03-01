from pydantic import BaseModel, Field


class PromotionName(BaseModel):
    name: str = Field(alias='name')


class PromotionDetail(BaseModel):
    detail: str = Field(alias='detail')


class PromotionReduction(BaseModel):
    reduction: int = Field(alias='reduction')