import asyncio
import aiohttp

from aiohttp import ClientSession
from concurrency.util.utils import fetch_status
from concurrency.util.timer import async_timer


@async_timer()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://example.com" for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
