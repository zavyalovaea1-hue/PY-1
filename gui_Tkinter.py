from tkinter import *


def res(event=None):
    item = entry.get().strip()
    try:

        item = int(item) + 100 # преобразовываем числовой результат (+100)
    except ValueError:
        item = 'Free' # отрабатывает оишбку пустого окна и выводим вместо ошибки фри (сободно)
    result.config(text=item) # ввод результата в окно

root = Tk() # можно писать рут (корень) или вин (окно)
# root.geometry("400x250+400+200")# ПОДРЯД БЕЗ ПРОБЕЛОВ В СКОБКАХ! центр координат - верхнгий левый угол, х увеличиваетя как обычно, а у наоборот. сверху вниз
WIDTH = root.winfo_screenwidth()  # получить данные о размере экрана пользователя, ШИРИНА
HEIGHT = root.winfo_screenheight() # ВЫСОТА экрана пользователя
X = 400
Y = 250
root.geometry(f'{X}x{Y}+{WIDTH//2-X//2}' # ОКНО ОТКРЫВАЕТСЯ СТРОГО ПО ЦЕНТРУ НА ЛЮБОМ ОКНЕ
              f'+{HEIGHT//2-Y//2-20}') # // - делить нацело без остатка
# root.geometry("400x250+400+200")#
root.title('Проба')
# размещение информации в ткинтер проводится всего тремя менеджерами: пак,грид и пол
text = Label(root, text='Введите значение: ')
text.config(font=('Arial', 20), bg='lightblue', fg='black')
text.pack() # внизу side = BOTTOM, по умолчанию используется side = TOP (центр вверху)
entry = Entry(root, font=('Arial', 20), width=20, justify=CENTER) # ширина в символах, не в пикселях
entry.pack(pady=10)
entry.focus_set() # поставить курсор в поле
result = Label(root, text='  '*10, bg='lightgrey', fg='black', font=('Arial', 20))
result.config(justify=CENTER)
result.pack() # выводим результат
btn = Button(text = 'кнопка', command=res)
btn.pack(pady=10)
entry.bind('<Return>', res) # значение выводится по клику ентер
root.mainloop()