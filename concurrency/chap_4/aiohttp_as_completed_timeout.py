import asyncio
import aiohttp

from concurrency.util.utils import fetch_status
from concurrency.util.timer import async_timer


@async_timer()
async def main():
    async with aiohttp.ClientSession() as session:
        fetches = [
            asyncio.create_task(fetch_status(session, "https://example.com")),
            asyncio.create_task(fetch_status(session, "https://example.com")),
        ]

        done, pending = await asyncio.wait(fetches)

        print(f"Done tasks count {len(done)}")
        print(f"Pending tasks count {len(pending)}")


asyncio.run(main())
