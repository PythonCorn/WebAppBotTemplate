import asyncio
from typing import Optional, Dict, Union

from app.domains.payments.available_currencies import Currency, FIAT
from app.domains.payments.providers.cryptobot.client import CRYPTOBOT_CLIENT

RATES: Optional[Dict[str, float]] = None

async def get_exchange(amount: Union[int, float], user_currency: Currency, bot_currency=FIAT):
    async with CRYPTOBOT_CLIENT:
        value = await CRYPTOBOT_CLIENT.get_amount_by_fiat(amount, user_currency, bot_currency)
        print(value)

async def get_rates():
    global RATES

    if RATES is None:
        async with CRYPTOBOT_CLIENT:
            rates = await CRYPTOBOT_CLIENT.get_exchange_rates()
            return rates

if __name__ == '__main__':
    asyncio.run(get_rates())