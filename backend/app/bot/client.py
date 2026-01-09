from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.bot.handlers.main import main_router
from app.bot.handlers.profile import profile_router
from app.bot.middlewares.database import DatabaseMiddleware
from app.core.settings import settings


bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

dispatcher = Dispatcher()
dispatcher.message.middleware(DatabaseMiddleware())
dispatcher.callback_query.middleware(DatabaseMiddleware())

dispatcher.include_router(main_router)
dispatcher.include_router(profile_router)

# @dispatcher.message(CommandStart())
# async def sds(msg: Message, session: AsyncSession):
#     async with CRYPTOBOT_CLIENT:
#         invoice = await CRYPTOBOT_CLIENT.create_invoice(
#             amount=5,
#             asset="TRX"
#         )
#     user_repo = UserRepo(session)
#     await user_repo.add_new_user(
#         telegram_id=msg.from_user.id,
#         username=msg.from_user.username,
#     )
#     await msg.answer(
#         "Hello",
#         reply_markup=InlineKeyboardMarkup(
#             inline_keyboard=[
#                 [
#                     InlineKeyboardButton(
#                         text="app",
#                         web_app=WebAppInfo(url="https://impoverished-agley-sharron.ngrok-free.dev/")
#                     ),
#                     InlineKeyboardButton(
#                         text="Pay",
#                         url=invoice.bot_invoice_url
#                     )
#                 ]
#
#             ]
#         )
#     )