import asyncio
import asyncpg

import logging


async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="products", password="roman"
    )

    try:
        async with conn.transaction():
            await conn.execute("INSERT INTO brand VALUES(7777, 'brand_1')")
            await conn.execute("INSERT INTO brand VALUES(7777, 'brand_2')")
    except Exception as ex:
        logging.exception(ex)

    finally:
        await conn.close()


asyncio.run(main())
