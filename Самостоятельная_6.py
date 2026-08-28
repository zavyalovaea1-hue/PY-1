# Добавьте в программу пункт меню, который будет очищать текстовое поле.Эта команда должна
# быть доступна через меню "Файл".
# Требования:
# 1. Добавь в меню `file_menu`новую команду.
# 2. Назови её "Очистить".
# 3. При нажатии на неё должен вызываться уже существующий метод delete`.
# Совет: Используй метод .add_command()`.

from calendar import error
from email.header import UTF8
from tkinter import * # менеджер заметок, открытие файлов
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def add_note():
    try:

        file = fd.askopenfilename( # открыть файл по имени...
            filetypes=[('text file', '*.txt'), ('all files', '*.*')] # в выборе будут текстовые файлы и все на выбор пользователя
        ) # эта команда позволяет открывать поиск файла в папках внутренней памяти компа
        if not file: # убираем ошибку, если файл не выбран
            return

        with open (file, 'r', encoding='UTF-8') as file:
        # with open (r'C:\Users\Катя\Desktop\учебный файл.txt', 'r', encoding='UTF-8') as file: # р эс файл - читать из файла
    # note='Не забыть подготовиться к итоговой работе до 1 сентября!'
            note = file.read()
            txt.insert(END, note) # метод инсерт позволяет вставлять заметку по кнопке в поле тхт в конце текста. ЕНД вводим обязательно без него мметод не работает
    except Exception as error: # срабатывает на все ошибки
        mb.showerror('Ошибка', error) # выводим ошибку, если не выполняются даные и выходит ошибка


def clear_note():
    answer = mb.askyesno(title='Вопрос', message='Удалить все заметки?') # выводим вопрос - да или нет?
    if answer:
        txt.delete(1.0, END)  # откуда докуда очистать с индекса 1, с 1 с нулевой позиции строки до окончания текста


def save_note(): # сохранить данные в указанный файл
    file_path = fd.asksaveasfilename(  # файл диалог, вызываем перед применением
        defaultextension='.txt',
        filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
    )
    content = txt.get('1.0', END) # выгружаем из текстового поля данные
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content) # врайт - записать
        print('Файл сохранён:', file_path)
        mb.showinfo('Info', "Файл успешно сохранен.")
    except Exception as error:
        mb.showerror('Ошибка', error)


win = Tk()
win.title('Менеджер заметок')
win.geometry('600x400')
fr = Frame(win)
fr.pack(side=LEFT)

txt = Text(fr, width=40, height=10, bg = 'lightyellow', wrap=WORD) # перенос по словам
txt.pack(side=LEFT)
scroll = Scrollbar(fr, command=txt.yview)
scroll.pack(side=RIGHT, fill=Y)
txt.config(yscrollcommand=scroll.set) # две строки подряд прокручивае в обе стороны

mainmenu = Menu(win)
win.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0) # теарофф закрепляет меню и выводит выделение цвета перед выбором. 0 и 1 - да и нет
filemenu.add_command(label="Добавить заметку", command=add_note)
filemenu.add_command(label="Очистить", command=clear_note)
filemenu.add_command(label="Сохранить", command=save_note)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)


win.mainloop()
