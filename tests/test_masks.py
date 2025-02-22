import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("4111111111111111", "4111 11** **** 1111"),
    ("123456", "12****"),
    ("", "Пустая строка"),  # Оставляем, если функция будет исправлена
    ("123", "***"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected
