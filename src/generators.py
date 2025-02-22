from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей, представляющих транзакции.
    :param currency: Валюта для фильтрации (например, "USD").
    :yield: Транзакции, соответствующие заданной валюте.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генерирует описания операций для каждой транзакции.

    :param transactions: Список словарей с транзакциями.
    :yield: Описание операции (ключ "description").
    """
    for transaction in transactions:
        description = transaction.get("description", "")
        if isinstance(description, str):
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение диапазона.
    :param stop: Конечное значение диапазона.
    :yield: Сгенерированный номер карты.
    """
    for number in range(start, stop + 1):
        formatted_number = f"{number:016}"  # Заполняем нулями до длины 16 цифр
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"


def print_transactions(transactions: list[dict]) -> None:
    """
    Выводит в консоль информацию о транзакциях.

    :param transactions: Список словарей транзакций.
    """
    for transaction in transactions:
        print(f"ID: {transaction['id']}, Описание: {transaction['description']}")


# Тестирование функционала через print
if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]

    # Пример вызова filter_by_currency
    print("\n=== filter_by_currency ===")
    usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
        print(transaction)

    # Пример вызова transaction_descriptions
    print("\n=== transaction_descriptions ===")
    descriptions = transaction_descriptions(transactions)
    for description in descriptions:
        print(description)

    # Пример вызова card_number_generator
    print("\n=== card_number_generator ===")
    for card_number in card_number_generator(1, 5):
        print(card_number)

    # Пример вызова print_transactions
    print("\n=== print_transactions ===")
    print_transactions(transactions)
