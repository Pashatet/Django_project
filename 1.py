import aiohttp
import asyncio

# Асинхронная функция для выполнения GET-запроса с передачей параметров
async def fetch_with_params(session, url, params=None):
    async with session.get(url, params=params) as response:
        return response.url

async def main():
    # Параметры для GET-запроса
    params = {
        'param1': 'value1',
    }

    # Создание асинхронной сессии и отправка запроса с параметрами
    async with aiohttp.ClientSession() as session:
        response = await fetch_with_params(session, 'http://example.com/page', params)
        print(response)

# Запуск асинхронной функции
asyncio.run(main())

# dfsfsfdsf