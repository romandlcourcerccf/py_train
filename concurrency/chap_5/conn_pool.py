import asyncio
import asyncpg
from concurrency.util.timer import async_timer

product_query = """
SELECT
p.product_id,
p.product_name,
p.brand_id,
s.sku_id,
pc.product_color_name,
ps.product_size_name
FROM product as p
JOIN sku as s on s.product_id = p.product_id
JOIN product_color as pc on pc.product_color_id = s.product_color_id JOIN product_size as ps on ps.product_size_id = s.product_size_id WHERE p.product_id = 100"""


async def query_product(pool):
    async with pool.acquire() as conn:
        return await conn.fetchrow(product_query)


@async_timer()
async def query_sync(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timer()
async def query_async(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


async def main():
    async with asyncpg.create_pool(
        host="127.0.0.1",
        port=5432,
        user="12345",
        database="test",
        password="roman",
        min_size=6,
        max_size=6,
    ) as pool:
        await query_async(pool, 10000)
        await query_sync(pool, 10000)


asyncio.run(main())
