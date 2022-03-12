from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionCreate
from app.db.tables import Promotion


db = SessionLocal()


def get_by_id_promotion(id_promotion: int):
    db.commit()
    respon = db.query(Promotion).filter(Promotion.id_promotion == id_promotion).first()
    return respon
