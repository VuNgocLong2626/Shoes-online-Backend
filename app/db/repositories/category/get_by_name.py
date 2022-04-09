from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.category import CategoryCreate
from app.db.tables import Category

db = SessionLocal()



def get_by_name_category(name: str):
    respon = db.query(Category).filter(Category.name.like(f'%{name}%')).all()
    db.close()
    return respon
