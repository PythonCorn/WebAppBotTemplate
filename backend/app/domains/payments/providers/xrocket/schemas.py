from typing import Union, Optional

from pydantic import BaseModel

class XRocketData(BaseModel):
    id: int
    amount: Union[int, float]
    currency: str
    description: Optional[str]
    payload: Optional[str]
    callbackUrl: Optional[str]
    status: Optional[str]
    link: Optional[str]

class XRocketInvoiceResponse(BaseModel):
    success: bool
    data: XRocketData