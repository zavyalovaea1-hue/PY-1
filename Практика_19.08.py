# from tkinter import *
# import tkinterweb
#
# window=Tk()
# frame = tkinterweb.HtmlFrame(window)
# frame.load_website("https://www.google.com")
# frame.pack(fill="both", expand=1)
# window.mainloop()
#
# from tkinter import *
# import tkinterweb
#
#
# def read():
#     Site = e.get()
#     frame.load_website(Site)
#
#
# window = Tk()
# m = Label(text="введите адрес сайта:")
# m.pack()
# e = Entry(width=20, justify='left')
# e.pack()
# b = Button(text="Ввод", command=read)
# b.pack()
# frame = tkinterweb.HtmlFrame(window)
#
# frame.pack(fill="both", expand=1)
# window.mainloop()

from tkinter import *
import time

# window=Tk()
# window.geometry('300x400')
# window.title('Календарь')
# time = time.strftime('%d %B %Y')
# m = Label(font="Verdana 24 bold")
# m.pack()
# m.config(text=time)
# window.mainloop()

from tkinter import *
import time
# window=Tk()
# window.geometry("600x200")
# Month = time.strftime('%B')
# Year = time.strftime('%Y')
# match Month:
#     case "January":
#         Month = "Январь"
#     case "February":
#         Month = "Февраль"
#     case "March":
#         Month = "Март"
#     case "August":
#         Month = "Август"
# m = Label(font="Verdana 24 bold")
# m.pack()
# m.config(text=Month + " " + Year)
# window.mainloop()

# from tkinter import *
# import time
#
# window=Tk()
# window.geometry('600x200')
# Month = time.strftime('%B')
# Year = time.strftime('%Y')
# Day = time.strftime('%d')
# match Month:
#     case "January":
#         Month = "Января"
#     case "February":
#         Month = "Февраля"
#     case "March":
#         Month = "Марта"
# m = Label(font="Verdana 24 bold")
# m.pack()
# m.config(text=Day + " " + Month + " " + Year)
# window.mainloop()

from tkinter import *
import time
# def tick():
#     t = time.strftime("%H:%M:%S")
#     m.config(text=t)
#     m.after(1000, tick) # вызовы идут каждую секунду
#
# window=Tk()
# m = Label(font="Verdana 24 bold")
# m.pack()
# tick() # вызов функции, без нее часы не работают
# window.mainloop()

# from tkinter import *
# import time
# window = Tk()
# Day = time.strftime('%A')
# match Day:
#     case "Monday":
#            Day = "понедельник"
#     case "Tuesday":
#            Day = "вторник"
#     case "Wednesday":
#            Day = "среда"
#     case "Thursday":
#            Day = "четверг"
#     case "Friday":
#            Day = "пятница"
#     case "Saturday":
#            Day = "суббота"
#     case "Sunday":
#            Day = "воскресенье"
# metka = Label(window, font=("Verdana 24 bold"))
# metka.pack()
# metka.config(text = "Сегодня " + Day)
# window.mainloop()

# радиокнопки
# from tkinter import *
# window=Tk()
#
# kvas = "Квас"
# tea = "Чай"
# coffee = "Кофе"
#
# drink = StringVar(value=coffee)
#
# m = Label(text="Выбери любимый напиток:")
# m.pack()
# m2 = Label(textvariable=drink)
# m2.pack()
# minecraft_b = Radiobutton(text=kvas, value=kvas, variable=drink)
# minecraft_b.pack()
#
# roblox_b = Radiobutton(text=tea, value=tea, variable=drink)
# roblox_b.pack()
#
# brawl_b = Radiobutton(text=coffee, value=coffee, variable=drink)
# brawl_b.pack()
#
# window.mainloop()
#
# m2 = Label(textvariable=drink)
# m2.pack()

# from tkinter import *
# import datetime as dt

#
# def datetime():
#     m.config(text=f"{Date} {Time}")
#
# def date():
#     m.config(text=Date)
#
#
# def time():
#     m.config(text=Time)
#
# def night():
#     R3.config(bg="black", fg="black")
#     R4.config(bg="black", fg="black")
#
#
# window = Tk()
#
# d = dt.datetime.now()
# Date = d.strftime('%d %B %Y')
# print(Date)
# Time = d.strftime('%X')
# print(Time)
#
# var = IntVar()
# var.set(0)
#
# R1 = Radiobutton(text="Дата и время", command=datetime,
#                  variable=var, value=0)
# R1.pack(side=LEFT)
# R2 = Radiobutton(text="Дата", command=date,
#                  variable=var, value=1)
# R2.pack(side=LEFT)
# R3 = Radiobutton(text="Время", command=time,
#                  variable=var, value=2)
# R3.pack(side=LEFT)
# R4 = Radiobutton(text="Ночная тема", command=night,
#                  variable=var, value=3)
# R4.pack(side = LEFT)
# m = Label(font="Verdana 24 bold")
# m.pack(side=LEFT)
# m.config(text=f"{Date} {Time}")
# window.mainloop()

