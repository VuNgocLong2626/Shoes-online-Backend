from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate import RateCreate
from app.db.tables import Rate


db = SessionLocal()


def get_all_rate():
    db.close()
    rate_all = db.query(Rate).all()
    return rate_all