
from fastapi import APIRouter, Request
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from os import getenv
from paypalcheckoutsdk.orders import OrdersCreateRequest
from fastapi.responses import JSONResponse
from app.utils.payment import pay


router = router = APIRouter(
    prefix="",
    tags=["Pay Ment"],
    responses={404: {"description": "Not found"}}
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

@router.post("/create-order")
async def create_order_paypal(    
    money:int,
    order_id: int):
    respon = pay(money, order_id)
    return respon

@router.get("/payment_return")
async def payment_return(
    vnp_Amount: int,
    vnp_BankCode: str,
    vnp_BankTranNo: int,
    vnp_CardType: str,
    vnp_OrderInfo: str,
    vnp_PayDate: str,
    vnp_ResponseCode: int,
    vnp_TmnCode: str,
    vnp_TransactionNo: int,
    vnp_TransactionStatus: int,
    vnp_TxnRef: int,
    vnp_SecureHash: str
):
    respon = {
        "vnp_Amount": vnp_Amount,
        "vnp_BankCode": vnp_BankCode,
        "vnp_BankTranNo": vnp_BankTranNo,
        "vnp_CardType": vnp_CardType,
        "vnp_PayDate": vnp_PayDate,
        "vnp_ResponseCode": vnp_ResponseCode,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_TransactionNo": vnp_TransactionNo,
        "vnp_TransactionStatus": vnp_TransactionStatus,
        "vnp_TxnRef":vnp_TxnRef,
        "vnp_SecureHash": vnp_SecureHash
    }
    return respon