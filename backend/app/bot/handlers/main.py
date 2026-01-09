from aiocryptopay.const import Assets
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.bot.keyboards.inline import create_inline_keyboard, MAIN_PAGE
from app.domains.payments.providers.cryptobot.client import CRYPTOBOT_CLIENT

main_router = Router(name="main")

@main_router.message(CommandStart())
async def main_menu(msg: Message):
    # rate = await get_exchange(
    #     100,
    #     Currency.USDT,
    #
    # )
    async with CRYPTOBOT_CLIENT:
        rate = await CRYPTOBOT_CLIENT.get_amount_by_fiat(
            summ=100,
            asset=Assets.TRX,
            target="RUB"
        )
        print(rate)
    await msg.answer(
        text="Hello!",
        reply_markup=create_inline_keyboard(MAIN_PAGE)
    )