# from tkinter import *
#
# def show():
#     c['fg']=v.get()
#
# window=Tk()
#
# v = StringVar()
# v.set('black')
# c = Checkbutton(text="Это переключатель цвета", variable=v,
#                 onvalue="magenta", offvalue="red", command=show)
# c.pack()
# window.mainloop()

from tkinter import *
import time
#
# def tick():
#   t = time.strftime("%H:%M:%S")
#   m.config(text=t)
#   m.after(1000, tick)
#
# def bg_color():
#   m['bg'] = v1.get()
#
# def fg_color():
#   m['fg'] = v2.get()
#
# def font():
#   m['font'] = v3.get()
#
# window = Tk()
# window.geometry('480x308')
# m = Label(font='Verdana 16', bg='lightblue', fg='black')
# m.pack()
#
# v1 = StringVar()
# v1.set('lightblue')
# c1 = Checkbutton(text='Переключатель цвета фона', variable=v1, onvalue='salmon', offvalue='lightblue', command=bg_color)
# c1.pack()
#
# v2 = StringVar()
# v2.set('black')
# c2 = Checkbutton(text='Переключатель цвета текста', variable=v2, onvalue='white', offvalue='black', command=fg_color)
# c2.pack()
# v3 = StringVar()
# v3.set('Verdana 16')
# c3 = Checkbutton(text='Переключатель шрифта', variable=v3, onvalue='Courier 16 bold', offvalue='Verdana 16', command=font)
# c3.pack()
#
# tick()
# window.mainloop()

