import pandas as pd
import time
from fastapi import UploadFile, File
from google_drive_downloader import GoogleDriveDownloader as gdd
import re
from app.models.schemas import user as _user_schemas
from datetime import date
import datetime
from app.db.repositories.image.create_image import create_image

#user: _user_schemas.UserToken ,
def read(file: UploadFile = File(None)):
    if not file.filename.endswith('.xlsx'):
        return "Not file Excel"
    df = pd.read_excel(file.file.read(), sheet_name=0)
    js = df.to_json(orient='records', lines=True)
    arr = []
    for row in range(len(df)):
        db = df.iloc[row]
        

    respon = {
        "row": len(df)-1,
        "col": len(df.iloc[len(df)-1]),
        "date": ""
    }
    return respon


def check_google_drive(check: str):
    if check == "nan":
        return False
    m = re.search('https?://([A-Za-z_0-9.-]+).*', check)
    if m is None:
        return False
    m = m.group(1)
    if m == 'drive.google.com':
        return True
    return False

def get_file_extension(filename: str):
    return filename.split(".")[-1]

def generate_ksuid() -> str:
    kid = str(datetime.datetime.now()).replace(" ", "")
    return kid

def get_new_filename(filename: str):
    ksuid = generate_ksuid()
    file_extension = get_file_extension(filename)
    return f'{ksuid}.{file_extension}'.replace(" ", "")

def dowload_load_image(url: str, id_dong_vat: int):
    chek = check_google_drive(url)
    if not chek:
        return False
    z = re.findall('(?<=id=)([^&\n]*)(?=&)?',url)

    if not z:
        z = re.findall('(\/file\/d\/)(.*?)(?:&|$)', url)[0]
    save_file = f'media/products/{id_dong_vat}/images'
    file_name = get_new_filename("jpg")
    file_location = f"{save_file}/{file_name}"
    
    gdd.download_file_from_google_drive(file_id=z[len(z)-1].replace("/view", ""),
                                    dest_path=file_location,
                                    unzip=True)
    return file_location