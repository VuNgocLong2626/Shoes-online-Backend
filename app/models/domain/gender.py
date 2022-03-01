from pydantic import BaseModel, Field


class GenderName(BaseModel):
    name: str = Field(alias='name')