from tkinter import *
from tkinter import messagebox as ab
import tkinterweb
# def root():
#     window.destroy() # закрыть окно по нажатию кнопки выход
#
# def clear_all():
#     e1.delete(0, END)
#     e2.delete(0, END)
#     e3.delete(0, END)
#     e4.delete(0, END)
#     l5.config(text = '') # ОЧИСТИТЬ ПОЛЕ
# # pack grid нельзя смешивать. Грид - сетка дял виджетов.
# def show_info ():
#     name = e1.get() # вывод информации в окно get
#     surname = e2.get()
#     group_num = e3.get()
#     age = e4.get()
#     sex = gender.get()
#     about = txt.get(1.0, END) # с какой по какую позицию из поля берется инфомрация
#
#     if not name or not surname or not group_num or not age:
#         print('Заполните обязательные поля!') # ВЫВОД РЕЗУЛЬТАТА В КОНССОЛЬ,СТРОКУ МОЖНО УДАЛИТЬ И ВЫВОДИТЬ СРАЗУ В ОКНО
#         ab.showwarning('Warning', 'Заполните обязательные поля!') # ВИДЖЕТ ПРЕДУПРЕЖДЕНИЕ О НЕЗАПОЛНЕННЫХ ПОЛЯХ
#         return
#     if not age.isdigit():
#         ab.showwarning('Warning', 'В  поле возраст должны быть цифры.')  # ВИДЖЕТ ПРЕДУПРЕЖДЕНИЕ О НЕЗАПОЛНЕННЫХ ПОЛЯХ
#         return
#
#     l5.config(text= f'Имя: {name} Фамилия {surname} Номер группы: {group_num } Возраст {age} Пол {sex} О себе {about}')
# window=Tk()
# window.geometry("600x500")
# window.title('Анкета cтудента')
# header_frame=Frame(window)
# header_frame.pack()
# form_frame=Frame(window)
# form_frame.pack()
# text_frame = Frame(window)
# text_frame.pack()
# button_frame=Frame(window)
# button_frame.pack()
#
# l = Label(header_frame, text='Студент Анкета', width = 20)
# l.pack(pady=10)
# l1 = Label(form_frame, text = 'Имя', width = 20)
# l1.grid(column=0, row=0)
# e1 = Entry(form_frame, width = 20)
# e1.grid(column=1, row=0)
# l2 = Label(form_frame, text = 'Фамилия', width = 20)
# l2.grid(column=0, row=1)
# e2 = Entry(form_frame, width = 20)
# e2.grid(column=1, row=1)
# l3 = Label(form_frame, text = 'Группа', width = 20)
# l3.grid(column=0, row=2)
# e3 = Entry(form_frame, width = 20)
# e3.grid(column=1, row=2)
# l4 = Label(form_frame, text = 'Возраст', width = 20)
# l4.grid(column=0, row=3)
# e4 = Entry(form_frame, width = 20)
# e4.grid(column=1, row=3)
# l5 = Label(text_frame, text= '', width = 60, height = 3)
# l5.pack()
# l6 = Label(text_frame, text = 'О себе')
# l6.pack(pady=10)
# txt = Text(text_frame, width=30, height=8)
# txt.pack(side=LEFT)
# scrol = Scrollbar(text_frame, command=txt.yview)# делаем скролбар
# scrol.pack(side=LEFT, fill=Y) # разммещаем в том же фрейме
# txt.config(yscrollcommand=scrol.set) # пишем команмду, чтобы он корректно двигался за движением текста
# gender = StringVar(value="Мужской")
# R1 = Radiobutton(form_frame, text="Мужской",
#                  variable=gender, value='Мужской')
# R1.grid(column=1, row=4)
# R2 = Radiobutton(form_frame, text="Женский",
#                  variable=gender, value='Женский')
# R2.grid(column=2, row=4)
# button2=Button(button_frame, text='Выход', command=root)
# button2.grid(column=2, row=5)
# button3 = Button(button_frame,text = 'Очистить', command = clear_all)
# button3.grid(column=3, row=5)
# button4=Button(window, text='Показать данные', command = show_info, width=15)
# button4.pack()
# window.mainloop()
#
#
# from tkinter import *
# import tkinterweb
# def root():
#     window.destroy() # закрыть окно по нажатию кнопки выход
#
# def show_info ():
#     name = e1.get() # вывод информации в окно get
#     surname = e2.get()
#     group_num = e3.get()
#     age = e4.get()
#     l5.config(text= f'МОРОЖЕНОЕ: {name} + {surname} ГОРЧИЦА = : {group_num } УЕА {age}')
# def clear_all():
#     e1.delete(0, END)
#     e2.delete(0, END)
#     e3.delete(0, END)
#     e4.delete(0, END)
#     l5.config(text = '') # ОЧИСТИТЬ ПОЛЕ
# # pack grid нельзя смешивать. Грид - сетка дял виджетов.
# window=Tk()
# window.geometry("400x250")
# window.title('СТУДЕНТ АНКЕТЫ')
# header_frame=Frame(window)
# header_frame.pack()
# form_frame=Frame(window)
# form_frame.pack()
# button_frame=Frame(window)
# button_frame.pack()
# button1_frame=Frame(window)
# button1_frame.pack()
#
# l = Label(header_frame, text='СТУДЕНТ АНКЕТЫ', width = 20)
# l.pack(pady=10)
# l1 = Label(form_frame, text = 'МОРОЖЕНОЕ', width = 10)
# l1.grid(column=0, row=0)
# e1 = Entry(form_frame, width = 10)
# e1.grid(row=0, column=1,)
# l2 = Label(form_frame, text = '+', width = 10)
# l2.grid(column=0, row=1)
# e2 = Entry(form_frame, width = 10)
# e2.grid(row=0, column=4)
# l3 = Label(form_frame, text = 'ГОРЧИЦА = ', width = 10)
# l3.grid(column=0, row=2)
# e3 = Entry(form_frame, width = 10)
# e3.grid(row=3, column=0)
# l4 = Label(form_frame, text = 'ВКУСНЯТИНА', width = 10)
# l4.grid(column=0, row=3)
# e4 = Entry(form_frame, width = 10)
# e4.grid(column=1, row=3)
# l5 = Label(form_frame, text= '', width = 10)
# l5.grid(column=2, row=3)
# button1=Button(form_frame, text='Показать данные', command = show_info)
# button1.grid(column=3, row=3)
# button2=Button(button_frame, text='Аааааааааааааааааааааааааааа помогите!!!!!!!!!!!!', height = 3, command=root)
# button2.grid(column=0, row=4)
# button3 = Button(button_frame,text = 'Очистить', command = clear_all)
# button3.grid(column=1, row=4)
# window.mainloop()
import random
from tkinter import messagebox as mb

def check_color():
    user = color_var.get() # забираем значение пользователя
    print(user)
    colors = ['желтый','зеленый','красный']
    color = random.choice(colors)
    if user == '' or user == ' ':  # if not user
        mb.showwarning('Предупреждение!',  'Заполните поле!')
        return
    elif user == color:
        result = 'Вы угадали!'
    else:
        result = f'Вы не угадали. Вы выбрали: {user}. Правильный ответ - {color}'
    answer = mb.askyesno(title='Вопрос', message='Результат в метку?')
    if answer:
        l_result.config(text = result)
    else:
        l_result.config(text='')
        mb.showinfo('Info', result)

window=Tk()
window.geometry("400x300")
window.title('Угадайте цвет светофора')
l_result = Label(window, text='')
l_result.pack(pady=10)

l = Label(window, text='Угадай цвет светофора', width=30, font =('Arial', 12))
l.pack(pady=10)
l.pack(pady=10)
color_var = StringVar(value='Зеленый') # переключаем радиокнопки, ставим указатель на хеленый
g = Radiobutton(window, text='Зеленый', variable=color_var, value='Зеленый')
g.pack(pady=10)
r = Radiobutton(window, text='Красный', variable=color_var, value='Красный')
r.pack(pady=10)
y = Radiobutton(window, text='Желтый', variable=color_var, value='Желтый')
y.pack(pady=10)

b = Button(window, text = 'Проверить', command = check_color) # command = check_color
b.pack(pady=10)

window.mainloop()



