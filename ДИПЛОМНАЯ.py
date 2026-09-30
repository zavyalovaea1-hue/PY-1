import requests
import json

from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

from fastapi import params


def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,ripple,cardano,solana,dogecoin,polkadot,avalanche,chainlink,litecoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        # Словарь наименований популярных криптовалют
        names = {
            "bitcoin": "BTC",
            "ethereum": "ETH",
            "ripple": "XRP",
            "cardano": "ADA",
            "solana": "SOL",
            "dogecoin": "DOGE",
            "polkadot": "DOT",
            "avalanche": "AVAX",
            "chainlink": "LINK",
            "litecoin": "LTC"
        }

        for coin_id, info in data.items():
            symbol = names.get(coin_id, coin_id.upper())
            price = info.get("usd")
            if coin_id in data['price']:
                return data['price'][coin_id]
            else:
            mb.showerror('Ошибка', f'Валюта {target_code} не найдена для базы {base_code}')
            return None

        except Exception as e:
        mb.showerror('Ошибка', f'Не удалось получить курс для {base_code}: {e}')
        return None
    except requests.exceptions.RequestException as error:
        print("Ошибка запроса:", error)


if __name__ == "__main__":
    get_crypto_prices()


def update_currency_label(event):
    code = target_combobox.get()
    name = params[code]  # доставаем название валюты из словаря
    currency_label.config(text=name)


def update_base_label1(event):
    code = base_combobox.get()
    name = params[code]  # доставаем название валюты из словаря
    base_label1.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code1 = base_combobox.get()


    if not target_code:
        mb.showwarning('Внимание', 'Выберите целевую валюту')
        return
    if not base_code1:
        mb.showwarning('Внимание', 'Выберите хотя бы одну базовую валюту')
        return

    message = ''


    if base_code1:
        rate1 = get_crypto_prices(base_code1, target_code)
        if rate1 is not None:
            base = params[base_code1]  # доставаем название валюты
            target = params[target_code]
            message += f'{rate1:.5f} {target} за 1 {base}\n'


    if message:
        mb.showinfo('Курс обмена', message)
    else:
        mb.showerror('Ошибка', 'Не удалось получить ни один курс')


root = Tk()
root.title('Курс валют ')
root.geometry('350x420')

# Базовая валюта 1
Label(text='Базовая валюта 1').pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=list(currencies.keys()))  # выпадающее меню
base_combobox.pack()
base_label1 = ttk.Label()
base_label1.pack(pady=2, padx=10)

# Целевая валюта
Label(text='Целевая валюта ').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(params))  # выпадающее меню
target_combobox.pack()
currency_label = ttk.Label()
currency_label.pack(pady=2, padx=10)

button = Button(text='Получить курс', command=exchange).pack()

base_combobox.bind('<<ComboboxSelected>>', update_base_label1)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

root.mainloop()