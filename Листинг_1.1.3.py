# t.pensize(3)
# t.color('red')
# t.rt(60)
# for i in range(4, 80, 4):
#     t.fd(i)
# #     t.rt(60)
# from turtle import * # три круга при помощи цикла
# import turtle as t # поднимаем и опускаем перо
# colormode(255)
# t.ht()
# t.pensize(4)
# t.color('blue')
# for i in range(4, 56, 4):
#     t.forward(i)
#     t.left(90)
import string

# t.ht()
# t.pensize(4) # команда: ширина пера
# t.color('blue')
# for i in range(56, 4, -4):
#     t.fd(i)
#     t.rt(90)

#

# r=40
# t.pensize(5)
# t.color("#FFA500")
# for i in range(6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)

# r=40
# t.pensize(10)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for i in range(6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)
# r=30
# for i in range(6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)
# r=20
# for i in range(6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)
# r=10
# for i in range(6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)

# r=40 # вложенные циклы
# t.pensize(10)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for j in range(4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r=r-10

# r=20 # три вложенных цикла подряд
# t.pensize(4)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for i in range(4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r=r-5
# t.pu()
# t.fd(80)
# t.pd()
# r = 20
# for j in range(4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r=r-5
# t.pu()
# t.fd(80)
# t.pd()
# r = 20
# for j in range(4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r=r-5

# import turtle as t
#
# t.pensize(4) # тройное вложение циклов
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for k in range(3):
#   r = 20
#   for j in range(4):
#     for i in range(6):
#       t.begin_fill()
#       t.circle(r)
#       t.end_fill()
#       t.rt(60)
#     r = r - 5
#   t.pu()
#   t.fd(80)
#   t.pd()

# import turtle as t
# import time # вводим время

# t.pensize(4)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for k in range(3):
#   print("!___k = " + str(k))
#   r = 20
#   for j in range(4):
#     print("__j = " + str(j))
#     for i in range(6):
#       print("i = " + str(i))
#       t.begin_fill()
#       t.circle(r)
#       t.end_fill()
#       t.rt(60)
#       time.sleep(1) # пауза, ожидание 1 секунда
#     r = r - 5
#     print("Следующие 6")
#   t.pu()
#   t.fd(80)
#   t.pd()
#   print("Цветок готов!")

# import turtle as t # вводим диапазон range
# print(range(40, 0, -10))
# t.speed(50)
# range(40)
# t.pensize(10)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for j in range(40, 0, -10):
#   for i in range(6):
#     t.begin_fill()
#     t.circle(j)
#     t.end_fill()
#     t.rt(60)

# import turtle as t # эксперимент с цветами
# r = 40
# t.pensize(10)
# t.color(255, 165, 0)
# t.fillcolor(162, 0, 255)
# for j in range(4):
#   for i in range(6):
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)
#   r = r - 10

# import turtle as t
#
# t.pensize(10)
# t.color(255, 165, 0)
# t.fillcolor(162, 0, 255)
# for j in range(40, 0, -10):
#   for i in range(6):
#     t.begin_fill()
#     t.circle(j)
#     t.end_fill()
#     t.rt(60)

# import turtle as t
#
# t.ht()
# t.pensize(5)
# for r in range(40, 0, -10):
#   for i in range(6):
#     t.color(255, 165, r * 6)
#     t.fillcolor(162, r * 5, 255)
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     t.rt(60)

# Name = input ('Введите имя')
# print(Name[0]) # - первая буква имени
# print(Name[1])
# print(Name[2])
# print(Name[3])
# print(Name[-1]) # - последняя буква имени
# print(Name[-2]) # - предпоследняя буква имени
# print(Name[-3])

text = "Пример текстовой строки"
s = text [8:15]
print(s)

text = "Phyton - это круто!"
s = text [-7:-2]
print(s)

text = "Привет, как дела?!"
s = text [:6]
print(s)

text = "Это последние символы!"
s = text [-5:]
print(s)

# text = "12345678"
# s = text [::2] # :: - срез
# print(s)

# text = "Аргентина манит негра" # не решено!!!!
# s = string [::-1] # :: - срез

text = "Разделить строку"
x = 9
p_1 = text[:x]
p_2 = text[x:]
print(p_1, p_2)











