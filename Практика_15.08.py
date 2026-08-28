# # Кинотеатр 10*15,
#
# hall = [[0 for place in range(3)] for row in range(2)] # создаем матрицу кинозала из списков
# for row in range(2): # проверяем свободно место или нет вложенным циклом
#     print(f'Ряд: {row + 1}') # счиатаем не с 0 места а с 1.
#     for place in range(3):
#         print(f'Место: {place + 1}')
#
#         if hall[row][place] == 0: # предлагаем бронирование места.
#             answer = input('Хотите забронировать? Введите да или нет: ')
#             if answer == 'да':
#                 hall [row][place] = 1
#
# count = 0
# for row in hall:
#     count += row.count(0) #
# print(f'Количество свободных мест: {count}')
# for row in hall:
#     print(row)
# import tkinter
# import tkinter import *
import tkinter as tk # импорт библиотеки ткинтер из тк. Можно as tk убрать, все равно будет работать.
# import numpy as np # короткко присваиваем имя библиотеке
# import pandas as pd

# win = tk.Tk() # привязвываем окно к тк интер
# win.geometry('600x400')  # задаем размер окна
# win.title('Рабочее окно') # даем имя окну
# # знакомимся с виджетами ткинтер
# label = tk.Label(win, text = 'Это лейбл!', font = ('Arial', 16)) # виджет лейбл. указать где создаем
# label.pack(pady = 50)  #проявить лейбл виджет в окне вин, пади 10 - сдвинуть надпись
# tk.mainloop()

# все функции пишем в верхней части окна, а виджеты в нижней
# def replace():
#     number.set(number.get() + 1)
#
# def replace1():
#     number.set(number.get() - 1)
#
# def print_entry():
#     print(entry.get()) # функция забирает данные из поля и печатает в консоль

#
#     # label.config(text = (+5)) # замена тек ста в кнопке
#     number.set(number.get() +5) # get записывает текущее значение переменной, set записывает новое значение и выводит

#
# win = tk.Tk() # привязвываем окно к тк интер
# win.geometry('600x400')  # задаем размер окна
# win.title('Рабочее окно') # даем имя окну
# number = tk.IntVar(value = 0)
# # знакомимся с виджетами ткинтер
# # label = tk.Label(win, text = 'Моя первая программа!', fg = 'darkblue', bg = 'lightblue', font = ('Arial', 16), height = 3, width = 20, anchor='w') # виджет лейбл. указать где создаем, анкор выравнивание текста по окну, принцип - север, юг, запад восток на англ языке
# frame1 = tk.Frame(win) # три внутренних окна - одно в вин и в нем два справа и слева
# frame1.pack()
# frame2 = tk.Frame(frame1)
# frame2.pack(side = 'left')
# frame3 = tk.Frame(frame2)
# frame3.pack(side = 'right')
# label = tk.Label(frame3, textvariable=number, fg = 'darkblue', bg = 'lightblue', font = ('Arial', 16), height = 3, width = 10, anchor='w') # виджет лейбл. указать где с
# label.pack(pady = 10) #проявить лейбл виджет в окне вин, (side = 'left') (padi = 10) пади 10 - сдвинуть надпись, bg цвет фона fg цвет надписи
#  # сайд - перемещение метки внутри текста
# button = tk.Button(frame2, text = 'Увеличить на 1', command=replace, width = 15, height = 1) # создаем кнопку. К кнопке нужно привязать команду
# button1 = tk.Button(frame2, text = 'Уменьшить на 1', command=replace1, width = 15, height = 1)
# # функция реплей пишется без скобок после нее, иначе функция будет обработана сразу без клика command=replace())
# button.pack(pady = 10)
# button1.pack(pady = 10)
#
# button2 = tk.Button(frame2, text = 'Вывод в консоль', command=print_entry, width = 15, height = 1) # создаем кнопку. К кнопке нужно привязать команду
# button2.pack(pady = 10)
# entry = tk.Entry(frame3, width = 40) # поле в которое можно вносить информацию, считать из этого поля
# entry.pack(pady = 10) # вывести поле
# print(entry.get())
# tk.mainloop()

