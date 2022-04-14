import os
from datetime import datetime


def write_file(
    destination_dir: str, filename: str,
    data
):
    is_exist = os.path.exists(destination_dir)
    if not is_exist:
        os.makedirs(destination_dir)
    filename = get_new_filename(filename)
    # save_to = f'{destination_dir}/{filename}'
    # with open(save_to, "wb+") as f:
    #     f.write(data)
    # return save_to


def get_file_extension(filename: str):
    return filename.split(".")[-1]


def generate_ksuid():
    kid = str(datetime.now())
    return kid


def get_new_filename(filename: str):
    ksuid = generate_ksuid()
    file_extension = get_file_extension(filename)
    return f'{ksuid}.{file_extension}'
