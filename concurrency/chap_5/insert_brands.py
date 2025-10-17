import asyncio
import asyncpg

from typing import List, Tuple, Union

from random import sample


def load_common_words() -> List[str]:
    with open(
        "/Users/roman/projects/py_train/concurrency/chap_5/words.txt", "r"
    ) as reader:
        return reader.readlines()


def gen_brand_names(words: List[str]) -> List[Tuple[Union[str,]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = gen_brand_names(common_words)

    insert_statement = "insert into brand values(DEFAULT, $1)"
    return await connection.executemany(insert_statement, brands)


async def main():
    common_words = load_common_words()

    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="products", password="roman"
    )
    print("Got connection!")

    await insert_brands(common_words, conn)

    await conn.close()


asyncio.run(main())
