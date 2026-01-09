from typing import Dict, Tuple

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

MAIN_PAGE = {
    "profile": InlineKeyboardButton(
        text="Профиль",
        callback_data="profile"
    )
}

PROFILE_PAGE = {
    "update_balance": InlineKeyboardButton(
        text="Пополнить баланс",
        callback_data="update_balance"
    )
}

def create_inline_keyboard(buttons: Dict[str, InlineKeyboardButton], sizes: Tuple[int, ...] = (1, )):
    builder = InlineKeyboardBuilder()
    builder.add(*buttons.values())
    return builder.adjust(*sizes).as_markup()
