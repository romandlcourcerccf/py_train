import asyncio
import asyncpg

from asyncpg import Record
from typing import List


async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="test", password="roman"
    )

    print("Got connection!")

    await conn.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await conn.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"

    results: List[Record] = await conn.fetch(brand_query)

    for brand in results:
        print(brand)

    await conn.close()


asyncio.run(main())
