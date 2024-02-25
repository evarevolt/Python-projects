import aiohttp
import asyncio
from aiohttp import ClientTimeout

async def fetch_data(url, timeout=30):
    async with aiohttp.ClientSession(timeout=ClientTimeout(timeout)) as session: # создаем сессию с использованием менеджера контекста
        async with session.get(url) as response: # делаем GET-запрос
            return await response.json() # получаем тело ответа в json формате

async def print_data(url):
    data = await fetch_data(url)
    print("Ответ от сервера:", data['title'])

async def main():
    url = "https://dummyjson.com/products/{number}"
    COUNT = 10
    tasks = []
    for number in range(1,COUNT):
        task = asyncio.create_task(print_data(url.format(number=number)))
        tasks.append(task)
    await asyncio.gather(tasks)

asyncio.run(main())