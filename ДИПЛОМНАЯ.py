import requests

from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

# Словарь: символ → CoinGecko ID
CRYPTO_IDS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "XRP": "ripple",
    "ADA": "cardano",
    "SOL": "solana",
    "DOGE": "dogecoin",
    "DOT": "polkadot",
    "AVAX": "avalanche",
    "LINK": "chainlink",
    "LTC": "litecoin",
}

# Словарь: символ → красивое название для GUI
CRYPTO_NAMES = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "XRP": "Ripple",
    "ADA": "Cardano",
    "SOL": "Solana",
    "DOGE": "Dogecoin",
    "DOT": "Polkadot",
    "AVAX": "Avalanche",
    "LINK": "Chainlink",
    "LTC": "Litecoin",
}


def get_rate(base_code, target_code):
    """Возвращает курс: сколько target_code стоит 1 base_code."""
    base_id = CRYPTO_IDS.get(base_code)
    target_id = CRYPTO_IDS.get(target_code)

    if not base_id or not target_id:
        mb.showerror("Ошибка", f"Неизвестная криптовалюта: {base_code} или {target_code}")
        return None

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": f"{base_id},{target_id}",
        "vs_currencies": "usd",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        base_price = data.get(base_id, {}).get("usd")
        target_price = data.get(target_id, {}).get("usd")

        if base_price is None or target_price is None:
            mb.showerror("Ошибка", "Не удалось получить цены от API")
            return None

        # Курс: сколько target стоит 1 base
        rate = target_price / base_price
        return rate

    except requests.exceptions.Timeout:
        mb.showerror("Ошибка", "Превышено время ожидания ответа от сервера")
    except requests.exceptions.HTTPError as e:
        mb.showerror("Ошибка", f"HTTP-ошибка: {e}")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Сетевая ошибка: {e}")
    except ValueError as e:
        mb.showerror("Ошибка", f"Не удалось разобрать JSON: {e}")
    return None


def update_currency_label(event):
    code = target_combobox.get()
    name = CRYPTO_NAMES.get(code, code)
    currency_label.config(text=name)


def update_base_label1(event):
    code = base_combobox.get()
    name = CRYPTO_NAMES.get(code, code)
    base_label1.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code1 = base_combobox.get()

    if not target_code:
        mb.showwarning("Внимание", "Выберите целевую криптовалюту")
        return
    if not base_code1:
        mb.showwarning("Внимание", "Выберите базовую криптовалюту")
        return

    rate1 = get_rate(base_code1, target_code)
    if rate1 is not None:
        base = CRYPTO_NAMES[base_code1]
        target = CRYPTO_NAMES[target_code]
        message = f" {rate1:.8f} {base} за 1 {target}\n"
        mb.showinfo("Курс обмена", message)
    else:
        mb.showerror("Ошибка", "Не удалось получить курс")


root = Tk()
root.title("Криптик: курсы криптовалют")
root.geometry("350x420")

# Базовая криптовалюта
Label(text="Базовая криптовалюта").pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=list(CRYPTO_IDS.keys()))
base_combobox.pack()
base_combobox.set(" ")
base_label1 = ttk.Label()
base_label1.pack(pady=5, padx=10)

# Целевая криптовалюта
Label(text="Целевая криптовалюта").pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(CRYPTO_IDS.keys()))
target_combobox.pack()
target_combobox.set(" ")
currency_label = ttk.Label()
currency_label.pack(pady=5, padx=10)

Button(text="Получить курс", command=exchange).pack(pady=10)

base_combobox.bind("<<ComboboxSelected>>", update_base_label1)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

root.mainloop()