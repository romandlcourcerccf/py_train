import asyncio
import aiohttp

from aiohttp import ClientSession
from concurrency.util.timer import async_timer


@async_timer()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://www.example.com"

    async with aiohttp.ClientSession() as session:
        status = await fetch_status(session, url)

        print(f"Got {status} from url {url}")


asyncio.run(main())
