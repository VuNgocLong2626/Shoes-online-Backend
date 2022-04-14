from pydantic import BaseModel, Field


class UserAccount(BaseModel):
    account: str = Field(alias='account')


class UserPassword(BaseModel):
    password: str = Field(alias='password')
