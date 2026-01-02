import hashlib
import hmac
from typing import Dict, Any
from urllib.parse import parse_qsl

from fastapi import HTTPException

from app.core.settings import settings


def telegram_auth(init_data: str) -> Dict[str, Any]:
    data = dict(parse_qsl(init_data.replace("?", "")))

    check_hash = data.pop("hash")

    check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))

    secret_key = hmac.new(
        key=b"WebAppData",
        msg=settings.BOT_TOKEN.encode(),
        digestmod=hashlib.sha256
    ).digest()

    calculated_hash = hmac.new(secret_key, check_string.encode(), hashlib.sha256).hexdigest()

    if calculated_hash != check_hash:
        raise HTTPException(status_code=403, detail="Invalid init data")

    return data