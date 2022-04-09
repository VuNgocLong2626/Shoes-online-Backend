from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.promotion import PromotionUpdate
from app.db.tables import Promotion


db = SessionLocal()


def update_promotion(promotion_in: PromotionUpdate):
    try:
        db.query(Promotion).\
        filter(Promotion.id_promotion == promotion_in.id_promotion).\
        update({
            Promotion.name: promotion_in.name,
            Promotion.detail: promotion_in.detail,
            Promotion.reduction: promotion_in.reduction
                })
        db.commit()
        db.close()
        return promotion_in
    except:
        return None