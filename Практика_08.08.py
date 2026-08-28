"""СТРУКТУРА ДАННЫХ ПИТОН, КООРДИНАТНАЯ СИСТЕМА, ПРИМЕНЕНИЕ ЦИКЛИЧЕСКИХ И ЛИНЕЙНЫХ АЛГОРИТМОВ И СОЗДАНИЕ ФУНКЦИЙ"""
"""Дана строка: Иванов Иван Иванович, email ivanovii@example.com, тел: +7(912)345-67-89, адрес: ул. ленина, дом. 15, кв. 200"""
# практика. мой код
# str  = "Иванов Иван Иванович, email: ivanovii@example.com, тел: +7(912)345-67-89, адрес: ул. Ленина, дом. 15, кв. 200"
# print('Пользователь: ', str[:6],str[7: 8],str[12:13])
# d = {'email':'ivanovii@example.com', 'тел': '+7(912)345-67-89', 'адрес': 'ул. Ленина, дом. 15, кв. 200'}
# print('майл: ', d['email'])
# print('Тел: ', d['тел'])
# print('Адрес проживания: ', d['адрес'])
#
# # решение Алисы АИ (вычленение домена и имени емайла)
# s = "Иванов Иван Иванович, email: ivanovii@example.com, тел: +7(912)345-67-89, адрес: ул. Ленина, дом. 15, кв. 200"
#
# parts = s.split(', ')
#
# name = parts[0]                         # "Иванов Иван Иванович"
# email_part = parts[1]                   # "email: ivanovii@example.com"
# email = email_part.split(': ')[1]       # "ivanovii@example.com"
# domain = email.split('@')[1]            # "example.com"
#
# print("Имя:", name)
# print("Email:", email)
# print("Домен:", domain)
#
# #решение преподавателя, решаем через строку, разбиваем по пробелму с запятыми
# st = "Иванов Иван Иванович, email: ivanovii@example.com, тел: +7(912)345-67-89, адрес: ул. Ленина, дом. 15, кв. 200"
# fio = st.split(',')[0] # ИНДЕКСАЦИЯ СПИСКА, НУЛЕВОЙ ЭЛЕМЕНТ - ИВАНОВ ИВАН ИВАНОВИЧ
# # print(fio)
#
# surname = fio.split()[0]
# name = fio.split()[1][0] # ВЫВОД ИНИЦИАЛОВ! 1 слово первого слова списка, нулевая буква И (выводит инициал)
# patronymic = fio.split()[2][0]
# print(surname, name, patronymic)
# # ИЛИ:
# # print(surname)
# # print(name)
# # print(patronymic)
# print(f'{surname} {name} {patronymic}')
# # мой вариант (разбить на имя пользователя и домен)
# email = st.split(' ')[4] # ВЫДЕЛИТЬ ЕМАЙЛ ИЗ СПИСКА
# print(email)
# domain = email[9:20]
# print(domain)
# fio1 = email[:8]
# print(fio1)
#
# # вариант преподавателя
# email = st.split(',')[1].strip() # СТРИП УДАЛЯЕТ ЛИШНИЕ ПРОБЕЛЫ. бЕРЕТСЯ ЕМАЙЛ 1 ЗНАЧЕНИЕ В СПИСКЕ
# email = email.split(':')[1].strip() # БЕРЕТСЯ САМ ЕМАЙЛ, БЕЗ ОБОЗНАЧЕНИЯ EMAIL
# email1 = email.split('@')
# email_name = email1[0]
# email_domain = email1[1]
# print(email_name, email_domain)
# # мой вариант
# tel = st.split(',')[2]
# print(tel)
# tel = tel.split(':')[1]
# print(tel)
#
# # вариант преподавателя, вывод ф строки мой
# tel = st.split(',')[2]
# tel = tel.split(':')[1].strip()
# print(tel)
# adress = st.split(':')[3].strip()
# print(adress)
# print(f'{'Пользователь:'} {surname} {name} {patronymic}')
# print(f'{'Email:'} {email} {"Домен:"} {email_domain} {"имя:"} {email_name}')
# print(f'{"Телефон:"} {tel}')
# print(f'{'Адрес:'} {adress}')

