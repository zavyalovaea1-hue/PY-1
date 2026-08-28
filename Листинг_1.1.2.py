# import turtle
# turtle.forward(100) #движение вперед на 100 пикселей
import turtle
# turtle.shape("turtle") # что такое shape? в листинге написано форма курсора
# turtle.forward(100)

# turtle.left(120)
# turtle.fd(100)
# turtle.left(120)
# turtle.fd(100)
# turtle.left(120) # рисуем треугольник с поворотом налево на 120 градусов

# turtle.left(90) # рисуем квадрат по 90 гардусов налево, 4 стороны
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)

# for i in range(4):
#     turtle.fd(100)
#     turtle.left(90) # цикл
#
# print (range(4)) # печатем диапазон

# for i in range(4): # печатем значение переменной в цикле (всегда начинается с 0)
#     turtle.fd(100)
#     turtle.left(90)
#     print(i)

# for i in range(3): # цикл для треугольника
#     turtle.fd(100)
#     turtle.left(120)

# Ugol = 3 # используем переменную количество углов
# turtle.shape("turtle")
# for i in range(Ugol):
#     turtle.fd(100)
#     turtle.left(360/Ugol)

# Ugol = 5 # рисуем пятиугольник
# turtle.shape("turtle")
# for i in range(Ugol):
#     turtle.fd(100)
#     turtle.left(360/Ugol)

# Ugol = 6 # рисуем шестиугольник
# turtle.shape("turtle")
# for i in range(Ugol):
#     turtle.fd(100)
#     turtle.left(360/Ugol)

# Ugol = 5 # закрашиваем фигуру цветом черепахи
# turtle.begin_fill()
# turtle.shape("turtle")
# for i in range(Ugol):
#     turtle.fd(100)
#     turtle.left(360/Ugol)
# turtle.end_fill()

# Ugol = input('Введите количество углов фигуры')
# Ugol = int(Ugol)
# turtle.color('green')
# turtle.begin_fill()
# turtle.shape("turtle")
# for i in range(Ugol):
#     turtle.fd(100)
#     turtle.left(360/Ugol)
# turtle.end_fill() # Зеленый многоугольник

# Ugol = input('Введите количество углов фигуры: ')
# Ugol = int(Ugol)
# Color = input ('Введите цвет на английском языке: ')
# turtle.color(Color)
# turtle.begin_fill()
# turtle.shape('turtle')
# for i in range(Ugol):
#     turtle.forward(100)
#     turtle.left(360/Ugol)
# turtle.end_fill()  # вводим углы и цвет с клавиатуры

# Ugol = 5 # Рисуем перевернутую пятиугольную звезду
# turtle.shape('turtle')
# turtle.begin_fill()
# for i in range(Ugol):
#     turtle.forward(100)
#     turtle.left(360*2/Ugol)
# turtle.end_fill()

# Ugol = 5 # Рисуем пятиконечную звезду
# turtle.begin_fill()
# for i in range(Ugol):
#     turtle.forward(100)
#     turtle.right(360*2/Ugol)
# turtle.end_fill()

# Ugol = 5 # рисуем красную звезду
# turtle.begin_fill()
# turtle.color("red")
# turtle.width(3)
# for i in range(Ugol):
#     turtle.forward(100)
#     turtle.right(360*2/Ugol)
# turtle.end_fill()

# Ugol = 7 # рисуем 7 -конечную звезду
# turtle.begin_fill()
# turtle.color("pink", "purple")
# for i in range(Ugol):
#     turtle.forward(100)
#     turtle.right(360*2/Ugol)
# turtle.end_fill()
#
# Ugol = 7 # рисуем 7 -конечную звезду
# turtle.begin_fill()
# turtle.color("pink", "purple")
# for i in range(Ugol):
#     turtle.forward(100)
#     turtle.right(360*3/Ugol)
# turtle.end_fill()

Ugol = 9 # три вида 9-угольных звезд
turtle.color('yellow')
turtle.begin_fill()
for i in range(Ugol):
    turtle.forward(200)
    turtle.right(360*4/Ugol)
turtle.end_fill()
# import turtle
# import turtle as t

# turtle.circle(50)
# t.circle(50)
# import turtle
# import turtle as t
# t.color ('purple') # цвет текстом
# t.circle(100)

# from turtle import * # формат цвета в РГБ
# colormode(255)
# import turtle as t
# t.color(255, 127, 80) # цвет в формате РГБ
# t.circle(100)

# from turtle import * # заливка фигуры
# colormode(255)
# import turtle as t
# t.begin_fill()
# t.color(255, 127, 80)
# t.circle(100)
# t.end_fill()

# from turtle import * # заливка фигуры
# colormode(255)
# import turtle as t
# t.begin_fill()
# t.color(255, 127, 80)
# t.circle(100)
# t.end_fill()
# t.fd(50)
# t.begin_fill()
# t.color(255, 160, 220)
# t.circle(100)
# t.end_fill()

# from turtle import * # три круга разного цвета рядом
# import turtle as t # поднимаем и опускаем перо
# colormode(255)
# turtle.begin_fill()
# t.color(255, 127, 80)
# t.circle(100)
# t.end_fill()
# t.penup()
# t.fd(100)
# t.pendown()
# t.begin_fill()
# t.color(255, 160, 22)
# t.circle(100)
# t.end_fill()
# t.penup()
# t.fd(100)
# t.pendown()
# t.begin_fill()
# t.color(255, 160, 22)
# t.circle(100)
# t.end_fill()

# from turtle import * # три круга при помощи цикла
# import turtle as t # поднимаем и опускаем перо
# colormode(255)
# for i in range(3):
#     turtle.begin_fill()
#     t.color(255, 127, 80)
#     t.circle(100)
#     t.end_fill()
#     t.penup()
#     t.fd(100)
#     t.pendown()

# from turtle import * # три круга при помощи цикла  поворотом 120
# import turtle as t # поднимаем и опускаем перо
# colormode(255)
# import turtle as t
# for i in range(3):
#     turtle.begin_fill()
#     t.color(255, 127, 80)
#     t.circle(100)
#     t.end_fill()
#     t.penup()
#     t.fd(50)
#     t.left(120)
#     t.pendown()

# from turtle import * # четыре круга при помощи цикла
# import turtle as t # поднимаем и опускаем перо
# colormode(255)
# import turtle as t
# for i in range(4):
#     turtle.begin_fill()
#     t.color(255, 127, 80)
#     t.circle(100)
#     t.end_fill()
#     t.penup()
#     t.fd(50)
#     t.left(90)
#     t.pendown()

from turtle import * # три круга при помощи цикла
import turtle as t # поднимаем и опускаем перо
colormode(255)
import turtle as t
# for i in range(4):
#     turtle.begin_fill()
#     t.color(60*i, 60*i, 60*i)
#     i +=10
#     t.circle(20)
#     t.end_fill()
#     t.penup()
#     t.fd(50)
#     t.left(90)
#     t.pendown()
# t.color('red')
# t.rt(60)
# for i in range (6, 100, 12):
#     t.forward(i)
#     t.rt(120)
#





























