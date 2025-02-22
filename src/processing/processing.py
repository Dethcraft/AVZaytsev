from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей (операций) по ключу 'state'.

    :param data: Список словарей, описывающих операции.
    :param state: Статус, по которому выполняется фильтрация. По умолчанию 'EXECUTED'.
    :return: Список отфильтрованных операций.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], ascending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей (операций) по ключу 'date'.

    :param data: Список словарей с ключом 'date' в формате 'YYYY-MM-DD'.
    :param ascending: Флаг сортировки по возрастанию. По умолчанию True.
    :return: Список операций, отсортированных по указанному порядку.
    """
    return sorted(
        data,
        key=lambda x: datetime.strptime(x.get('date', ''), '%Y-%m-%d'),
        reverse=not ascending
    )


# Пример использования
if __name__ == '__main__':
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
        {"id": 2, "state": "PENDING", "date": "2023-09-30"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-02"}
    ]

    # Фильтрация по статусу
    filtered_operations = filter_by_state(operations, state="EXECUTED")
    print("Отфильтрованные операции:")
    print(filtered_operations)

    # Сортировка по дате
    sorted_operations = sort_by_date(filtered_operations, ascending=True)
    print("\nОтсортированные операции:")
    print(sorted_operations)