# def show_info():
#     name = entry.get()
#     age = entry1.get()
#     print(f'Привет {name}, тебе {age} лет!')
#     l_result.config(text = f'Привет {name} тебе{age} лет!')
#
#
# win = tk.Tk()
# win.geometry('300x300')  # задаем размер окна
# win.title('Анкета') # даем имя окну
# label = tk.Label(win, text = 'Имя:', font = ('Times New Roman', 11), height = 1, width = 20) # виджет лейбл. указать где создаем, анкор выравнивание текста по окну, принцип - север, юг, запад восток на англ языке
# label.pack(pady = 5)
# entry = tk.Entry(width = 20) # поле в которое можно вносить информацию, считать из этого поля
# entry.pack(pady = 5) # вывести поле
# print(entry.get())
# label1 = tk.Label(win, text = 'Возраст:', font = ('Times New Roman', 11), height = 1, width = 20) # виджет лейбл. указать где создаем, анкор выравнивание текста по окну, принцип - север, юг, запад восток на англ языке
# label1.pack(pady = 5)
# entry1 = tk.Entry(width = 20) # поле в которое можно вносить информацию, считать из этого поля
# entry1.pack(pady = 5) # вывести поле
# button = tk.Button(win, text = 'Показать', command=show_info, width = 15, height = 1) # создаем кнопку. К кнопке нужно привязать команду
# button.pack(pady = 15)
#
# l_result = tk.Label(win)
# l_result.pack()
#
# tk.mainloop()

import random
#  НЕРАБОЧИЙ КОД (ИГРА КАМЕНЬ, НОЖНИЦЫ, БУМАГА)
# choices = {'ножницы':'бумага',
#            'бумага':'камень',
#            'камень':'ножницы'}
#
# win = tk.Tk()
# win.geometry('300x300')  # задаем размер окна
# win.title('Камень, ножницы, бумага') # даем имя окну
#
# l_result = tk.Label(win, text = 'Сделайте выбор', font = ('Arial', 12))
# l_result.pack()
#
# def play(user_choice):
#     comp_choice = random.choice(choices)
#
#     if user_choice == comp_choice:
#         result = 'Ничья!'
#     elif (user_choice == 'Камень' and comp_choice == 'Ножницы') or \
#         (user_choice == 'Ножницы' and comp_choice == 'Бумага') or \
#         (user_choice == 'Бумага' and comp_choice == 'Камень'):
#         result = 'Вы выиграли!'
#     else:
#         result = 'Вы проиграли!'
#     l_result.config(text = f'Вы {user_choice}\n Компьютер {comp_choice} \n(result)')
#
# def choice_button1():
#     play('Камень')
#
# def choice_button2():
#     play('Ножницы')
#
# def choice_button3():
#     play('Бумага')
#
# # label = tk.Label(win, text = 'Камень', font = ('Times New Roman', 11), height = 1, width = 20) # виджет лейбл. указать где создаем, анкор выравнивание текста по окну, принцип - север, юг, запад восток на англ языке
# # label.pack(pady = 20)
#
# l = tk.Label(win, text = 'Здесь будет результат')
# l.pack(pady = 5)
# button1 = tk.Button(win, text = 'Камень', command=choice_button1, width = 15, height = 1) # создаем кнопку. К кнопке нужно привязать команду
# button1.pack(pady = 15)
# button2 = tk.Button(win, text = 'Ножницы', command=choice_button2, width = 15, height = 1) # создаем кнопку. К кнопке нужно привязать команду
# button2.pack(pady = 15)
# button3 = tk.Button(win, text = 'Бумага', command=choice_button3, width = 15, height = 1) # создаем кнопку. К кнопке нужно привязать команду
# button3.pack(pady = 15)
# l_result = tk.Label(win)
# l_result.pack()
# tk.mainloop()


import tkinter as tk
import random

choices = ["Камень", "Ножницы", "Бумага"]

win = tk.Tk()
win.geometry("400x300")
win.title("Камень, ножницы, бумага")

result_label = tk.Label(win, text="Сделайте выбор", font=("Arial", 14))
result_label.pack(pady=10)


def play(user_choice):

    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "Ничья!"
    elif (user_choice == "Камень" and comp_choice == "Ножницы") or \
         (user_choice == "Ножницы" and comp_choice == "Бумага") or \
         (user_choice == "Бумага" and comp_choice == "Камень"):
        result = "Вы выиграли!"
    else:
        result = "Вы проиграли!"

result_label.config(
    text=f"Вы: {user_choice}\nКомпьютер: {comp_choice}\n{result}")

def choice_stone():

    play("камень")

def choice_paper():

    play("бумага")

def choice_scissors():

    play("ножницы")


l = tk.Label(win, text = "")
l.pack(pady= 30)

b_stone = tk.Button(win, text = "Камень", width=20, command=choice_stone)
b_stone.pack(pady = 5)

b_paper = tk.Button(win, text = "Бумага", width=20, command=choice_paper)
b_paper.pack(pady = 5)


b_scissors = tk.Button(win, text = "Ножницы", width=20, command=choice_scissors)
b_scissors.pack(pady = 5)


tk.mainloop()



