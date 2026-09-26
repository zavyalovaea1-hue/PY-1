import requests
import json

from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def get_rate(base_code, target_code):
    try:
        response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
        response.raise_for_status()

        data = response.json()

        if target_code in data['rates']:
            return data['rates'][target_code]
        else:
            mb.showerror('Ошибка', f'Валюта {target_code} не найдена для базы {base_code}')
            return None
    except Exception as e:
        mb.showerror('Ошибка', f'Не удалось получить курс для {base_code}: {e}')
        return None


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]  # доставаем название валюты из словаря
    currency_label.config(text=name)


def update_base_label1(event):
    code = base_combobox.get()
    name = currencies[code]  # доставаем название валюты из словаря
    base_label1.config(text=name)


def update_base_label2(event):
    code = base_combobox2.get()
    name = currencies[code]  # доставаем название валюты из словаря
    base_label2.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code1 = base_combobox.get()
    base_code2 = base_combobox2.get()

    if not target_code:
        mb.showwarning('Внимание', 'Выберите целевую валюту')
        return
    if not base_code1 and not base_code2:
        mb.showwarning('Внимание', 'Выберите хотя бы одну базовую валюту')
        return

    message = ''


    if base_code1:
        rate1 = get_rate(base_code1, target_code)
        if rate1 is not None:
            base = currencies[base_code1]  # доставаем название валюты
            target = currencies[target_code]
            message += f'{rate1:.5f} {target} за 1 {base}\n'


    if base_code2:
        rate2 = get_rate(base_code2, target_code)
        if rate2 is not None:
            base = currencies[base_code2]  # доставаем название валюты
            target = currencies[target_code]
            message += f'{rate2:.5f} {target} за 1 {base}'

    if message:
        mb.showinfo('Курс обмена', message)
    else:
        mb.showerror('Ошибка', 'Не удалось получить ни один курс')

currencies = {
    'USD': 'Доллар США',
    'EUR': 'Евро',
    'CNY': 'Юань',
    'RUB': 'Российский рубль',
}

root = Tk()
root.title('Курс валют ')
root.geometry('350x420')

# Базовая валюта 1
Label(text='Базовая валюта 1').pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=list(currencies.keys()))  # выпадающее меню
base_combobox.pack()
base_label1 = ttk.Label()
base_label1.pack(pady=2, padx=10)

# Базовая валюта 2
Label(text='Базовая валюта 2').pack(pady=10, padx=10)
base_combobox2 = ttk.Combobox(values=list(currencies.keys()))  # выпадающее меню
base_combobox2.pack()
base_label2 = ttk.Label()
base_label2.pack(pady=2, padx=10)

# Целевая валюта
Label(text='Целевая валюта ').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies))  # выпадающее меню
target_combobox.pack()
currency_label = ttk.Label()
currency_label.pack(pady=2, padx=10)

button = Button(text='Получить курс', command=exchange).pack()

base_combobox.bind('<<ComboboxSelected>>', update_base_label1)
base_combobox2.bind('<<ComboboxSelected>>', update_base_label2)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

root.mainloop()