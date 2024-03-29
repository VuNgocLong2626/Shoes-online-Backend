from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionCreate
from app.db.tables import Promotion


db = SessionLocal()


def get_by_name(name: str):
    respon = db.query(Promotion).filter(Promotion.name.like(f'{name}%')).all()
    db.close()
    return respon
