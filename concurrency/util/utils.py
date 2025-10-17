from concurrency.util.timer import async_timer
import asyncio
import aiohttp
from aiohttp import ClientSession


@async_timer()
async def fetch_status(
    session: ClientSession, url: str, total=5, delay: int = 0
) -> int:
    await asyncio.sleep(delay)
    timeout = aiohttp.ClientTimeout(total)
    async with session.get(url, timeout=timeout) as result:
        return result.status
