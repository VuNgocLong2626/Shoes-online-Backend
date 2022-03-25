from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate_comment import CommentRateCreate
from app.db.tables import RateProduct


db = SessionLocal()


def create_rate_comment(_in: CommentRateCreate):
    comment_new = RateProduct(**_in.dict())
    db.add(comment_new)
    try:
        db.flush()
        db.commit()
        return comment_new
    except:    
        return None