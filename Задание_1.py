# Задание 1.
# i = -7
# while i < 43:
#     i += 10
#     print(i, end=' ')
# Задание 2.
password = input("Введите пароль (не менее 8 символов): ")
while len(password) < 8:
    print("Пароль слишком короткий! Нужно минимум 8 символов.")
    password = input("Попробуйте ещё раз: ")
print("Пароль принят!")
# Задание 3.
user_input = input("Введите строку с параметрами автомобиля: ")
parts = user_input.split()  # деление по пробелам
mark = parts[0]
year = parts[1]
mileage = parts[2]
price = parts[3]
res = (
    f"Продается автомобиль\n"
    f"Марка: {mark}\n"
    f"Год выпуска: {year}\n"
    f"Пробег: {mileage}\n"
    f"Цена: {price}"
)
print(res)
