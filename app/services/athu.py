from fastapi import HTTPException, status, Depends
from typing import Optional
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.models.schemas.user import UserToken as _usertoken_schemas


SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGORITHM = "HS256"


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="user/login-form")
oauth2_bearer_admin = OAuth2PasswordBearer(tokenUrl="admin/login-form")


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(user_name: str, password: str):
    user = ""
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(
    user_in: _usertoken_schemas,
    expires_delta: Optional[timedelta] = None
):

    encode = user_in.dict()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=15)  # time
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        account: str = payload.get("account")
        id_permission: int = payload.get("id_permission")
        id_info: int = payload.get("id_info")
        id_user: int = payload.get("id_user")
        if account is None or id_permission is None or id_info is None or id_user is None:
            raise get_user_exception()
        if not id_permission == 3:
            raise get_user_exception()
        user_token = _usertoken_schemas(**{
            "account": account,
            "id_user": id_user,
            "id_permission": id_permission,
            "id_info": id_info
        })
        return user_token
    except JWTError:
        raise get_user_exception()


async def get_current_admin(token: str = Depends(oauth2_bearer_admin)):
    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        account: str = payload.get("account")
        id_permission: int = payload.get("id_permission")
        id_info: int = payload.get("id_info")
        id_user: int = payload.get("id_user")
        if account is None or id_permission is None or id_info is None or id_user is None:
            raise get_user_exception()
        if id_permission == 3:
            raise get_user_exception()
        user_token = _usertoken_schemas(**{
            "account": account,
            "id_user": id_user,
            "id_permission": id_permission,
            "id_info": id_info
        })
        return user_token
    except JWTError:
        raise get_user_exception()


def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response
