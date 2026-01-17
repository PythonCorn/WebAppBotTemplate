from decimal import Decimal
from typing import Union

from xrocket import PayAPI

from app.core.settings import settings
from app.domains.payments.available_currencies import Currency
from app.domains.payments.providers.xrocket.schemas import XRocketInvoiceResponse, XRocketData

XROCKET_CLIENT = PayAPI(
    api_key=settings.XROCKET_TOKEN
)

async def create_invoice_xrocket(amount: Union[int, float, Decimal], currency: Currency) -> XRocketData:
    invoice = await XROCKET_CLIENT.invoice_create(
        amount=amount,
        currency=currency
    )
    data = XRocketInvoiceResponse.model_validate(invoice)
    if not data.success:
        raise AttributeError(f"{data.error}")
    return data.data
