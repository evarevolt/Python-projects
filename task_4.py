import asyncio

async def task(number, divisor):
    print(f"Задача {number}: начало работы")
    await asyncio.sleep(1)
    if divisor == 0:
        raise ValueError("Ошибка деления на ноль")
    result = number / divisor
    print(f"Задача {number}: завершена с результатом {result}")
    return result

async def main():
    tasks = [
        task(1, 2),
        task(2, 0),  # Ошибка
        task(3, 3)
    ]
    results = []
    for future in asyncio.as_completed(tasks):
        try:
            result = await future
            results.append(result)
        except Exception as e:
            print(f"В задаче возникла ошибка: {e}")
    print(f"Итоговые результаты успешных задач: {results}")

if __name__ == '__main__':
    asyncio.run(main())
