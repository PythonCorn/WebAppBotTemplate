import logging
import sys
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI
from redis.asyncio import Redis

from app.bot.client import bot
from app.core.settings import settings
from app.core.ngrok_url import get_public_url
from app.core.include_webhook_bot import set_bot_webhook, close_bot_webhook

redis: Optional[Redis] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global redis

    redis = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        decode_responses=True
    )

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    public_url = await get_public_url() # получение публичной ссылки
    await set_bot_webhook(bot, public_url) # передача ссылки в бота для установки webhook
    yield
    await close_bot_webhook(bot) # закрытие сессии бота
    await redis.close()