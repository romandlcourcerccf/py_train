import asyncio
import asyncpg
from asyncpg.transaction import Transaction

import logging


async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="products", password="roman"
    )

    transaction: Transaction = conn.transaction()
    await transaction.start()

    try:
        async with conn.transaction():
            await conn.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1_1')")
            await conn.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1_2')")
    except asyncpg.PostgresError as ex:
        logging.exception(ex)
        await transaction.rollback()
    else:
        await transaction.commit()

    query = """
            select brand_name from brand where brand_name like 'brand_1%'
            """
    brands = await conn.fetch(query)
    print(brands)

    await conn.close()


asyncio.run(main())
