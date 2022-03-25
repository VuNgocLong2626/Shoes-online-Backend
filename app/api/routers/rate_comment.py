from fastapi import APIRouter
from typing import List, Optional
from app.services.rate_comment import RateCommentServices
from app.models.schemas import rate_comment as _rate_comment_schemas


router = APIRouter(
    prefix="/rate-comment",
    tags=["Rate Comment"],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=_rate_comment_schemas.CommentRateDetail)
async def create_rate_comment(_in: _rate_comment_schemas.CommentRateInDB):
    respon = RateCommentServices.create_rate_comment(_in)
    return respon

@router.get("/{id_product}")
async def get_all_comment_id_product(id_product: int):
    respon = RateCommentServices.get_comment_id_product(id_product)
    return respon

@router.put("/")
async def update_comment(comment_in: _rate_comment_schemas.CommentUpdate):
    respon = RateCommentServices.update_comment(comment_in)
    return respon