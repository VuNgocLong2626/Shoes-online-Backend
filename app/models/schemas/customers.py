# from app.models.domain import (
#     base as _base,
#     user as _user_domain)
from app.models.schemas import athu as _user_shemas


class CustomerCreate(_user_shemas.User, _user_shemas.UserInDB):
    pass


class CustomerDetail(_user_shemas.User):
    pass
