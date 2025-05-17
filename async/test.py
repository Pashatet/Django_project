import aiohttp
import asyncio
from aiocache import cached, caches, Cache
import time

default_cache = caches.get('default')
# # **Использование кеша без декоратора
# async def fetch(url):
#     cached_response = await default_cache.get(url)
#     if cached_response is not None:
#         return cached_response  # Возвращаем кешированный ответ, если он есть
#     else:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 text = await response.text()
#                 await default_cache.set(url, text, ttl=20)  # Сохраняем ответ в кеш
#                 return text

# Декоратор для кеширования асинхронной функции
@cached(ttl=20, cache=Cache.MEMORY)  # ttl - время жизни кеша в секундах
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = 'https://httpbin.org/delay/2'  # задержка ответа в 2 секунды

    # При первом вызове данные будут получены и сохранены в кеше.
    # Замеряем время выполнения запроса.
    start_time = time.time()
    response = await fetch(url)
    end_time = time.time()
    print(f"First request duration: {end_time - start_time:.2f} seconds")
    print(f"First request content: {response[:100]}...")  # печать первых 100 символов

    # Второй запрос (должен идти из кеша)
    # Замеряем время выполнения запроса.
    start_time = time.time()
    response = await fetch(url)
    end_time = time.time()
    print(f"Second request duration (from cache): {end_time - start_time:.2f} seconds")
    print(f"Second request content (from cache): {response[:100]}...")  # печать первых 100 символов из кеша


asyncio.run(main())