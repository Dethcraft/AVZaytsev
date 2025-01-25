import pytest
from src.decorators import log


@log()
def multiply(x: int, y: int) -> int:
    return x * y


@log(filename="testlog.txt")
def subtract(x: int, y: int) -> int:
    return x - y


@log()
def failing_function():
    raise ValueError("Test error")


def test_multiply(capsys):
    result = multiply(3, 4)
    captured = capsys.readouterr()  # Захват вывода
    assert result == 12
    assert "Function multiply executed successfully" in captured.err  # Проверка вывода в поток stderr


def test_subtract_file_log(tmp_path):
    filepath = tmp_path / "log.txt"

    @log(filename=filepath)
    def subtract(x, y):
        return x - y

    result = subtract(10, 5)
    with open(filepath, "r") as log_file:
        logs = log_file.read()
    assert result == 5
    assert "Function subtract called" in logs
    assert "Function subtract executed successfully" in logs


def test_failing_function(capsys):
    with pytest.raises(ValueError):
        failing_function()

    captured = capsys.readouterr()  # Захват вывода
    assert "Function failing_function raised an error" in captured.err
