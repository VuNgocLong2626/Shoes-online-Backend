from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionCreate
from app.db.tables import Promotion


db = SessionLocal()


def create_promotion(promotion_in: PromotionCreate):
    promotion_new = Promotion(**promotion_in.dict())
    db.add(promotion_new)
    try:
        db.flush()
        db.commit()
        return promotion_new
    except:    
        return None