from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("4111111111111111") == "4111 11** **** 1111"
    assert get_mask_card_number("123456") == "12****"
    assert get_mask_card_number("") == ""  # Пустая строка
    assert get_mask_card_number("1234") == "****"  # Короткий номер


def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**34567890"
    assert get_mask_account("123456") == "**123456"
    assert get_mask_account("") == ""  # Пустая строка
    assert get_mask_account("123") == "**123"  # Короткий номер
