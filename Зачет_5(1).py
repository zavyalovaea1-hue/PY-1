import requests
import json

from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    if target_code and base_code:
        try:
            result = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            result.raise_for_status() # статус сайта
            # data = json.loads(result.text)  # возвращаем джейсон файл в строковом типе данных
            data = result.json() # получаем джейсон файл
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code] # доставем название валюты
                target = currencies[target_code]

                mb.showinfo('Курс обмена',
                            f'Курс ' 
                            f'{exchange_rate:.5f} {target} за 1 {base}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')

        except Exception as e:
            mb.showerror('Ошибка', f'Error 400 {e}')


currencies = {'USD':'Доллар США',
              'EUR':'Евро',
              'CNY':'Юань',
              'RUB':'Российский рубль'
              }


root = Tk()
root.title('Курс валют')
root.geometry('350x420')

# Базовая валюта 1
Label(text='Базовая валюта 1').pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack()
base_label1 = ttk.Label()
base_label1.pack(pady=2, padx=10)

# Базовая валюта 2
Label(text='Базовая валюта 2').pack(pady=10, padx=10)
base_combobox2 = ttk.Combobox(values=list(currencies.keys()))
base_combobox2.pack()
base_label2 = ttk.Label()
base_label2.pack(pady=2, padx=10)

# Целевая валюта
Label(text='Целевая валюта').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack()
currency_label = ttk.Label()
currency_label.pack(pady=2, padx=10)

Button(text='Получить курс', command=exchange).pack(pady=15)
base_combobox.bind('<<ComboboxSelected>>', update_base_label1)
base_combobox2.bind('<<ComboboxSelected>>', update_base_label2)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

root.mainloop()