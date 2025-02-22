from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования"""

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                log_message = f"Function {function.__name__} called with arguments: {args}, {kwargs}. Result: {result}"
            except Exception as e:
                log_message = f"Function {function.__name__} raised an error: {e}"
                raise

            if filename:
                with open(filename, "a", encoding="utf-8") as log_file:
                    log_file.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return inner

    return wrapper


@log("log.txt")
def multiply(x: int, y: int) -> int:
    """Функция умножения двух чисел."""
    return x * y


@log("log.txt")
def subtract(x: int, y: int) -> int:
    """Функция вычитания двух чисел."""
    return x - y


@log("log.txt")
def failing_function() -> None:
    """Функция, которая вызывает ошибку."""
    raise ValueError("Test error")