# мое решение:
# numbers = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]
# numbers1 = numbers[0::2] # вывести каждый второй элемент, начиная с первогог
# print(numbers1)
# numbers2 = numbers[::-1] # вывести список в обратном направлении, не используя метод реверс
# print(numbers2)
# # while numbers[]/3(int)==0:
# #     print(numbers)
# # else:
# #     print("Нет подходящих значений")
#
# new_numbers = [] # выводим список чисел днеелящихся на 3 без остатка
# for i in numbers: # ай часть списка намбрс
#     if i % 3 !=0: # если ай переменная делится на 3 и не равно 0 (не делится без остатка), то
#         new_numbers.append(i) # добавляем в списко
# print(new_numbers)
# # тоже самое, но по-другому через лист компрехеншен
# new_num = [i for i in numbers if i % 3 == 0] # ай для ай из списка намбрс если делится на 3 без остатка, то:
# print(new_num)
#
# # Исходный список
# # Количество элементов
# # Четные числа
# # Нечетные числа
# # Максимальное значение
# # Минимальное значение
# # Среднее значение
# # Отсортированный список
# # Список наоборот
#
# print(f'{'Исходный список:'} {numbers}')
# print(f'{'Количество элементов:'} {len(numbers)}')
# numbers3 = [j for j in numbers if j % 2 == 0]
# print(f'{'Четные числа:'} {numbers3}')
# numbers4 = [k for k in numbers if k % 2 != 0]
# print(f'{'Нечетные числа:'} {numbers4}')
# print(f'{'Максимальное значение:'} {max(numbers)}') # самое большое значение
# print(f'{'Минимальное значение:'} {min(numbers)}')
# print(f'{'Среднее значение:'} {round(sum(numbers)/len(numbers),2)}') # раунд - округляем до двух знаков после запятой
# # print(f'{'Отсортированный список:'} {numbers.sort()}')
# # print(f'{'Список наоборот:'} {numbers.reverse()}')
# numbers.sort()
# # функция sorted можно использовать для списка, создает новый список, sort сортирует тот который есть список
# print(sorted(numbers))
# print('Отсортированный список:', numbers)
# print('Список наоборот:', numbers[::-1])

# numbers = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]
# st = "Hello world!" # для строки сорт не доступен, только для чисел.
# print(numbers) # метод (метод к строе не привязан, отдельно живет)
# print(sorted(numbers)) # функция привязана
# print(sorted(st)) # функция привязана, может использоваться для структуры список. Для строки сорт и сортед не применяется, только вот так

# fruits = ('яблоко', 'банан', 'груша', 'апельсин', 'банан', 'киви', 'банан', 'слива')
# print(fruits.index('банан'))
# cnt = 0
#
# # ИИшный ответ:
#
# cnt = fruits.count('банан')
# print(cnt)
#
# # краткая запись преподавателя:
#
# print(fruits.count('банан'))
#
# fruits = ('яблоко', 'банан', 'груша', 'апельсин', 'банан', 'киви', 'банан', 'слива')
# cnt = 0
# for i in fruits:
#     if i == 'банан':
#         cnt += 1
# print(cnt)
#
# fruits = ('яблоко', 'банан', 'груша', 'апельсин', 'банан', 'киви', 'банан', 'слива')
# cnt = sum(1 for i in fruits if i == 'банан') # КРАТКАЯ ФУНКЦИЯ, ЗАПИСЬ. суммировать 1, для ай из кортежа фрюит, если ай - банан
# print(cnt)
#
# new_num = [] # создаем новый список. Этот метод больше подходит для чисел, для списков
# for i in fruits:
#     new_num.append(i) # переменная списка печатается первый раз
#     new_num.append(i) # и второй раз
# print(new_num)
#
# new_fruits = () # для кортежа такой вариант не работает
# for j in fruits:
#     new_num.append(j)  # переменная списка печатается первый раз
#     new_num.append(j)  # и второй раз
# print(new_fruits)
#
# # new_fruits = () # ОШИБКА! ДЕМОНСТРАЦИЯ ОШИБКИ. для кортежа такой вариант не работает
# # for j in fruits:
# #     new_fruits +=(j)  # переменная списка печатается первый раз
# # print(new_fruits) # воспринимает как строку
#
# new_fruits = () # для кортежа такой вариант не работает
# for j in fruits:
#     new_fruits +=(j,j)  # пишем значение с запятой (признак кортежа) и добавляем еще джей.
# print(new_fruits) # к кортежу добавить строку нельзя, к кортежу можно добавить только кортеж. Он не изменяет его, а пересоздает

# set1 = {2, 4, 6, 8, 10, 12}
# set2 = {6, 8, 10, 14, 16, 18}
#
# res = set1 & set2 # выявляет пересечение
# print(res)
# res = set1 | set2 # проводит объединение
# print(res)
# res = set1 - set2
# print(res)
# print(set1.issubset(set2))

