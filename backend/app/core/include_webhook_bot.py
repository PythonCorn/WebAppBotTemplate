from aiogram import Bot

from app.core.settings import settings


async def set_bot_webhook(bot: Bot, public_url: str):
    await bot.delete_webhook(drop_pending_updates=True)
    endpoint = f"{public_url}/webhook/{settings.BOT_WEBHOOK}"
    await bot.set_webhook(url=endpoint)

async def close_bot_webhook(bot: Bot):
    await bot.delete_webhook(drop_pending_updates=False)
    await bot.session.close()