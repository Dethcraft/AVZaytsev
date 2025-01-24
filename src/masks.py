def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры видимыми.
    Корректно форматирует пробелы.

    Пример:
        "4111111111111111" -> "4111 11** **** 1111"
    """
    if len(card_number) < 6:  # Если длина номера карты меньше 6 символов
        return "*" * len(card_number)
    elif len(card_number) > 12:  # Для длинных номеров
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return masked_number
    else:  # Для номеров средней длины
        return f"{card_number[:2]}****"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 или 8 символов.

    Пример:
        "12345678901234567890" -> "**34567890"
    """
    if not account_number:  # Если строка пустая
        return ""
    elif len(account_number) > 8:
        return f"**{account_number[-8:]}"  # Оставляем последние 8 символов
    else:
        return f"**{account_number}"  # Маскируем все, кроме короткого номера


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
