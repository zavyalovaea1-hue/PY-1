from time import strftime
from tkinter import *
from tkinter import messagebox
import pygame as pg # для загрузки библиотеки пишем в терминале pip install pygame. Или открываем пайтон packages, пишем в поиске pygame.
# либо через шестеренку настройка или на пирог - сеттингс апперанс интерпретатор,выбираем пакет и грузим. ставим галки инсталлируем
def tick():
    global time_run
    current_time = strftime('%H:%M:%S') # выводим текущее время
    current_time1 = strftime('%H:%M')
    current_time2 = strftime('%H')
    text.config(text=current_time)
    if (time_run==current_time or time_run == current_time1
            or time_run == current_time2):
        time_run = ''
        pg.mixer.music.play()
    # tick() # загружает процессор, так лучше не делать
    text.after(1000, tick) # каждую 1000 милисекунд будет обращаться к процессору за функцией тик


def on():
    global time_run
    time_run = entry.get().strip()
    messagebox.showinfo('Время установки будильника',
                        f'Будильник установлен {time_run}')


def off():
    global time_run
    time_run = ''
    pg.mixer.music.stop()
    messagebox.showwarning('Предупреждение',
                        f'Будильник отключен {time_run}')
#вставить файл в пэйчарм - нажимаем на проект правой клавишей мыши и паст. Копировать строку контрол д
pg.mixer.init() # инициируем программу, миксер
pg.mixer.music.load('music.mp3')  # загружаем рабочий модуль, в конце название файла с музыкой
time_run = ''
root = Tk() # можно писать рут (корень) или вин (окно)
root.config(bg = 'black')# меняем цвет всего окна
root.geometry('400x300')
root.title('Будильник')
text = Label(root, text='00:00:00')
text.config(font=('Arial', 50), bg='black', fg='lime')
text.pack() # внизу side = BOTTOM, по умолчанию используется side = TOP (центр вверху)
entry = Entry(root, font=('Arial', 20), width=10, justify=CENTER) # ширина в символах, не в пикселях
entry.pack(pady=10)
entry.focus_set() # поставить курсор в поле

btn = Button(text = 'Включить', width=10, font=('Arial', 10), command=on)
btn.pack(pady=5)
btn1 = Button(text = 'Выключить', width=10, font=('Arial', 10), command=off)
btn1.pack(pady=5)

tick()
root.mainloop()

