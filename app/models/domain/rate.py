from pydantic import BaseModel, Field


class RateStart(BaseModel):
    number_star: int = Field(alias='number_star')