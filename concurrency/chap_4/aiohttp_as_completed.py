import asyncio
import aiohttp

from concurrency.util.utils import fetch_status
from concurrency.util.timer import async_timer


@async_timer()
async def main():
    async with aiohttp.ClientSession() as session:
        fetches = [
            fetch_status(session, "https://example.com", 0),
            fetch_status(session, "https://example.com", 2),
            fetch_status(session, "https://example.com", 10),
        ]

        for finished_task in asyncio.as_completed(fetches):
            print(await finished_task)


asyncio.run(main())
