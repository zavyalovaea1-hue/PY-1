import requests
from tkinter import Tk, Label, messagebox as mb
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


def get_rate_to_usd(base_code):
    """Возвращает курс криптовалюты к USD."""
    base_id = CRYPTO_IDS.get(base_code)
    if not base_id:
        return None

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": base_id,
        "vs_currencies": "usd",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        price_usd = data.get(base_id, {}).get("usd")
        if price_usd is None:
            return None
        return price_usd

    except requests.exceptions.Timeout:
        mb.showerror("Ошибка", "Превышено время ожидания ответа от сервера")
    except requests.exceptions.HTTPError as e:
        mb.showerror("Ошибка", f"HTTP-ошибка: {e}")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка", f"Сетевая ошибка: {e}")
    except ValueError as e:
        mb.showerror("Ошибка", f"Не удалось разобрать JSON: {e}")

    return None


def update_base_label(event):
    code = base_combobox.get()
    name = CRYPTO_NAMES.get(code, code)
    base_label.config(text=name)


def show_usd_rate():
    base_code = base_combobox.get().strip()

    if not base_code:
        mb.showwarning("Внимание", "Выберите криптовалюту из списка!")
        return

    rate = get_rate_to_usd(base_code)
    if rate is not None:
        name = CRYPTO_NAMES[base_code]
        message = f"{rate:,.2f} USD за 1 {name} ({base_code})"
        mb.showinfo("Курс к доллару", message)
    else:
        mb.showerror("Ошибка", "Не удалось получить курс. Попробуйте позже.")


root = Tk()
root.title("Криптик: Курс к USD")
root.geometry("350x280")

# Выбор базовой криптовалюты
Label(root, text="Выберите криптовалюту").pack(pady=15, padx=10)
base_combobox = ttk.Combobox(root, values=list(CRYPTO_IDS.keys()), state="readonly")
base_combobox.pack()
base_combobox.set("")

# Метка с названием выбранной валюты
base_label = ttk.Label(root, text="", font=("Arial", 11))
base_label.pack(pady=5, padx=10)

btn = ttk.Button(root, text="Показать курс к USD", command=show_usd_rate)
btn.pack(pady=20)

base_combobox.bind("<<ComboboxSelected>>", update_base_label)

root.mainloop()
