import asyncio

async def child_task(id, delay):
    print(f"Task {id} started")
    await asyncio.sleep(delay)
    print(f"Task {id} finished after {delay} seconds")
    return f"Result of task {id}"

async def parent_task():
    print("Parent task started")
    # Создаем асинхронные задачи
    tasks = [asyncio.create_task(child_task(i, delay)) for i, delay in enumerate([2, 3, 1], start=1)]
    # Ожидаем завершения всех задач
    results = await asyncio.gather(*tasks)
    print("Parent task finished")
    return results

async def main():
    results = await parent_task()
    print(f"All tasks completed. Results: {results}")

# Запускаем асинхронный цикл
asyncio.run(main())
