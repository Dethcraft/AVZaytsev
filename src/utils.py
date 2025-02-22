import os
import json
from typing import List, Dict


def read_transactions(file_path: str) -> List[Dict]:
    """Читает JSON-файл и возвращает список транзакций."""
    if not os.path.exists(file_path):
        print(f"Ошибка: файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # Загружаем JSON
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("Ошибка: JSON-файл содержит не список")
    except json.JSONDecodeError as e:
        print(f"Ошибка: Ошибка декодирования JSON: {e}")
    except OSError as e:
        print(f"Ошибка: Ошибка при чтении файла: {e}")

    return []
