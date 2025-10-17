import asyncio
import asyncpg

from random import randint, sample
from typing import List, Tuple


def load_common_words() -> List[str]:
    with open(
        "/Users/roman/projects/py_train/concurrency/chap_5/words.txt", "r"
    ) as reader:
        return reader.readlines()


def gen_products(
    common_words: List[str],
    brand_id_start: int,
    brand_id_end: int,
    products_to_create: int,
) -> List[Tuple[str, int]]:
    products = []
    for _ in range(products_to_create):
        description = [common_words[index] for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))

    return products


def gen_skus(
    product_id_start: int, product_id_end: int, skus_to_create: int
) -> List[Tuple[int, int, int]]:
    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))

    return skus


async def main():
    common_words = load_common_words()

    conn = await asyncpg.connect(
        host="127.0.0.1", port=5432, user="12345", database="products", password="roman"
    )

    prod_tuples = gen_products(
        common_words=common_words,
        brand_id_start=1,
        brand_id_end=100,
        products_to_create=100,
    )

    print(prod_tuples[0])

    # await conn.executemany(
    #     "INSERT INTO product VALUES(DEFAULT, $1, $2)", [prod_tuples[0]]
    # )

    sku_tuples = gen_skus(product_id_start=1, product_id_end=500, skus_to_create=100000)
    await conn.executemany("insert into sku values (DEFAULT, $1, $2, $3)", sku_tuples)

    await conn.close()


asyncio.run(main())
