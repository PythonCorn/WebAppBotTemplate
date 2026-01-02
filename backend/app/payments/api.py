from fastapi import APIRouter

from app.payments.providers.cryptobot.api import cryptobot_webhook

payments_router = APIRouter(prefix="/payments", tags=["payments"])
payments_router.include_router(cryptobot_webhook)