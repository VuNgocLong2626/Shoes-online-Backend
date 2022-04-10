from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Category
import sqlalchemy

db = SessionLocal()


def create_name_category(name: str):
    category_new = Category(name=name,id_promotion=sqlalchemy.sql.null())
    db.add(category_new)
    try:
        db.flush()
        db.commit()
        return category_new
    except:
        db.rollback()
        return None