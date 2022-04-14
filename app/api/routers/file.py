from fastapi import APIRouter, Request, UploadFile, File
from app.services.file import ImageService
from app.utils.read_file_xlxs import read


router = APIRouter(
    prefix="/file",
    tags=["File"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_file_image(image_path: str):
    respon = ImageService.get_image(image_path)
    print(respon)
    return respon


@router.get("/kkkkkkkkk")
async def get_file_image_kkkk(image_path: str, request: Request):
    return request.url._url.replace("kkkkkkkkk", "")


@router.post("/read")
async def create_file_image(_in: UploadFile = File(None)):
    respon = read(_in)
    return respon
