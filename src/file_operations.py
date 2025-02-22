import pandas as pd
from typing import List, Dict, Any, Hashable


def read_transactions_from_csv(file_path: str) -> List[Dict[Hashable, Any]]:
    """Читает финансовые операции из CSV-файла и возвращает список словарей."""
    try:
        data = pd.read_csv(file_path)
        transactions: List[Dict[Hashable, Any]] = data.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict[Hashable, Any]]:
    """Читает финансовые операции из Excel-файла и возвращает список словарей."""
    try:
        data = pd.read_excel(file_path)
        transactions: List[Dict[Hashable, Any]] = data.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []
