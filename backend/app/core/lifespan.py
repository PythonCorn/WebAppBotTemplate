import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.bot.client import bot
from app.cache.client import get_redis
from app.core.ngrok_url import get_public_url
from app.core.include_webhook_bot import set_bot_webhook, close_bot_webhook


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = get_redis()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    public_url = await get_public_url()  # получение публичной ссылки
    await set_bot_webhook(bot, public_url)  # передача ссылки в бота для установки webhook
    yield
    await close_bot_webhook(bot)  # закрытие сессии бота
    await redis.close()
