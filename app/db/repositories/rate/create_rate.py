from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate import RateCreate
from app.db.tables import Rate


db = SessionLocal()


def create_rate(rate_in: RateCreate):
    rate_new = Rate(**rate_in.dict())
    db.add(rate_new)
    try:
        db.flush()
        db.commit()
        return rate_new
    except:    
        return None