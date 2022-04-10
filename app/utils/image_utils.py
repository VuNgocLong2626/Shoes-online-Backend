from fastapi import UploadFile
import os
from app.utils import (
    file_utils as _file_utils,
)
import shutil
from ksuid import ksuid
from datetime import datetime


def create_product_image(
    product_id: int, file: UploadFile,
    image_order: int
):
    # destination_dir = f'media/products/{product_id}/images'
    # image_path = _file_utils.write_file(
    #     destination_dir, file.filename,
    #     file.file.read()
    # )

    save_file = f'media/products/{product_id}/images'
    is_exist = os.path.exists(save_file)
    if not is_exist:
        os.makedirs(save_file)
    file_name = get_new_filename(file.filename)
    file_location = f"{save_file}/{file_name}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj (file.file, file_object)
    return file_location

def delete_product_image(
    product_id: int
):
    save_file = f'media/products/{product_id}/images'
    shutil.rmtree(save_file)


def get_file_extension(filename: str):
    return filename.split(".")[-1]

def generate_ksuid() -> str:
    kid = str(datetime.now()).replace(" ", "")
    return kid

def get_new_filename(filename: str):
    ksuid = generate_ksuid()
    file_extension = get_file_extension(filename)
    return f'{ksuid}.{file_extension}'.replace(" ", "")