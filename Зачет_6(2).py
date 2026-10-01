import requests
import tkinter as tk
from tkinter import ttk, messagebox as mb

from PyQt5.QtCore import center

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


def update_currency_label(event):
    code = base_combobox.get()
    name = CRYPTO_NAMES.get(code, code)
    base_label.config(text=name)

    # Сбрасываем прогресс-бар и текст курса
    progress_bar['value'] = 0
    usd_label.config(text="Загрузка...")

    # Имитируем задержку 1 секунду с анимацией прогресс-бара
    animate_progress(0, code)


def animate_progress(current_value, code):
    """Плавно заполняет прогресс-бар за ~1 секунду, затем запрашивает курс."""
    if current_value >= 100:
        # Когда анимация завершена — запрашиваем курс
        rate_usd = get_rate_to_usd(code)
        if rate_usd is not None:
            usd_label.config(text=f"{rate_usd:,.2f} USD")
        else:
            usd_label.config(text="Курс не получен")
        return

    # Шаг анимации (например, каждые 20 мс)
    step = 5
    progress_bar['value'] = current_value + step
    root.after(20, lambda: animate_progress(min(current_value + step, 100), code))


root = tk.Tk()
root.title("Криптик: Курсы криптовалют")
root.geometry("350x350")

# Выбор базовой криптовалюты
tk.Label(root, text="Выберите криптовалюту", font='Arial 12').pack(pady=25, padx=10)

base_combobox = ttk.Combobox(root, values=list(CRYPTO_IDS.keys()), state="readonly", )
base_combobox.pack(pady=2)
base_combobox.set("")

# Метка для названия валюты
base_label = ttk.Label(root, text="", font=("Arial", 12))
base_label.pack(pady=10, padx=10)

# Прогресс-бар (линия загрузки)
progress_bar = ttk.Progressbar(root, mode='determinate', length=145)
progress_bar.pack(pady=10, padx=10)  # Без отступа сверху, сразу под комбобоксом

# Метка для курса USD (опущена на 10 pady ниже прогресс-бара)
usd_label = ttk.Label(root, text="", font=("Arial", 16, "bold"))
usd_label.pack(pady=15, padx=10)

# Связываем событие выбора с обновлением меток
base_combobox.bind("<<ComboboxSelected>>", update_currency_label)

root.mainloop()