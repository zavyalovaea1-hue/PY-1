from calendar import error
from email.header import UTF8
from tkinter import * # менеджер заметок, открытие файлов
from tkinter import filedialog as fd
from tkinter import messagebox as mb

# # обработать событие, чтоб не было ошибки если файл не выбран
# def add_note():
#     try:
#
#         file = fd.askopenfilename( # открыть файл по имени...
#             filetypes=[('text file', '*.txt'), ('all files', '*.*')] # в выборе будут текстовые файлы и все на выбор пользователя
#         ) # эта команда позволяет открывать поиск файла в папках внутренней памяти компа
#         if not file: # убираем ошибку, если файл не выбран
#             return
#
#         with open (file, 'r', encoding='UTF-8') as file:
#         # with open (r'C:\Users\Катя\Desktop\учебный файл.txt', 'r', encoding='UTF-8') as file: # р эс файл - читать из файла
#     # note='Не забыть подготовиться к итоговой работе до 1 сентября!'
#             note = file.read()
#             txt.insert(END, note) # метод инсерт позволяет вставлять заметку по кнопке в поле тхт в конце текста. ЕНД вводим обязательно без него мметод не работает
#     except Exception as error: # срабатывает на все ошибки
#         mb.showerror('Ошибка', error) # выводим ошибку, если не выполняются даные и выходит ошибка
#
#
# def clear_note():
#     answer = mb.askyesno(title='Вопрос', message='Удалить все заметки?') # выводим вопрос - да или нет?
#     if answer:
#         txt.delete(1.0, END)  # откуда докуда очистать с индекса 1, с 1 с нулевой позиции строки до окончания текста
#
#
# def save_note(): # сохранить данные в указанный файл
#     file_path = fd.asksaveasfilename(  # файл диалог, вызываем перед применением
#         defaultextension='.txt',
#         filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
#     )
#     content = txt.get('1.0', END) # выгружаем из текстового поля данные
#     try:
#         with open(file_path, 'w', encoding='utf-8') as f:
#             f.write(content) # врайт - записать
#         print('Файл сохранён:', file_path)
#         mb.showinfo('Info', "Файл успешно сохранен.")
#     except Exception as error:
#         mb.showerror('Ошибка', error)
#
#
# def info_spr():
#     mb.showinfo('Info', 'Приложение "Менеджер заметок"')
#
# win = Tk()
# win.title('Менеджер заметок')
# win.geometry('600x400')
# fr = Frame(win)
# fr.pack(side=LEFT)
#
# txt = Text(fr, width=40, height=10, bg = 'lightyellow', wrap=WORD) # перенос по словам
# txt.pack(side=LEFT)
# scroll = Scrollbar(fr, command=txt.yview)
# scroll.pack(side=RIGHT, fill=Y)
# txt.config(yscrollcommand=scroll.set) # две строки подряд прокручивае в обе стороны
# # b1 = Button(win, text = 'Добавить заметку', command=add_note)
# # b1.pack(side=LEFT)
# # b2 = Button(win, text = 'Очистить', command=clear_note)
# # b2.pack(side=LEFT)
# # b3 = Button(win, text = 'Сохранить', command=save_note)
# # b3.pack(side=LEFT)
#
#
# mainmenu = Menu(win)
# win.config(menu=mainmenu)
#
# filemenu = Menu(mainmenu, tearoff=0) # теарофф закрепляет меню и выводит выделение цвета перед выбором. 0 и 1 - да и нет
# filemenu.add_command(label="Добавить заметку", command=add_note)
# filemenu.add_command(label="Очистить", command=clear_note)
# filemenu.add_command(label="Сохранить", command=save_note)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=win.destroy)
# infomenu = Menu(mainmenu)
# mainmenu.add_cascade(label="File", menu=filemenu)
# mainmenu.add_cascade(label="Info", menu=infomenu)
# infomenu.add_command(label='About', command=info_spr)
#
# text = Text(width=30, height=8, bg="lightgray", wrap=WORD)
# text.pack(side=LEFT)
# scroll = Scrollbar(command=text.yview)
# scroll.pack(side=LEFT, fill=Y)
# text.config(yscrollcommand=scroll.set)
#
# win.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox


def open():
    # global imgconv, l

    try:
        file = fd.askopenfilename()
        if file:  # Проверяем, был ли выбран файл
            img = Image.open(file)
            imgconv = img

            # Адаптируем размер изображения под размер окна
            window_width = 500
            window_height = 500
            img.thumbnail((window_width, window_height))

            img = ImageTk.PhotoImage(img)

            # Если лейбл уже существует, обновляем его изображение
            if 'l' in globals():
                l.configure(image=img)
                l.image = img
            else:
                l = Label(image=img)
                l.pack()
                l.image = img

    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл не найден")
    except OSError:  # Ошибка при открытии файла или неизображения
        messagebox.showerror("Ошибка", "Не удалось открыть файл, возможно, это не изображение")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


window = Tk()
window.title("PHOTO")
window.geometry("500x500")
mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=open)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=quit)
mainmenu.add_cascade(label="Файл", menu=filemenu)

window.mainloop()


# def open():
#
# window = Tk()
# window.title("PHOTO")
# window.geometry("500x500")
# mainmenu = Menu(window)
# window.config(menu=mainmenu)
#
# filemenu = Menu(mainmenu, tearoff=0)
# filemenu.add_command(label="Открыть...", command=open)
# filemenu.add_separator()
# filemenu.add_command(label="Выход", command=quit)
# mainmenu.add_cascade(label="Файл", menu=filemenu)

# window.mainloop()


