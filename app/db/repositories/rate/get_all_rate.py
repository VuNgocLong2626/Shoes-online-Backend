from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate import RateCreate
from app.db.tables import Rate


db = SessionLocal()


def get_all_rate():
    rate_all = db.query(Rate).all()
    db.close()
    return rate_all