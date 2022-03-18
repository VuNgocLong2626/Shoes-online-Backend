from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.category import CategoryCreate
from app.db.tables import Category
import sqlalchemy


db = SessionLocal()


def create_category(category_in: CategoryCreate):
    if category_in.id_promotion is None:
        category_new = Category(name=category_in.name,id_promotion=sqlalchemy.sql.null())
    else:
        category_new = Category(**category_in.dict())
    db.add(category_new)
    try:
        db.flush()
        db.commit()
        return category_new
    except:    
        return None