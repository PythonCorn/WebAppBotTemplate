from aiogram.types import Update
from fastapi import APIRouter
from starlette.requests import Request

from app.bot.client import dispatcher, bot

webhook_bot = APIRouter(prefix="/bot", tags=["webhook"])

@webhook_bot.post("")
async def webhook_endpoint(request: Request):
    body = await request.json()
    update = Update.model_validate(body)
    await dispatcher.feed_update(bot, update)
    return {
        "status": "ok"
    }