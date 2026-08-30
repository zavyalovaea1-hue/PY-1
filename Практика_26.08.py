import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os # модуль позволяет читать содержимое ос


def choose_directory():
    folder = fd.askdirectory()  # просить выбрать в окне директорию (путь), фолдер переменная, записывает в переменную
    e.delete(0, tk.END) # поле ентри (е) - очищаем остатки предыдущих адресов
    e.insert(tk.END, folder) # в поле ентри (е) вставляем путь к папке
    open_directory(folder)

def open_directory(path):
    try:
        items = sorted(os.listdir(path)) # лист дир - получение списка файлов из директории, сортируем список
        for item in items:
            full_path = os.path.join(path, item)
            print(full_path)
            if os.path.isdir(full_path):
                # listbox.insert(tk.END, f'Folder {item}')
                listbox.insert(tk.END, f'📂 {item}') # вызов эмодзи вин + ,.
            else:
                listbox.insert(tk.END, f'📜 {item}') # либо папка, либо файл
            # listbox.insert(tk.END, item)
    except Exception as error:
        mb.showerror('Показывать ошибку', error)

def open_selected():
    pass


win = tk.Tk()
win.title("Мини-проводник")
win.geometry("700x500")

e = tk.Entry(win, width=80)
e.pack(pady=10)

b = tk.Button(win, text = 'Выбрать папку', command = choose_directory)
b.pack(pady=10)

listbox = tk.Listbox(win, width=80, height=20, font = ('Arial', 18))
listbox.pack(pady=10)
listbox.bind('<Double-Button-1>', open_selected)

win.mainloop()