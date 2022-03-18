from fastapi import HTTPException
from fastapi.responses import FileResponse
import os


class ImageService():

    def get_image(image_path: str) -> FileResponse:
        if os.path.exists(image_path):
            return FileResponse(image_path, media_type="image/jpeg")
        return HTTPException(
            status_code=404, detail="File not found!"
        )