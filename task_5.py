import random
import asyncio


async def random_generate(max_number,count):
    for i in range(count):
        await asyncio.sleep(0.5)
        yield random.randint(1,max_number)

async def print_numbers(name,max_number,count):
    async for number in random_generate(max_number,count):
        print(f'{name} - {number}')

# главная корутина
async def main():
    # создание нескольких задач
    tasks = [asyncio.create_task(print_numbers('task1',10,5)),   
    asyncio.create_task(print_numbers('task2',35,5)),
    asyncio.create_task(print_numbers('task3',100,5))
    ]
    await asyncio.gather(*tasks)

# запуск asyncio-программы
asyncio.run(main())