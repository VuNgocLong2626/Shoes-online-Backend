from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionCreate
from app.db.tables import Promotion, Category


db = SessionLocal()


def get_category_by_id_promotion(id_promotion: int):
    respon = db.query(Category).join(Promotion).filter(Promotion.id_promotion == id_promotion).all()
    db.close()
    return respon
