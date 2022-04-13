from fastapi import APIRouter, Response, status, HTTPException
from sqlalchemy import null
from typing import List
from app.utils.statistics import test

router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def test1():
    test()
    return {"Ahihhi"}