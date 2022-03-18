from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ImageCreate
from app.db.tables import Image


db = SessionLocal()


def create_image(image: str, id_product: int):
    image_in = ImageCreate(**{
        "path": image,
        "id_product_detail": id_product
        })
        
    image_new = Image(**image_in.dict())
    db.add(image_new)
    try:
        db.flush()
        db.commit()
        return image_new
    except:    
        return None