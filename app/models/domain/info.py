from pydantic import BaseModel, Field
from datetime import date


class InfoPhone(BaseModel):
    phone: str = Field(
                        None,
                        min_length=10,
                        max_length=12,
                        alias='phone')


class InfoFullName(BaseModel):
    full_name: str = Field(
                            None,
                            min_length=2,
                            max_length=250,
                            alias='full_name')


class InfoDOB(BaseModel):
    dob: date = Field(None, alias='dob')


class InfoEmail(BaseModel):
    email: str = Field(None, alias='email')