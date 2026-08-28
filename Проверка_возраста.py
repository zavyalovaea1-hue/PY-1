# проверка возраста
# num = input("Введите ваш возраст: ")
#
# if num.isdigit():
#     age = int(num)
#     if age >= 18:
#         print("Доступ разрешен!")
#     else:
#         print("Доступ запрещен!")
# else:
#     print("Пожалуйста, введите корректное число.")

# age = int(input ('Введите ваш возраст: ')) # int переводит строку в числовые данные
# if age >=18:
#     print('Доступ разрешен.')
# else:
#     print ('Доступ запрещен.')

# снятие средств с банкомата, мой вариант
# amount = int(input('Введите сумму денег к выдаче: '))
# if amount <= 50000:
#     amount = 50000 - amount
#     print('Остаток средств: ', amount)
# else:
#     print('Недостаточно средств')

# снятие средств с банкомата, вариант преподавателя
# account = 1500
# yor_query = int(input('Введите сумму: '))
# if yor_query <= account:
#     result = account - yor_query
#     print('Заберите ваши деньги: ', yor_query)
#     print('Остаток на счете: ', result)
# else:
#     print('Недостаточно средств')

# мой вариант: суммирование или разность двух чисел по запросу пользвоателя (калькулятор)
# n = int(input('Введите первое число: '))
# n1 = int(input('Введите второе число: '))
# action = input('Введите действие + или -: ')
# if action == '+':
#     print(n + n1)
# else:
#     print(n - n1)

# # вариант преподавателя и мой вариант: суммирование или разность двух чисел по запросу пользвоателя (калькулятор)
# n1 = int(input('Введите первое число: '))
# n2 = int(input('Введите второе число: '))
# sign = input('Введите действие + или - или * или /: ')
# if n2 == '0'and sign == '/':
#     sign = input('Введите действие + или - или * или /: ')
#     print('Делить на ноль нельзя!')
# else:
#     res = n1 / n2
#     print(res)
# if sign == '+':
#     res = n1 + n2
# if sign == '-':
#     res = n1 - n2
# if sign == '*':
#     res = n1 * n2
# print(res)
# # if sign == '/':
# #     if n2 == '0':
# #         print('Делить на ноль нельзя!')
# #     else:
# #         res = n1 / n2
# #         print(res)

# задача с делением на ноль не решена!
# n1 = int(input('Введите первое число: '))
# n2 = int(input('Введите второе число: '))
# sign = input('Введите действие + или - или * или /: ')
# if sign == '+':
#     res = n1 + n2
# elif sign == '-':
#     res = n1 - n2
# elif sign == '*':
#     res = n1 * n2
# elif sign == '/':
#     if n2 ==0:
#         result = 'Деление на 0 запрещено'
#     else:
#         res = n1 / n2
# print(res)
# мой код - проверка логина и пароля на соответствие
# Login = 1111
# Password = 2222
# while True:
#     Login = input('Введите логин: ')
#     Password = input('Введите пароль: ')
#     if Login=='1111' and Password=='2222':
#         print('Доступ разрешен')
#         break
#     elif Login==1111 and Password==2222:
#         print('Ошибка, введите данные заново.')

# вариант преподавателя, проверка пароля и логина
# login = 'Student'
# password = '12345'
# while True:
#     your_login = input('Введите логин: ')
#     your_password = input('Введите пароль: ')
#     if your_login ==login and your_password ==password:
#         print('Доступ открыт')
#         break
#     else:
#         print('Ошибка')

login = 'Student'
password = '12345'
while True:
    your_login = input('Введите логин: ')
    your_password = input('Введите пароль: ')
    for your_password in range(3):
        if your_password == password:
            res = 'Доступ открыт'
    print(res)
    break
    elif your_login == login and your_password != password:
    cnt = cnt + 1
    if cnt == 3:
        print('Аккаунт заблокирован')
