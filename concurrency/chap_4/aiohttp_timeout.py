import asyncio
import aiohttp

from aiohttp import ClientSession
from concurrency.util.timer import async_timer


@async_timer()
async def fetch_status(session: ClientSession, url: str) -> int:
    timeout = aiohttp.ClientTimeout(total=0.01)
    async with session.get(url, timeout=timeout) as result:
        return result.status


async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://www.example.com"

    async with aiohttp.ClientSession() as session:
        status = await fetch_status(session, url)

        print(f"Got {status} from url {url}")


asyncio.run(main())
