from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionCreate
from app.db.tables import Promotion


db = SessionLocal()


def get_all_promotion():
    respon = db.query(Promotion).all()
    db.close()
    return respon
