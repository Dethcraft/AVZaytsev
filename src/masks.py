import os
import logging

if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    if len(card_number) < 6:
        logger.warning("Длина номера карты меньше 6 символов")
        return card_number
    elif len(card_number) == 16:
        masked = f'{card_number[:4]} **** **** {card_number[-4:]}'
        logger.debug(f"Маскированный номер: {masked}")
        return masked
    else:
        logger.warning("Неизвестный формат номера карты")
        return card_number


def get_mask_account(account_number: str) -> str:
    if not account_number:
        logger.warning("Пустой номер счета")
        return "***"
    elif len(account_number) > 8:
        masked = f'***{account_number[-8:]}'
        logger.debug(f"Маскированный номер счета: {masked}")
        return masked
    else:
        masked = f'***{account_number}'
        logger.debug(f"Маскированный короткий номер счета: {masked}")
        return masked
