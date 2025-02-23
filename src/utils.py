import logging
import os
import json
from typing import List, Dict

# Настройка логирования
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        logger.error(f"Ошибка: файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.debug(f"Прочитано {len(data)} транзакций")
                return data
            else:
                logger.error("Ошибка: JSON-файл содержит не список")
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}")
    except OSError as e:
        logger.error(f"Ошибка при чтении файла: {e}")

    return []
