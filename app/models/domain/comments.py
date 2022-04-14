from pydantic import BaseModel, Field
from datetime import date


class CommentsContent(BaseModel):
    Content: str = Field(alias='Content')


class CommentsDate(BaseModel):
    Date: date = Field(alias='Date')
