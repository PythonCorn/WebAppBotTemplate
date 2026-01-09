import json

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from sqlalchemy.ext.asyncio import AsyncSession

from app.bot.keyboards.inline import MAIN_PAGE, create_inline_keyboard, PROFILE_PAGE
from app.cache.client import get_redis
from app.domains.users.repos import UserRepo
from app.domains.payments.providers.cryptobot.client import CRYPTOBOT_CLIENT

profile_router = Router(name="profile")

@profile_router.callback_query(F.data == MAIN_PAGE["profile"].callback_data)
async def user_profile(call: CallbackQuery, session: AsyncSession):
    await call.answer()
    user_repo = UserRepo(session)
    user = await user_repo.get_user_by_telegram_id(call.from_user.id)
    await call.message.answer(
        text=f"UserID: {user.telegram_id}\n"
             f"Username: {user.username}\n"
             f"Balance: {user.balance}\n",
        reply_markup=create_inline_keyboard(PROFILE_PAGE)
    )

@profile_router.callback_query(F.data == PROFILE_PAGE["update_balance"].callback_data)
async def update_balance(call: CallbackQuery):
    await call.answer()
    async with CRYPTOBOT_CLIENT:
        invoice = await CRYPTOBOT_CLIENT.create_invoice(
            amount=5,
            asset="TRX"
        )
        cache = get_redis()
        await cache.set(
            f"invoice:{invoice.invoice_id}",
            json.dumps({
                "telegram_id": call.from_user.id,
                "amount": invoice.amount,
                "currency": invoice.asset,
            }),
            ex=3600
        )
        await call.message.answer(
            text=f"Вы решили пополнить баланс на {invoice.amount} {invoice.asset}?",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Yes",
                            url=invoice.bot_invoice_url
                        )
                    ]
                ]
            )
        )