# d = {'Иван':[5, 4, 5], 'Петр': [3, 4, 4], 'Мария': [5, 5, 4], 'Ольга': [4, 5, 5]}
# d1 = {'Елена':[5, 4, 5], 'Дмитрий':[4, 3, 3], 'Сергей':[5, 5, 5]}
# print(d) # метод эппенд здесь не работает!!!
# d['Анна'] = [5, 5, 5] # метод замены значения в словаре
# print(d)
#
# del d['Петр'] # функция дел (удалить)
# print(d)
# d.update(d1) # обновить d списком d1, добавить, соединяем 2 словаря
# print(d1)
# for key, value in d.items(): # можно указывать для словаря ключ и величину или dictionary  словарь, будет встречаться и то, и другое
#     print(key) # получается список из имен
#     average = round(sum(value) / len(value), 2) # считаем среднее арифметическое
#     print(key, average) # печатаем одновременно имя и среднее арифметическое
#
# import random
# n = random.randint(1, 100)
# print(n)
# cnt = 0
# while True:
#     s = int(input('Угадайте рандомное число в пределах от 1 до 100: '))
#     cnt = cnt + 1
#     if s == n:
#         print('Поздравляю, вы угадали число c', {cnt}, 'попыток!')
#         break
#     elif s < n:
#         print('Больше!')
#     elif s > n:
#         print('Меньше!')

# посчитать все гласные, согласные, цифры и какой символ встречается чаще всего.
# vowels = 'а, е, ё, и, о, у, ы, э, ю, я'
# vowels = [i.strip() for i in vowels.split(',')] # содержится ли введеная буква в этом списке, для этого создается новый список
# print(vowels)
# st = input("Введите строку: ")
# count_vowels = 0
# # cont_vowels = count_vowels+1
# count_consonant = 0
# count_digit = 0
# for i in st: # i итерация по гласным символам
#     if i != ' ':
#         if i in vowels:
#             print(i)
#             count_vowels += 1
#         elif i.isalpha():
#             count_consonant += 1
#         elif i.isdigit():
#             count_digit +=1
# print(count_vowels)
# print(count_consonant)
# print(count_digit)
# max_count = 0
# max_ch = ''
# count = 0
#
# for i in st:
#     if i !=' ':
#         count=st.count(i)
#     # count = st.count(i)
#     # print(i, count)
#         if count > max_count: # метод каунт считает символы в строк ст
#             max_count = count
#             max_ch = i
# print(f'Самый часто встречающийся символ {max_ch} встречается {max_count} раз(а)')

from turtle import * # черепашка стартует из позиции (0, 0).
def draw_landscape():
    penup()
    goto(-300, -200) # двигаем черепашку
    pendown()
    color('lightgreen')
    begin_fill()
    for i in range(2):
        fd(600)
        left(90)
        fd(150)
        left(90)
    end_fill()
draw_landscape() # функцию надо вызвать - отрисовать прямоугольник - объявляем функцию в начале, вывзаем в конце

def draw_sky():
    penup()
    left(90) # двигаем черепашку
    fd(150)
    pendown()
    color('lightblue')
    begin_fill()
    for i in range(1):
        right(90)
        fd(600)
        left(90)
        fd(300)
        left(90)
        fd(600)
        left(90)
        fd(300)
    end_fill()
draw_sky() # функцию надо вызвать - отрисовать прямоугольник - объявляем функцию в начале, вывзаем в конце
def draw_sun():
    penup()
    goto(200, 200)
    pendown()
    begin_fill()
    color('orange', 'yellow')
    for i in range(18):
        forward(40)
        left(100)
    end_fill()
draw_sun() # функцию

# color('yellow')
# begin_fill()
# for i in range(4):
# fd(15)
# left(90)
# end_fill()

def draw_window():
    color('yellow')
    begin_fill()
    for i in range(4):
        fd(20)
        left(90)
    end_fill()

def draw_block_of_flats():
    penup()
    goto(-170, -170)
    pendown()
    color('black', 'grey')
    begin_fill()
    for i in range(4):
        fd(100)
        left(90)
        fd(200)
        left(90)
    end_fill()
penup()
goto(-170, -170)
pendown()
color('grey')
begin_fill()
for i in range(2):
    left(90)
    fd(100)
    left(90)
    fd(200)
end_fill()
for row in range(6):
    penup()
    goto(-145, -145 + row * 30)
    print(xcor(), ycor())
    pendown()
    draw_window()
    for new in range(1):
        penup()
        goto(-115, -145 + row * 30)
        print(xcor(), ycor())
        pendown()
        draw_window()


exitonclick() # вызывает рабочее окно из библиотеки тертл



















