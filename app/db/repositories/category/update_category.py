from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.category import CategoryUpdate
from app.db.tables import Category

db = SessionLocal()


def update_category(category_in: CategoryUpdate):
    try:
        db.query(Category)\
            .filter(Category.id_category == category_in.id_category)\
            .update({
                Category.name: category_in.name,
                Category.id_promotion: category_in.id_promotion
            })
        db.commit()
        return category_in
    except:
        return None