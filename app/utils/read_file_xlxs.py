import pandas as pd
import time
from fastapi import UploadFile, File
from google_drive_downloader import GoogleDriveDownloader as gdd
import re
from app.models.schemas import (
    user as _user_schemas,
    product as _product_schemas,
    product_detail as _product_detail_schemas,
    size_quatity as _size_quatity_schemas
    )
from datetime import date
import datetime
from app.db.repositories.image.create_image import create_image
from app.db.repositories.color.create_color import create_color
from app.db.repositories.color.get_by_hex_color import get_by_hex_color
from app.db.repositories.gender.create_gender import create_gender
from app.db.repositories.gender.get_gender_by_name import get_gender_by_name
from app.db.repositories.category.get_firts_by_name_category import get_by_name_category
from app.db.repositories.category.create_name_caregory import create_name_category
from app.db.repositories.size.get_size_by_number import get_size_by_number
from app.db.repositories.size.create_size import create_size

from app.db.repositories.product.create_product import create_product
from app.db.repositories.product.get_by_name import get_by_name
from app.db.repositories.product_detail.create_produc_detail import create_product_detail
from app.db.repositories.size_quantity.create_quantity import create_size_quatity

#user: _user_schemas.UserToken ,
def read(file: UploadFile = File(None)):
    if not file.filename.endswith('.xlsx'):
        return "Not file Excel"
    df = pd.read_excel(file.file.read(), sheet_name=0)
    js = df.to_json(orient='records', lines=True)
    col = len(df.iloc[len(df)-1])
    arr = []
    for row in range(len(df)):
        db = df.iloc[row]
        category = get_by_name_category(db.values[3])
        if category is None:
            category = create_name_category(db.values[3])
            print(db.values[3])

        gender = get_gender_by_name(db.values[4])
        if gender is None:
            gender = create_gender(name=db.values[4])
        
        color = get_by_hex_color(db.values[5])
        if color is None:
            color = create_color(name=db.values[5])
        
        product_basic = get_by_name(db.values[0])
        if product_basic is None:
            product_in = _product_schemas.ProductCreateForm(**{
                "id_category": category.id_category,
                "id_gender": gender.id_gender,
                "detail": db.values[1],
                "money": str(db.values[2]),
                "name":db.values[0]
            })
            product_basic = create_product(product_in)

        product_detail_in = _product_detail_schemas.ProductDetailCreate(**{
            "id_color": color.id_color,
            "id_product": product_basic.id_product
        })
        product_detail = create_product_detail(product_detail_in)
        # create image in DB
        url_1 = dowload_load_image(str(db.values[6]))
        create_image(url_1,product_detail.id_product_detail)

        url_2 = dowload_load_image(str(db.values[7]))
        create_image(url_2,product_detail.id_product_detail)

        url_3 = dowload_load_image(str(db.values[8]))
        create_image(url_3,product_detail.id_product_detail)

        url_4 = dowload_load_image(str(db.values[9]))
        create_image(url_4,product_detail.id_product_detail)
        #Create or check size and add quantity
        for index in range(10,col):
            list_size_quantity = str(db.values[index]).split("/")
            size = get_size_by_number(list_size_quantity[1])
            if size is None:
                size = create_size(number=list_size_quantity[1])
            size_quantity_in = _size_quatity_schemas.SizeQuantityCreate(**{
                "id_size":size.id_size,
                "id_product_detail": product_detail.id_product_detail,
                "quantity_sold": 0,
                "quantity": list_size_quantity[0]
            })
            create_size_quatity(size_quantity_in)
    # print(url_1)
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

def dowload_load_image(url: str):
    chek = check_google_drive(url)
    if not chek:
        return False
    z = re.findall('(?<=id=)([^&\n]*)(?=&)?',url)

    if not z:
        z = re.findall('(\/file\/d\/)(.*?)(?:&|$)', url)[0]
    # save_file = f'media/products/{id_dong_vat}/images'
    # file_name = get_new_filename("jpg")
    # file_location = f"{save_file}/{file_name}"
    
    # gdd.download_file_from_google_drive(file_id=z[len(z)-1].replace("/view", ""),
    #                                 dest_path=file_location,
    #                                 unzip=True)
    id_image = z[len(z)-1].split("/")[0]
    link_image = f'http://drive.google.com/uc?export=view&id={id_image}'
    return link_image