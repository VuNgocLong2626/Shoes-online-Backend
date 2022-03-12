from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionCreate
from app.db.tables import Promotion


db = SessionLocal()


def get_all_promotion():
    db.commit()
    respon = db.query(Promotion).all()
    return respon
