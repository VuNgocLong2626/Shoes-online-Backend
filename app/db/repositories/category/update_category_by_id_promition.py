from app.db.database import SessionLocal
from app.db.tables import Category
from sqlalchemy import sql

db = SessionLocal()


def update_category_by_id_promition(id_promotion: int):
    try:
        db.query(Category)\
            .filter(Category.id_promotion == id_promotion)\
            .update({
                Category.id_promotion: sql.null()
            })
        db.commit()
        db.close()
        return id_promotion
    except Exception:
        return None
