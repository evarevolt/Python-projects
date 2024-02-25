import asyncio

async def async_timer(message):
    for i in range(10):
        print(message)
        await asyncio.sleep(1)
    

# Используйте event loop для запуска асинхронной функции
loop = asyncio.get_event_loop()
loop.run_until_complete(async_timer('give me your money'))