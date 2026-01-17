from fastapi import APIRouter

from app.domains.payments.providers.cryptobot.api import cryptobot_webhook
from app.domains.payments.providers.xrocket.api import xrocket_webhook

payments_router = APIRouter(prefix="/payments", tags=["payments"])
payments_router.include_router(cryptobot_webhook)
payments_router.include_router(xrocket_webhook)