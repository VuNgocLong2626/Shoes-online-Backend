from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.category import CategoryCreate
from app.db.tables import Category


db = SessionLocal()


def get_all_category():
    category_all = db.query(Category).all()
    db.close()
    return category_all