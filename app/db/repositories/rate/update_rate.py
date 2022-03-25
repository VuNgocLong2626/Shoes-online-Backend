from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate import RateUpdate
from app.db.tables import Rate


db = SessionLocal()


def update_rate(rate_in: RateUpdate):
    try:
        db.query(Rate)\
            .filter(Rate.id_rate == rate_in.id_rate)\
            .update({Rate.number_star: rate_in.number_star})
        db.commit()

        return rate_in
    except:
        return None