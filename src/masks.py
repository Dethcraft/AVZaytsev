def get_mask_card_number(card_number):
    if not card_number:  # Проверяем пустую строку
        return "Пустая строка"

    if len(card_number) < 4:
        return "***"  # Если слишком короткий номер

    if len(card_number) == 6:
        return card_number[:2] + "****"

    # Маскируем для стандартных номеров карт
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


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
