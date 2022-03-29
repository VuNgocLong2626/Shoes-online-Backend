from app.models.schemas.uesr_services import ServicesUpdate
from app.models.schemas.user import UserToken
from app.db.tables import Services
from app.db.database import SessionLocal


db = SessionLocal()


def update_services(_in: ServicesUpdate,user_in: UserToken):
    try:
        db.query(Services)\
            .filter(Services.id_services == _in.id_services)\
            .update({
                Services.status: _in.status,
                Services.id_verifier: user_in.id_user
            })
        db.commit()
        return _in
    except:
        return None