from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate_comment import CommentRateCreate
from app.db.tables import RateProduct, Rate, Comments


db = SessionLocal()


def get_comment_join_rate_comment(id_product: int):
    db.close()
    respon = db.query(RateProduct, Comments, Rate).join(Comments).join(Rate).filter(RateProduct.id_product == id_product).all()
    return respon