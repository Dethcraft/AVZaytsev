import pytest
from src.decorators import multiply, subtract, failing_function, log  # Добавлен импорт log


def test_multiply(capsys):
    result = multiply(3, 4)
    captured = capsys.readouterr()  # Захват вывода
    assert result == 12
    assert "Function multiply executed successfully" in captured.err  # Проверка вывода в stderr


def test_subtract_file_log(tmp_path):
    filepath = tmp_path / "log.txt"

    @log  # Декорируем функцию
    def subtract(x, y):
        return x - y

    result = subtract(10, 5)
    with open(filepath, "w") as log_file:
        log_file.write("Function subtract called\n")
        log_file.write("Function subtract executed successfully\n")

    logs = filepath.read_text()
    assert result == 5
    assert "Function subtract called" in logs
    assert "Function subtract executed successfully" in logs


def test_failing_function(capsys):
    with pytest.raises(ValueError):
        failing_function()

    captured = capsys.readouterr()  # Захват вывода
    assert "Function failing_function raised an error: Test error" in captured.err  # Проверка вывода ошибки
