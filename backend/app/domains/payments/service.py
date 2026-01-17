from abc import ABC, abstractmethod
from typing import Union

from aiocryptopay.models.invoice import Invoice

from app.domains.payments.available_currencies import Currency
from app.domains.payments.providers import CRYPTOBOT_CLIENT, XROCKET_CLIENT
from app.domains.payments.providers.xrocket.schemas import XRocketInvoiceResponse, XRocketData
from app.domains.payments.schemas import BaseInvoice


class AbstractPaymentService(ABC):

    @abstractmethod
    async def create_invoice(self, amount: Union[int, float], currency: Currency) -> BaseInvoice: ...


class CryptoBotPaymentService(AbstractPaymentService):
    async def create_invoice(self, amount: Union[int, float], currency: Currency):
        async with CRYPTOBOT_CLIENT:
            invoice: Invoice = await CRYPTOBOT_CLIENT.create_invoice(
                amount=amount,
                asset=currency
            )
            return BaseInvoice(
                invoice_id=invoice.invoice_id,
                amount=invoice.amount,
                currency=invoice.asset,
                url=invoice.bot_invoice_url
            )


class XRocketPaymentService(AbstractPaymentService):
    async def create_invoice(self, amount: Union[int, float], currency: Currency):
        invoice = await XROCKET_CLIENT.invoice_create(
            amount=amount,
            currency=currency
        )
        invoice_data = XRocketInvoiceResponse.model_validate(invoice)
        if not invoice_data.success:
            raise AttributeError(invoice_data.error)
        invoice: XRocketData = invoice_data.data
        return BaseInvoice(
            invoice_id=invoice.id,
            amount=invoice.amount,
            currency=invoice.currency,
            url=invoice.link
        )


class PaymentService:
    def __init__(self):
        self.providers = {
            "cryptobot": CRYPTOBOT_CLIENT,
            "xrocket": XROCKET_CLIENT
        }
