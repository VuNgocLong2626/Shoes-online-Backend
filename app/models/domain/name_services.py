from pydantic import BaseModel, Field


class NameServicesName(BaseModel):
    name: str = Field(
                    None,
                    min_length=2,
                    max_length=250,
                    alias='name')


class NameServicesDetail(BaseModel):
    detail: str = Field(
                        None,
                        min_length=2,
                        max_length=250,
                        alias='detail')