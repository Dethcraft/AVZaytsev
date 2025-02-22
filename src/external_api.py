import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_CURRENCY = os.getenv("BASE_CURRENCY", "RUB")
EXCHANGE_API_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму в рубли.

    :param transaction: Словарь с "amount" и "currency".
    :return: Сумма в рублях (float)
    """
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    headers = {'apikey': API_KEY}
    params = {"base": currency, "symbols": BASE_CURRENCY}

    try:
        response = requests.get(EXCHANGE_API_URL, headers=headers, params=params)
        response.raise_for_status()
        exchange_data = response.json()

        rate = exchange_data['rates'].get(BASE_CURRENCY)
        if rate is None:
            raise ValueError("Не удалось получить курс.")

        return float(amount) * rate

    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Ошибка API: {e}")
        return 0.0
