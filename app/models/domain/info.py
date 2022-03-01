from pydantic import BaseModel, Field
import datetime as date


class InfoPhone(BaseModel):
    phone: str = Field(min_length=11,
                        max_length=12,
                        alias='phone')


class InfoFullName(BaseModel):
    full_name: str = Field(min_length=2,
                            max_length=250,
                            alias='full_name')


class InfoDOB(BaseModel):
    dob: date = Field(None, alias='full_name')


class InfoEmail(BaseModel):
    email: str = Field(..., alias='email')