from enum import StrEnum


class BalanceActions(StrEnum):
    UPDATE = "UPDATE"
    WITHDRAW = "WITHDRAW"

class PaymentProviders(StrEnum):
    XROCKET = "XROCKET"
    CRYPTOBOT = "CRYPTOBOT"