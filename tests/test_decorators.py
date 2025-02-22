import pytest
import os
from src.decorators import multiply, subtract, failing_function


def test_multiply():
    """ Проверяем работу функции multiply. """
    result = multiply(3, 4)
    assert result == 12


def test_subtract():
    """ Проверяем работу функции subtract. """
    result = subtract(10, 5)
    assert result == 5


def test_failing_function():
    """ Проверяем, что функция бросает исключение. """
    with pytest.raises(ValueError):
        failing_function()


def test_log_file():
    """ Проверяем, записывается ли лог в файл. """
    log_file = "log.txt"

    # Удаляем файл перед тестом, если он существует
    if os.path.exists(log_file):
        os.remove(log_file)

    multiply(2, 3)  # Должен записать лог в файл log.txt

    with open(log_file, "r", encoding="utf-8") as f:
        logs = f.read()

    assert "Function multiply called with arguments" in logs
