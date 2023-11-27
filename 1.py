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

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}
# awdadw
for x in zodiac_element:
    print(zodiac_element.get(x))
# >>>>>>> be2f9d949cc0fd60371075a83e5ef4b14cca0fb5
