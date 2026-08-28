import math
from tkinter import * # любой ретерн - кортеж


def add(n1, d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return n, d


def sub(n1, d1, n2, d2):
    n = n1 * d2 - n2 * d2
    d = d1 * d2
    return n, d


def mult(n1, d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return n, d


def div(n1, d1, n2, d2):
    n = n1 * d2
    d = d1 * n2
    return n, d


def calk():
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())

        operator = oper.get().strip()
        res = (0, 1)
        match operator: # выполнение математических действий оператор матч
            case '+': res = add(n1, d1, n2, d2)
            case '-': res = sub(n1, d1, n2, d2)
            case '*': res = mult(n1, d1, n2, d2)
            case '/': res = div(n1, d1, n2, d2)
        nod = math.gcd(res[0], res[1])  # gcd наибольший общий делитель
        n = res[0]
        d = res[1]
        n = int(n / nod)
        d = int(d / nod)
        if d < 0:
            n = -n
            d = -d

        int_p = 0
        if abs(n) >= abs(d):
            int_p = n // d
            n = n % d
            # Если после взятия остатка дробь стала 0, убираем знаменатель
            if n == 0:
                d = 1
        int_part.config(text=int_p)
        num3.config(text=n)
        den3.config(text=d)

    except Exception:
        pass # не будем делать никаких действий при наличии этой ошибки


root = Tk() # можно писать рут (корень) или вин (окно)
WIDTH = root.winfo_screenwidth()  # получить данные о размере экрана пользователя, ШИРИНА
HEIGHT = root.winfo_screenheight() # ВЫСОТА экрана пользователя
X = 300
Y = 140
root.geometry(f'{X}x{Y}+{WIDTH//2-X//2}' # ОКНО ОТКРЫВАЕТСЯ СТРОГО ПО ЦЕНТРУ НА ЛЮБОМ ОКНЕ
              f'+{HEIGHT//2-Y//2-20}') # // - делить нацело без остатка
root.title('Калькулятор дробей')
frame = Frame(root)
frame.pack(pady=10) # во фрейме используем только менеджер разметки грид! 2  разных использовать нельзя!

num1 = Entry(frame, width=2)
num1.config(font='Arial 15', justify='center') # джастифай - расположение курсора по центру
num1.grid(row=0, column=0)

line1 = Label(frame, text=chr(8212)*2)
line1.grid(row=1,column=0)

den1 = Entry(frame, width=2)
den1.config(font='Arial 15', justify='center') # джастифай - расположение курсора по центру
den1.grid(row=2, column=0)

oper = Entry(frame, font='Arial 15', width=2)
oper.config(width=2, justify='center')
oper.grid(row=1, column=1, padx=5)

num2 = Entry(frame, width=2)
num2.config(font='Arial 15', justify='center') # джастифай - расположение курсора по центру
num2.grid(row=0, column=2)

line2 = Label(frame, text=chr(8212)*2)
line2.grid(row=1,column=2)

den2 = Entry(frame, width=2)
den2.config(font='Arial 15', justify='center') # джастифай - расположение курсора по центру
den2.grid(row=2, column=2)

btn = Button(frame, text='=', width=2, font='Arial 15', command=calk)
btn.grid(row=1, column=3, padx=5)

int_part = Label(frame, text='  ', bg='lightblue')
int_part.config(font='Arial 20', width=2, justify='center')
int_part.grid(row=1, column=4, padx=5)

num3 = Label(frame, width=2, bg='lightblue')
num3.config(font='Arial 15', justify='center') # джастифай - расположение курсора по центру
num3.grid(row=0, column=5)

line3 = Label(frame, text=chr(8212)*2)
line3.grid(row=1,column=5)

den3 = Label(frame, width=2, bg='lightblue')
den3.config(font='Arial 15', justify='center') # джастифай - расположение курсора по центру
den3.grid(row=2, column=5)

root.mainloop()
