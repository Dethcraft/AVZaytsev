import functools
import logging
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функции, её результатов и ошибок.

    :param filename: Имя файла для записи логов. Если None, логи выводятся в консоль.
    :return: Обёртка для декорируемой функции.
    """
    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        # Очищаем предыдущие обработчики для данного логгера
        if logger.hasHandlers():
            logger.handlers.clear()

        # Настройка обработчика
        if filename:
            handler = logging.FileHandler(filename, mode='w')
        else:
            handler = logging.StreamHandler()  # Вывод в stderr (основной для capsys)

        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Отключение распространения на родительские логгеры
        logger.propagate = False

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                logger.info(f"Function {func.__name__} called with args={args}, kwargs={kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"Function {func.__name__} executed successfully, result={result}")
                return result
            except Exception as e:
                logger.error(f"Function {func.__name__} raised an error: {e}. Inputs: args={args}, kwargs={kwargs}")
                raise e

        return wrapper

    return decorator