import asyncio

import aiohttp

from app.core.settings import settings


async def get_public_url(retries: int = 10, delay: float = 1.0) -> str:
    """
    Получение публичной https ссылки из ngrok.
    :param retries:
    :param delay:
    :return:
    """
    if settings.ENV == "prod":
        return settings.PUBLIC_URL

    url = "http://ngrok:4040/api/tunnels"

    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    tunnels = data.get("tunnels", [])
                    if tunnels:
                        return tunnels[0]["public_url"]
        except Exception:
            pass

        await asyncio.sleep(delay)

    raise RuntimeError("Ngrok tunnel not available")