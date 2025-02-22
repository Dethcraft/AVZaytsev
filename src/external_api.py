import requests
from typing import Dict

API_KEY = 'YOUR_API_KEY'
EXCHANGE_API_URL = 'https://api.example.com'


def convert_to_rub(transaction: Dict[str, float]) -> float:
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "RUB")

    headers = {'apikey': API_KEY}
    params = {'from': currency, 'to': 'RUB', 'amount': amount}

    try:
        response = requests.get(f"{EXCHANGE_API_URL}/convert", headers=headers, params=params)
        response.raise_for_status()
        exchange_data = response.json()

        result = exchange_data.get('result')
        if result is not None:
            return float(result)

    except requests.RequestException as e:
        print(f"Ошибка API: {e}")
    except ValueError:
        print("Не удалось получить курс.")

    return 0.0
