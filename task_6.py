import asyncio
from pathlib import Path

async def search_files(directory, extension):
    """Асинхронно ищет файлы с заданным расширением в указанном каталоге."""
    loop = asyncio.get_event_loop()
    files_found = []

    async def check_file(file):
        if file.suffix == extension:
            files_found.append(file)

    tasks = []
    for file in Path(directory).rglob('*' + extension):
        # Создаем асинхронную задачу для каждого файла
        task = loop.create_task(check_file(file))
        tasks.append(task)

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)

    return files_found

async def main():
    directory = input("Введите путь к каталогу: ")
    extension = input("Введите расширение файлов для поиска (например, .txt): ")
    files_found = await search_files(directory, extension)
    
    if files_found:
        print(f"Найденные файлы с расширением {extension}:")
        for file_path in files_found:
            print(file_path)
    else:
        print(f"Файлы с расширением {extension} не найдены.")

if __name__ == '__main__':
    asyncio.run(main())
