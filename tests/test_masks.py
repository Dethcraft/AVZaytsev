from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("4111111111111111") == "4111 **** **** 1111"
    assert get_mask_card_number("123456") == "123456"  # Если номер короче, возвращаем как есть
    assert get_mask_card_number("") == ""  # Пустая строка

def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "***34567890"
    assert get_mask_account("12345678") == "***12345678"
    assert get_mask_account("") == "***"
    assert get_mask_account("123") == "***123"
