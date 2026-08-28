def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y

history = []

while True:
    print("Выберите операцию: ")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. История вычислений")
    choice = input("Введите номер операции (1/2/3/4/5): ").strip()
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно ввести числа!")
            continue
        if choice == '1':
            result = f"Результат: {num1} + {num2} = {add(num1, num2)}"
            print(result)
            history.append(result)
        elif choice == '2':
            result = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
            print(result)
            history.append(result)
        elif choice == '3':
            result = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
            print(result)
            history.append(result)
        elif choice == '4':
            result = f"Результат: {num1} / {num2} = {divide(num1, num2)}"
            print(result)
            history.append(result)
    elif choice == '5':
        if not history:
            print("История пуста.")
        else:
            print("История вычислений:\n"),
            for i, rec in enumerate(history, start=0):
                print(f"{rec}")
        break
    else:
        print("Неверный выбор. Введите число от 1 до 5.")