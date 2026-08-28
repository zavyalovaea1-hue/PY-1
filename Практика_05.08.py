# users = {}
# password = '12345'
# login = "User"
#
# for i in range(1, 11):
#     print(f"User{i}") # нумерация юзеров от 1 до 10
#
#     your_login= input('Введите ваш логин: ').capitalize()
#     if your_login == login:
#         attempt = 0 # попытка 0
#         while attempt < 3:
#             your_password = input('Введите ваш пароль: ') # можно перевести в цифры через int
#             if your_password == password and your_login == login:
#                 print('Доступ разрешен')
#                 break
#             else:
#                 print('Ошибка. Повторите ввод пароля.')
#                 attempt = attempt + 1
#             if attempt == 3:
#                 print('Аккаунт заблокирован.')
#     else:
#         print("Такого пользователя нет в системе.")
# моя версия
st = 'Python - современный язык программирования! многие начинают изучать Python! Мы уже пишем код на Python!!!'
# text = text.strip()
# print(text.replace('Python', 'Java',3)) # заменяем питон на джава
# print(len(text))
# index = 0
#
# print(text.upper()) # сделать все буквы большими
#
# new_st = st.replace('Python', 'Java')
# new_st = new_st.replace('!', '') # (вырезать) удалить заменив на пробел или простоу удалить (можно просто убрать пробел оставить ''  без пробела
# print(new_st.upper()) # сделать все буквы большими
# print(len(st))
# print(len(st.replace(' ', ''))) # посчитать количество знаков без пробелов (удалив их реплэйс)
# print(len(st.split())) # посчитать количество слов по пробелам между ними (сплит)
# print(st.split()) # вывести слова отдельно каждому слову
# print(len(st.split()))
# print(len(st.replace('-', '').split()))
# мое решение
# while True:
#     password = input('Введите ваш пароль: ')
#     if len((password(>8)) and password.isdigit():
#         print('Доступ разрешен!')
# ИИ правки моего решения
# while True:
#     password = input('Введите ваш пароль: ')
#     has_upper = False
#     has_digit = False
#     for i in password: # проверяет посимолу пароль
#         if i.isupper(): # иметь букву верхнего регистра (проверка)
#             has_upper = True
#         if i.isdigit(): # иметь цифру (проверка)
#             has_digit = True
#     if has_upper and has_digit and len(password) > 8:
#         print('Пароль принят')
#         break
#     else:
#         print('Некоорректный пароль')

# while True:
#     password = input('Введите ваш пароль: ')
#     if len(password) > 8 and any(ch.isdigit() for ch in password):
#         print('Доступ разрешён!')
#         break
#     else:
#         print('Пароль не подходит: он должен быть длиннее 8 символов и содержать хотя бы одну цифру.')

# Задание - проверьте пароль: не меньше 8 символов, должна быть хотя бы одна заглавная буквы и цифра.
while True:
    password = input('Введите ваш пароль: ')

    has_upper = False
    has_digit = False # has  - иметь цифру
    for i in password:
        if i.isupper():
            has_upper = True
        if i.isdigit():
            has_digit = True
    if len(password) >= 8 and has_upper and has_digit:
        print('Пароль принят.')
        break
    else:
        print('Некорректный пароль.')






