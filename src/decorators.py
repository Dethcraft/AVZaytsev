import sys
import functools

def log(func):
    """
    Декоратор для логирования выполнения функций.
    Логирует успешное выполнение или возникновение ошибки с описанием.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Function {func.__name__} executed successfully", file=sys.stderr)  # Лог записывается в stderr
            return result
        except Exception as e:
            print(f"Function {func.__name__} raised an error: {e}", file=sys.stderr)  # Лог ошибки в stderr
            raise  # Повторно выбрасываем исключение
    return wrapper

@log
def multiply(x: int, y: int) -> int:
    return x * y

@log
def subtract(x: int, y: int) -> int:
    return x - y

@log
def failing_function():
    raise ValueError("Test error")