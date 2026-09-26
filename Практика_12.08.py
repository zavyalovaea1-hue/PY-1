from turtle import *
from time import sleep #оставновка черепашки
from random import randint
from datetime import datetime
# w = 300 # игра в черепашку (пойма черепашку), ширина
# h = 300 # высота
#
# penup()
# goto(-300, -300)
# pendown()
# color('lightgreen')
# begin_fill()
# for i in range(4):
#     fd(w*2)
#     left(90)
# end_fill()
#
# t1 = Turtle()
# t1.color('red')
# t1.shape('turtle')
# t1.width(5)
#
# def catcht1():
#     t1.penup()
#     t1.goto(randint(-300, 300),randint(-300, 300))
#     t1.pendown()
#     t1.left(randint(0, 180))
#
#
# def gameFinished(t1):
#     t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h # возвращаем черепашку в игровое поле, если она за него выходит
#     return t1_outside
#
# t1.onclick(catcht1)
# # t1.onclick(catcht1) # нажимаем на черепашку и запускается функция сатчт1 (поймать)
# while gameFinished(t1) != True:
#     t1.forward(7)
#     sleep(0.1) #0,1 секунды
#
# t1.clear()
# t1.penup()
# t1.goto(-50, 0)
# t1.write("Игра окончена!", font=('Times New Roman', 24)) # врайт - надпись и ее координаты по центру. , фонт - шрифт
# t1.hideturtle() # убрать черепашку
#
# mainloop()

w = 300 # игра в черепашку (поймай черепашку), ширина
h = 300 # высота

penup()
goto(-300, -300)
pendown()
color('lightgreen')
begin_fill()
for i in range(4):
    fd(w*2)
    left(90)
end_fill()

t1 = Turtle()
t1.shapesize(stretch_wid=3, stretch_len=3, outline=2)  # ширина, длина, толщина контура
t1.color('red')
t1.shape('turtle')
t1.width(5)

t2 = Turtle()
t2.shapesize(stretch_wid=3, stretch_len=3, outline=2)  # ширина, длина, толщина контура
t2.color('green')
t2.shape('turtle')
t2.width(5)
t2.left(120) # задать угол поворота черепашке 120 градусов

t3 = Turtle()
t3.shapesize(stretch_wid=3, stretch_len=3, outline=2)  # ширина, длина, толщина контура
t3.color('yellow')
t3.shape('turtle')
t3.width(5)
t3.left(240)

def catcht1(x, y):
    t1.penup()
    t1.goto(randint(-300, 300),randint(-300, 300))
    t1.pendown()
    t1.left(randint(0, 180))
def catcht2(x, y):
    t2.penup()
    t2.goto(randint(-300, 300), randint(-300, 300))
    t2.pendown()
    t2.left(randint(0, 180))
def catcht3(x, y):
    t3.penup()
    t3.goto(randint(-300, 300), randint(-300, 300))
    t3.pendown()
    t3.left(randint(0, 180))

def gameFinished(t1, t2, t3):
    t1_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h # возвращаем черепашку в игровое поле, если она за него выходит
    t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h # возвращаем черепашку в игровое поле, если она за него выходит
    t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h # возвращаем черепашку в игровое поле, если она за него выходит
    t_outside = t1_outside or t2_outside or t3_outside
    return t_outside


t1.onclick(catcht1) # нажимаем на черепашку и запускается функция сатчт1 (поймать)
t2.onclick(catcht2) # нажимаем на черепашку и запускается функция сатчт1 (поймать)
t3.onclick(catcht3) # нажимаем на черепашку и запускается функция сатчт1 (поймать)
while gameFinished(t1, t2, t3) != True:
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1) #0,1 секунды

t1.clear()
t2.clear()
t3.clear()
t1.penup()
t2.penup()
t3.penup()
t1.goto(-50, 0)
t2.goto(-50, 0)
t3.goto(-50, 0)
t1.write("Игра окончена!", font=('Times New Roman', 24)) # врайт - надпись и ее координаты по центру. , фонт - шрифт
t2.write("Игра окончена!", font=('Times New Roman', 24))
t3.write("Игра окончена!", font=('Times New Roman', 24))
t1.hideturtle() # убрать черепашку
t2.hideturtle() # убрать черепашку
t3.hideturtle() # убрать черепашку

mainloop()

