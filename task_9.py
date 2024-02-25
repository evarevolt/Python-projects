import asyncio

class AsyncCounter:
    def __init__(self):
        self.value = 0
        self.lock = asyncio.Lock()

    async def increment(self):
        async with self.lock:
            await asyncio.sleep(0.1)  # Имитация асинхронной операции
            self.value += 1

    async def decrement(self):
        async with self.lock:
            await asyncio.sleep(0.1)  # Имитация асинхронной операции
            self.value -= 1

    async def get_value(self):
        return self.value

async def modify_counter(counter, func, n):
    for _ in range(n):
        await func()

async def main():
    counter = AsyncCounter()
    tasks = [
        modify_counter(counter, counter.increment, 60),
        modify_counter(counter, counter.decrement, 50),
    ]
    
    # Запускаем задачи параллельно
    await asyncio.gather(*tasks)

    # Выводим итоговое значение счетчика
    print(f"Финальное значение: {await counter.get_value()}")

# Запускаем асинхронный цикл
asyncio.run(main())
