# Нарисуйте три разных круга, используя разные цвета и радиусы, используя модуль turtle. Для каждого круга используйте begin_fill(), color(), circle() и end_fill().
# Сохраните файл с проектом на компьютер.
# при выполнение задании внутри бегин фил должно быть действие (серкл 40), а перед филлколор и колор  - цвета
# import turtle
from turtle import *
shape('turtle') # курсор в виде черепахи
colormode(255)
pensize(4)
fillcolor((242, 245, 39))
color('blue')
begin_fill()
circle(40)
end_fill()
penup()
fd(100)
pendown()
fillcolor((218, 203, 15))
color('green')
begin_fill()
circle(50)
end_fill()
penup()
fd(150)
pendown()
fillcolor((203, 105, 39))
color('yellow')
begin_fill()
circle(60)
end_fill()
penup()
speed(50)
mainloop()








