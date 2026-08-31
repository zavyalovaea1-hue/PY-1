import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import Menu

import imgtk
from PIL import Image, ImageTk # импорт изображений

win = tk.Tk()
win.title("Tk")
win.geometry("600x500")

def open_file():
    try:
        file = fd.askopenfilename() # открыть файл по имени...
        if file: # код обрабатывается, если выбран файл
            img = Image.open(file)
            print(type(img)) # узнаем тип файла в консоли
            print(img.size) # узнаем размер файла
            win_width = 500
            win_height = 500
            img.thumbnail((win_width, win_height))  # умещаем несколько изображений в 1 окно с определенным размером пикселей

            imgtk = ImageTk.PhotoImage(img)
            l.config(image=imgtk)
            l.image = imgtk
    except Exception as er:
        mb.showerror('Error', er)

mainmenu = Menu(win)
win.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu) # каскад пишется для раздела меню, который будет разворачиваться вниз

# Добавляем команды ВНУТРЬ подменю filemenu
filemenu.add_command(label="Открыть", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Закрыть", command=win.destroy)

l = tk.Label(win)
l.pack()

win.mainloop()
