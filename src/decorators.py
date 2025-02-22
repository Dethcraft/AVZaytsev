def multiply(x: int, y: int) -> int:
    """ Функция умножения двух чисел. """
    result = x * y
    log_message = f"Function multiply called with arguments: {x}, {y}. Result: {result}\n"

    # Логируем в консоль
    print(log_message)

    # Записываем лог в файл
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_message)

    return result


def subtract(x: int, y: int) -> int:
    """ Функция вычитания двух чисел. """
    result = x - y
    log_message = f"Function subtract called with arguments: {x}, {y}. Result: {result}\n"

    # Логируем в консоль
    print(log_message)

    # Записываем лог в файл
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_message)

    return result


def failing_function():
    """ Функция, которая вызывает ошибку. """
    try:
        raise ValueError("Test error")
    except Exception as e:
        error_message = f"Function failing_function raised an error: {e}\n"

        # Логируем ошибку в консоль
        print(error_message)

        # Записываем ошибку в файл
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(error_message)

        raise  # Повторно вызываем исключение
