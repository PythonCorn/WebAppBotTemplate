from aiocryptopay import AioCryptoPay, Networks

from app.core.settings import settings

CRYPTOBOT_CLIENT = AioCryptoPay(
    token=settings.CRYPTOBOT_TOKEN,
    network=Networks.TEST_NET if settings.IS_TEST_CRYPTOBOT else Networks.MAIN_NET
)