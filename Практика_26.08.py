import tkinter as tk

win = tk.Tk()
win.title("Мини-проводник")
win.geometry("700x500")

e = tk.Entry(win, width=80)
e.pack(pady=10)

b = tk.Button(win, text = 'Выбрать папку')
b.pack(pady=10)

listbox = tk.Listbox(win, width=80, height=20)
listbox.pack(pady=10)


win.mainloop()