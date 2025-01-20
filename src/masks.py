def get_mask_card_number(number_card: str) -> str:
    """Функцию маскировки номера банковской карты"""
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(account: str) -> str:
    """Функцию маскировки номера банковского счета"""
    return f"**{account[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
