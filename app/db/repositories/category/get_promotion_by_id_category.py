from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.category import CategoryCreate
from app.db.tables import Category, Promotion

db = SessionLocal()



def get_promotion_by_id_category(id_category: int):
    db.close()
    respon = db.query(Category, Promotion.reduction).join(Promotion).filter(Category.id_category == id_category).first()
    return respon
