from enum import StrEnum
from typing import List


class Currency(StrEnum):
    USDT = "USDT"
    USDC = "USDC"
    ETH = "ETH"
    ETC = "ETC"
    BTC = "BTC"
    TRC = "TRC"
    TON = "TON"
    BNB = "BNB"

    @classmethod
    def currency_list(cls) -> List[str]:
        return [c.value for c in cls]  # type: ignore


class Fiat(StrEnum):
    RUB = "RUB"
    USD = "USD"


FIAT = Fiat.RUB

AVAILABLE_CURRENCIES: List[str] = Currency.currency_list()
