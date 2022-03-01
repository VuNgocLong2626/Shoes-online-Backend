from pydantic import BaseModel, Field
import datetime as date


class CommentsContent(BaseModel):
    content: str = Field(alias='Content')


class CommentsDate(BaseModel):
    date: date = Field(alias='Date')