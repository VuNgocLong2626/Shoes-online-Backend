from app.db.database import SessionLocal
from app.db.tables import NameServices


db = SessionLocal()


def get_all_nameser():
    nameser_all = db.query(NameServices).all()
    db.close()
    return nameser_all
