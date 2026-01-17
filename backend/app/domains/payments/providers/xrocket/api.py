from fastapi import APIRouter
from starlette.requests import Request

from app.core.settings import settings

xrocket_webhook = APIRouter(prefix=settings.XROCKET_WEBHOOK, tags=["xrocket"])

@xrocket_webhook.post("")
async def get_xrocket_payment(request: Request):
    raw_body = await request.body()
    print(request)
    print()
    print(raw_body)

d = {
    "type":"invoicePay",
    "timestamp":"2026-01-11T08:15:24.396Z",
    "data":{"id":"3690770","amount":0.3,"minPayment":null,"currency":"USDT","description":"","hiddenMessage":"","payload":"","callbackUrl":"","created":"2026-01-11T08:14:27.000Z","paid":"2026-01-11T08:15:24.000Z","status":"paid","expiredIn":0,"link":"https://t.me/xrocket?start=inv_wW61TIMMRZ2IR2m","activationsLeft":0,"totalActivations":1,"payment":{"userId":1972087205,"paymentNum":1,"paid":"2026-01-11T08:15:24.396Z","paymentAmount":0.3,"paymentAmountReceived":0.2955}}}