import asyncpg
import asyncio


async def main():
    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="test", password="roman"
    )

    print(conn.get_server_version())

    await conn.close()


asyncio.run(main())
