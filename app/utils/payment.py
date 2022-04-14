import hashlib
import hmac
import urllib
import urllib.parse
import urllib.request
from datetime import datetime

from app.utils.vnpay import vnpay


VNPAY_RETURN_URL = 'http://localhost:8000/payment_return'  # get from config
VNPAY_PAYMENT_URL = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
VNPAY_API_URL = 'https://sandbox.vnpayment.vn/merchant_webapi/merchant.html'
VNPAY_TMN_CODE = 'VL7HSN6Z'  # Website ID in VNPAY System, get from config
# Secret key for create checksum,get from config
VNPAY_HASH_SECRET_KEY = 'OYCFFSDAYXQPEHKNXQIHHASHDMFGMGOL'


def hmacsha512(key, data):
    byteKey = key.encode('utf-8')
    byteData = data.encode('utf-8')
    return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()


def pay(
    money: int,
    order_id_in: int
):
    # order_type = form.cleaned_data['order_type']
    order_id = order_id_in
    amount = money
    order_desc = f"Nap tien cho thue bao 0123456789. So tien {money} VND"
    bank_code = "NCB"
    language = 'vn'
    ipaddr = "14.160.92.201"
    # Build URL Payment
    vnp = vnpay()
    vnp.requestData['vnp_Version'] = '2.1.0'
    vnp.requestData['vnp_Command'] = 'pay'
    vnp.requestData['vnp_TmnCode'] = VNPAY_TMN_CODE
    vnp.requestData['vnp_Amount'] = amount * 100
    vnp.requestData['vnp_CurrCode'] = 'VND'
    vnp.requestData['vnp_TxnRef'] = order_id
    vnp.requestData['vnp_OrderInfo'] = order_desc
    # vnp.requestData['vnp_OrderType'] = order_type
    # Check language, default: vn
    if language and language != '':
        vnp.requestData['vnp_Locale'] = language
    else:
        vnp.requestData['vnp_Locale'] = 'vn'
        # Check bank_code, if bank_code is empty, customer will be selected bank on VNPAY
    if bank_code and bank_code != "":
        vnp.requestData['vnp_BankCode'] = bank_code

    vnp.requestData['vnp_CreateDate'] = datetime.now().strftime(
        '%Y%m%d%H%M%S')  # 20150410063022
    vnp.requestData['vnp_IpAddr'] = ipaddr
    vnp.requestData['vnp_ReturnUrl'] = VNPAY_RETURN_URL
    vnpay_payment_url = vnp.get_payment_url(
        VNPAY_PAYMENT_URL, VNPAY_HASH_SECRET_KEY)
    print(vnpay_payment_url)
    return vnpay_payment_url
