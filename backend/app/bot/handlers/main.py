from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton

from app.bot.keyboards.inline import create_inline_keyboard, MAIN_PAGE
from app.domains.payments.available_currencies import Currency
from app.domains.payments.providers import XROCKET_CLIENT
from app.domains.payments.providers.xrocket.client import create_invoice_xrocket

main_router = Router(name="main")

@main_router.message(CommandStart())
async def main_menu(msg: Message):

    invoice = await create_invoice_xrocket(0.3, Currency.USDT)
    print(invoice)
    MAIN_PAGE["invoice"] = InlineKeyboardButton(
        text=f"Оплати {0.3}{Currency.USDT}",
        url=invoice.link
    )
    await msg.answer(
        text="Hello!",
        reply_markup=create_inline_keyboard(MAIN_PAGE)
    )