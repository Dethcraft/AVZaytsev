import re
from collections import Counter
from typing import List, Dict


def mask_account_card(card_type: str, number: str) -> str:
    """
    Маскирует номер карты или счета.
    :param card_type: Тип данных ('card' или 'account').
    :param number: Номер карты или счета.
    :return: Маскированный номер.
    """
    if card_type == 'card':
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    elif card_type == 'account':
        return f"**{number[-8:]}"
    else:
        raise ValueError("Invalid card type")


def get_data_date(input_str: str) -> str:
    """
    Извлекает дату в формате 'YYYY-MM-DD' из строки.
    :param input_str: Входная строка с потенциальной датой.
    :return: Дата в формате 'YYYY-MM-DD' или пустая строка.
    """
    match = re.search(r'(\d{4})[-/.](\d{2})[-/.](\d{2})', input_str)
    if match:
        date = match.group(0).replace('/', '-').replace('.', '-')
        return date
    return ""


def search_operations(data: List[Dict], pattern: str) -> List[Dict]:
    """
    Возвращает список операций, где 'description' соответствует регулярному выражению pattern (без учёта регистра).
    """
    regex = re.compile(pattern, re.IGNORECASE)
    return [op for op in data if 'description' in op and regex.search(op['description'])]


def count_by_category(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает количество операций по категориям (категория ищется как подстрока в description).
    """
    counter: Counter = Counter()
    for cat in categories:
        counter[cat] = sum(
            cat.lower() in op.get('description', '').lower()
            for op in data
        )
    return dict(counter)
