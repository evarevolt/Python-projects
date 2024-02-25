import asyncio

class AsyncCache:
    def __init__(self):
        self.cache = {}

    async def set(self, key, value):
        # Имитация асинхронной операции с использованием asyncio.sleep
        await asyncio.sleep(1)  # Имитация задержки
        self.cache[key] = value

    async def get(self, key):
        # Имитация асинхронной операции с использованием asyncio.sleep
        await asyncio.sleep(1)  # Имитация задержки
        return self.cache.get(key)

# Функция для демонстрации использования асинхронного кэша
async def use_cache(cache, key, value):
    await cache.set(key, value)
    stored_value = await cache.get(key)
    print(f"Key: {key}, Stored Value: {stored_value}")

# Функция для запуска параллельных задач
async def main():
    cache = AsyncCache()
    # Создание и запуск параллельных задач для демонстрации работы кэша
    tasks = [use_cache(cache, f"key__{i}", i) for i in range(5)]
    await asyncio.gather(*tasks)

# Запуск асинхронной программы
asyncio.run(main())
