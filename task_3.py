import asyncio

def calculate(expr):
    # Разбиваем выражение по пробелам
    parts = expr.split()
    if len(parts) != 3:
        return "Ошибка: неверный формат. Используйте формат 'число оператор число'."
    num1, op, num2 = parts
    try:
        num1, num2 = float(num1), float(num2)
    except ValueError:
        return "Ошибка: оба аргумента должны быть числами."

    # Используем match для выбора операции
    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "Ошибка: деление на ноль."
        case _:
            return "Ошибка: неизвестная операция. Доступные операции: +, -, *, /."

async def main():
    while True:
        expr = await asyncio.to_thread(input, "Введите математическую операцию (или 'exit' для выхода): ")
        if expr.lower() == 'exit':
            print("Программа завершена.")
            break
        result = calculate(expr)
        print(f"Результат: {result}")

if __name__ == '__main__':
    asyncio.run(main())