from aiocryptopay.models.update import Update
from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.requests import Request

from app.cache.client import get_redis
from app.core.settings import settings
from app.domains.payments.providers.cryptobot.security import verify_signature

cryptobot_webhook = APIRouter(prefix=settings.CRYPTOBOT_WEBHOOK, tags=["cryptobot"])

@cryptobot_webhook.post("")
async def crypto_payment(request: Request):
    raw_body = await request.body()
    signature = request.headers.get("crypto-pay-api-signature")

    if not signature:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing signature"
        )

    if not await verify_signature(raw_body, signature):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid signature"
        )

    data = await request.json()
    update = Update.model_validate(data)
    print(update)
    cache = get_redis()
    invoice = await cache.get(f"invoice:{update.payload.invoice_id}")
    print(invoice)
    return {"status": "ok"}