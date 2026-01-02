import hashlib
import hmac

from app.core.settings import settings


async def verify_signature(raw_body: bytes, signature: str) -> bool:
    secret = hashlib.sha256(settings.CRYPTOBOT_TOKEN.encode()).digest()

    computed_signature = hmac.new(
        key=secret,
        msg=raw_body,
        digestmod=hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed_signature, signature)