import asyncio
import asyncpg


async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="products", password="roman"
    )

    async with conn.transaction():
        await conn.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
        await conn.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2')")
        query = "select brand_name from brand where brand_name like 'brand%' "

        brands = await conn.fetch(query)

        print(brands)

    await conn.close()


asyncio.run(main())
