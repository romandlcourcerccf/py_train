import asyncio
import aiohttp

from concurrency.util.utils import fetch_status
from concurrency.util.timer import async_timer


@async_timer()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://example.com", "https://example333.com"]
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        results = [res for res in results if not isinstance(res, Exception)]
        # print(exceptions)
        print(results)


asyncio.run(main())
