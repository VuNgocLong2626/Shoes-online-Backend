import requests
from tabnanny import check
from fastapi import APIRouter
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from os import getenv
from paypalcheckoutsdk.orders import OrdersCreateRequest
from app.utils.payment import pay
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.config import Config
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from app.services.user import UserServices
from app.models.schemas import (
    user as _user_schemas,
    info as _info_schemas
)
from app.db.repositories.user.get_user_by_account import get_user_by_account
from typing import Optional
import json
import webbrowser
import sys

router = router = APIRouter(
    prefix="",
    tags=["Pay Ment"],
    responses={404: {"description": "Not found"}}
)


s = {}

config = Config('.env')
oauth = OAuth(config)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

# Creating Access Token for Sandbox
client_id = "AWqzcbRdGkQQPHFjTeDEQfcg91yykM6-l0x_d0XfTsvO72Trq3nMq7cpCq2pyYvwScBsL87WkHlIjxNU"
client_secret = "EAuKGzpc4V9wSOomBv5vjDxNWzGrO75OsN62No6XGw6zOWduxGSI8MmlmDljC4CzHCpf3dasqgebTxy5"

# Creating an environment
environment = SandboxEnvironment(
    client_id=client_id, client_secret=client_secret)
client = PayPalHttpClient(environment)

# @router.post("/create-order")
# async def create_order_paypal(request: Request):
#     try:
#         data = await request.json()
#         request = OrdersCreateRequest()

#         request.prefer('return=representation')
#         request.request_body(
#             {
#                 "intent": "CAPTURE",
#                 "purchase_units": [
#                     {
#                         "amount": {
#                             "currency_code": "USD",
#                             "value": "100.00"
#                         }
#                     }
#                 ],
#                 "items": data
#             }
#         )
#         response = client.execute(request)
#         return JSONResponse(content={"id": response.result.id})
#     except IOError:
#         print(IOError)


@router.get("/create-order")
async def create_order_paypal(
    request: Request,
    money: Optional[int] = None,
    order_id: Optional[int] = None,
    close: Optional[int] = None
):
    user = request.session.get(f'{order_id}')
    # print(order_id)
    # data = json.dumps(user)
    # print(data)
    # return HTMLResponse(data)
    data = json.dumps(s.get(f'{order_id}'))
    # if user:
    #     print("ahihi")
    #     data = json.dumps(user)
    #     print(data)
    #     webbrowser.close()
    #     return HTMLResponse(data)
    if close == 0:
        return HTMLResponse('<button type="button" onclick="javascript:window.close()">Discard</button>')
    if data != 'null':
        print(data)
        return HTMLResponse(data)
    if order_id and money:
        respon = pay(money, order_id)
        webbrowser.open_new(respon)
        return respon
    # webbrowser.close()
    # print(order_id)
    # data = json.dumps(user)
    # print(data)
    # data = json.dumps(s.get(f'{order_id}'))
    return HTMLResponse(data)


@router.get("/payment_return")
async def payment_return(
    vnp_Amount: int,
    vnp_BankCode: str,
    vnp_BankTranNo: str,
    vnp_CardType: str,
    vnp_OrderInfo: str,
    vnp_PayDate: str,
    vnp_ResponseCode: int,
    vnp_TmnCode: str,
    vnp_TransactionNo: int,
    vnp_TransactionStatus: int,
    vnp_TxnRef: int,
    vnp_SecureHash: str,
    request: Request
):
    respon = {
        "vnp_Amount": vnp_Amount,
        "vnp_BankCode": vnp_BankCode,
        "vnp_BankTranNo": vnp_BankTranNo,
        "vnp_CardType": vnp_CardType,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_PayDate": vnp_PayDate,
        "vnp_ResponseCode": vnp_ResponseCode,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_TransactionNo": vnp_TransactionNo,
        "vnp_TransactionStatus": vnp_TransactionStatus,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_SecureHash": vnp_SecureHash,
        "url": request.url._url
    }
    request.session[f'{vnp_TxnRef}'] = respon
    # user = request.session.get(f'{vnp_TxnRef}')
    s.update({f'{vnp_TxnRef}': respon})
    print(s.get(f'{vnp_TxnRef}'))
    # print(vnp_TxnRef)
    # data = json.dumps(user)
    # print(data)
    return RedirectResponse(url=f'http://localhost:3000/purchase/id_order={vnp_TxnRef}')


@router.get('/google-link')
async def homepage(request: Request):
    return {"http://127.0.0.1:8000/login"}


@router.get('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    respon = await oauth.google.authorize_redirect(request, redirect_uri)
    print(respon)
    return respon


@router.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return {error.error}
    user = token.get('userinfo')
    respon = ""
    if user:
        # request.session['user'] = dict(user)
        _user = dict(user)
        _info = _info_schemas.InfoCreate(**{
            "full_name": _user.get("name"),
            "email": _user.get("email"),
            "phone": "0123456789",
            "dob": "2000-01-01",
            "address": "Chua Co Dia Chi",
        })
        _user_create = _user_schemas.UserCreate(**{
            "account": str(_user.get("email")),
            "password": str(_user.get("email")),
            "id_permission": 3,
            "info": _info
        })
        check_user = get_user_by_account(_user.get("email"))
        if check_user:
            _user_login = _user_schemas.UserLogin(**{
                "account": str(_user.get("email")),
                "password": str(_user.get("email")),
            })
            respon = UserServices.get_user(_user_login)
        else:
            respon = "Ahihi"
            respon = UserServices.create_user(_user_create)

    return respon