# count_info = 0
# count_error = 0
# count_warning = 0
#
# dates = []
# with open(r'C:\Users\Катя\Desktop\log.txt', 'r', encoding='utf-8') as file:
#
# with open(r'C:\Users\Катя\Desktop\log.txt','r',encoding='utf-8') as file: # ссылка на файл, два варианта записи: с одним слешем и буквой р
#
#     # буква р после адреса, говорит о том, что файл открывается на рид чтение. если на запись, то там будет стоять даблю
# # with open('C:\\Users\\Катя\\Desktop\\log.txt',encoding='utf-8') as file: # с двумя слешами и без буквы р в начале
#
#
#     for line in file: # представить файл по строкам
#         print(line) # вывести на печать строки
#         parts = line.split()
#         # dates.append(parts[0])
#         print(dates)
#
#         # print(parts[0]) # вычленяем дату и время
#         print(parts)
#         # print(parts[1])  # индекс 1, так как нулевой индекс дата, 1 индекс инфо, эррор, варнинг
#
#         dates.append(datetime.strptime(parts[0], '%Y-%m-%d'))
#         # if parts[1] == 'INFO':
#         #     count_info += 1
#         #     print(count_info)
#         # elif line.split()[1] == 'ERROR':
#         #     count_error += 1
#         #     print(count_error)
#         # elif line.split()[1] == 'WARNING':
#         #     count_warning += 1
#         #     print(count_warning)
# min_date = min(dates).day # выводит минимальную дату без месяца и года
# max_date = max(dates).day # выводит максимальную дату без месяца и года
# # print(f'Количество ошибок ИНФО: {count_info}')
# # print(f'Количество ошибок ЕРРОР: {count_error}')
# # print(f'Количество ошибок ВАРНИНГ: {count_warning}')
# print(f'Минимальная дата {min_date}')
# print(f'Максимальная дата {max_date}')
# print(f'Разница:| {max_date-min_date} дней') # вычитаем числа (даты)
#
# print(max(dates), min(dates))
#  # строки не удастся вычесть и посчитать разницу в датах по заданию
#
# def process_list(lst):
#     try:
#
#     # if not isinstance(lst, list): # проверка является ли списком
#     #     print('Ошибка: аргумент не является списком')
#
#         new_lst = []
#         for i in lst:
#             if i % 2 == 0:
#                 new_lst.append(i**2)
#             else:
#                 new_lst.append(i**3)
#         return new_lst
#     except Exception as e: #проверка на ошибку и замена сообщение ноне
#         print(f'Ошибка: {e}')
#
# print(process_list('bhghghghg'))
#
#     # if not isinstance(lst, list): # проверка является ли списком
#     #     print('Ошибка: аргумент не является списком')
# def process_list(lst):
#
#         new_lst = [i**2 if i % 2 == 0 else i**3 for i in lst] # записываем тоже самое одной строкой через СПИСОКОВЕ ВКЛЮЧЕНИЕ
#         return new_lst
#
# print(process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#
# lst = [1,2,3,4,5,6,7,8,9,0] # создаем тоже но не через функцию, а через лямбда
# new_lst = list(map(lambda i: i ** 2 if i % 2 == 0 else i ** 3, lst)) # лямбда используется всего 1 раз, с условием что мы ее больше нигде в программе использовать не будем
# print(new_lst)
#
#
# def process_list(lst):
#     new_lst = [i ** 2 if i % 2 == 0 else i ** 3 for i in
#                lst]  # записываем тоже самое одной строкой через СПИСОКОВЕ ВКЛЮЧЕНИЕ
#     return new_lst
#
#
# print(process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # создаем тоже но не через функцию, а через лямбда
# new_lst = list(map(lambda i: i ** 2 if i % 2 == 0 else i ** 3,
#                    lst))  # лямбда используется всего 1 раз, с условием что мы ее больше нигде в программе использовать не будем
# print(new_lst)
#
# def process_list(lst):
#
#         new_lst = [i**2 if i % 2 == 0 else i**3 for i in lst] # для каждого элемента списка лст
#         # for i in lst:
#         #         if i % 2 == 0:
#         #                 new_lst.append(i**2)
#         #         else:
#         #                 new_lst.append(i**3)
#         return new_lst
#
#         # new_lst = [i**2 if i % 2 == 0 else i**3 for i in lst] # записываем тоже самое одной строкой через СПИСОКОВЕ ВКЛЮЧЕНИЕ
#         # return new_lst
#
# print(process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#
# lst = [1,2,3,4,5,6,7,8,9,0] # создаем тоже но не через функцию, а через лямбда
# new_lst = list(map(lambda i: i ** 2 if i % 2 == 0 else i ** 3, lst)) # лямбда используется всего 1 раз, с условием что мы ее больше нигде в программе использовать не будем
# print(new_lst) № # мэп - для каждого элемента в списке лст, вместо фор
#
# def process_list(lst):
#         if isinstance(lst, list): # если аргумент является списком.,  то
#                 new_lst = []
#                 for i in lst:
#                         if i % 2 == 0:
#                                 new_lst.append(i ** 2)
#                         else:
#                                 new_lst.append(i ** 3)
#                 return new_lst
#         else:
#                 print('Ошибка: аргумент не является списком')
#
#
# print(process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#
#         # new_lst = [i**2 if i % 2 == 0 else i**3 for i in lst] # для каждого элемента списка лст
#         # # for i in lst:
#         # #         if i % 2 == 0:
#         # #                 new_lst.append(i**2)
#         # #         else:
#         # #                 new_lst.append(i**3)
#         # return new_lst
#
#         # new_lst = [i**2 if i % 2 == 0 else i**3 for i in lst] # записываем тоже самое одной строкой через СПИСОКОВЕ ВКЛЮЧЕНИЕ
#         # return new_lst
#
# print(process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))







