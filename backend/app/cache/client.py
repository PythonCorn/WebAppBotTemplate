from typing import Optional

from redis.asyncio import Redis

from app.core.settings import settings

REDIS: Optional[Redis] = None

def get_redis():
    global REDIS
    if REDIS is None:
        REDIS = Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                decode_responses=True
            )
    return REDIS