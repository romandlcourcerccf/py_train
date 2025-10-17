import asyncio
import asyncpg


async def take(gen, to_take: int):
    counter = 0
    async for item in gen:
        if counter > to_take:
            return
        else:
            yield item


async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="products", password="roman"
    )

    query = "SELECT product_id, product_name FROM product"

    async with conn.transaction():
        cursor = conn.cursor(query)  #!!!!!!

        async for prod in take(cursor, 10):
            print(prod)

    await conn.close()


asyncio.run(main())
