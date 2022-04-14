from pydantic import BaseModel, Field


class CategoryName(BaseModel):
    name: str = Field(alias='name')
