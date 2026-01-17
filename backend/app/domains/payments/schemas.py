from typing import Union

from pydantic import BaseModel

from app.domains.payments.available_currencies import Currency


class BaseInvoice(BaseModel):
    amount: Union[int, float]
    currency: Union[Currency, str]
    invoice_id: int
    url: str