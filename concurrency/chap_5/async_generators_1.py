import asyncio
import asyncpg


async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="products", password="roman"
    )

    query = "SELECT product_id, product_name FROM product"

    async with conn.transaction():
        async for prod in conn.cursor(query):
            print(prod)

    await conn.close()


asyncio.run(main())
