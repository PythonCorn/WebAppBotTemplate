from xrocket import PayAPI

from app.core.settings import settings

XROCKET_CLIENT = PayAPI(
    api_key=settings.XROCKET_TOKEN
)