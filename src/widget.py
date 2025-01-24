import re
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Примеры входных данных:
card_and_account_numbers = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """

date = "2018-07-11T02:26:18.671407"


def mask_account_card(card_type: str, number: str) -> str:
    """
    Маскирует номер карты или счета.

    :param card_type: Тип данных ('card' или 'account').
    :param number: Номер карты или счета.
    :return: Маскированный номер.
    """
    if card_type == "card":
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    elif card_type == "account":
        return f"**{number[-8:]}"
    else:
        raise ValueError("Invalid card type")


def get_data(input_str: str) -> str:
    """
    Извлекает дату в формате 'YYYY-MM-DD' из строки.
    Приводит дату к стандартному формату 'YYYY-MM-DD'.

    :param input_str: Входная строка с потенциальной датой.
    :return: Дата в формате 'YYYY-MM-DD' или пустая строка, если дата не найдена.
    """
    match = re.search(r'(\d{4})[-/](\d{2})[-/](\d{2})', input_str)
    if match:
        date = match.group(0).replace('/', '-')
        return date
    return ""
