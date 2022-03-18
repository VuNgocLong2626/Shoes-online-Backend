from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.category import CategoryCreate
from app.db.tables import Category

db = SessionLocal()



def get_by_id_category(id_category: int):
    db.close()
    respon = db.query(Category).filter(Category.id_category == id_category).first()
    return respon
