from fastapi import APIRouter
from typing import List, Optional
from app.services.file import ImageService
from app.models.schemas import product_detail as _File_schemas


router = APIRouter(
    prefix="/file",
    tags=["File"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_file_image(image_path: str):
    return ImageService.get_image(image_path)