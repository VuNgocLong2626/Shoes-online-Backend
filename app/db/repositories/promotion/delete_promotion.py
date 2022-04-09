from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionCreate
from app.db.tables import Promotion


db = SessionLocal()


def delete_promotion(id_promotion: int):
    try:
        db.query(Promotion).filter(Promotion.id_promotion == id_promotion).delete()
        db.commit()
        db.close()
        return True
    except:
        db.close()
        return None