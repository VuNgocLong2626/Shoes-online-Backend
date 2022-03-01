from pydantic import BaseModel, Field


class RateStart(BaseModel):
    start: int = Field(alias='number_star')