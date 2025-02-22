import json
import os
from typing import List


def read_transactions(file_path: str) -> List[dict]:
    """
    Читает JSON-файл с банковскими операциями.

    :param file_path: Путь к JSON-файлу.
    :return: Список транзакций или []
    """
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        print(f"[Ошибка] Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # Загружаем JSON
            data = json.load(file)

            # Проверяем, что это список
            if isinstance(data, list):
                return data
            else:
                print("[Ошибка] JSON-файл содержит не список!")
                return []

    except json.JSONDecodeError as e:
        print(f"[Ошибка] Ошибка декодирования JSON: {e}")
    except OSError as e:
        print(f"[Ошибка] Ошибка при чтении файла: {e}")

    return []
