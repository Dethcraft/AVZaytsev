import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
    print_transactions
)


# Фикстура для тестовых данных
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {"amount": "200.00", "currency": {"code": "RUB"}}
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {"amount": "300.00", "currency": {"code": "USD"}}
        },
    ]


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),
    ("RUB", 1),
    ("EUR", 0),
])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    transactions = list(filter_by_currency(sample_transactions, currency=currency))
    assert len(transactions) == expected_count


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_card_number_generator():
    cards = list(card_number_generator(1, 3))
    assert cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]

    single_card = list(card_number_generator(9999999999999999, 9999999999999999))
    assert single_card == ["9999 9999 9999 9999"]


def test_print_transactions(sample_transactions, capsys):
    print_transactions(sample_transactions)
    # capture the printed output
    captured = capsys.readouterr()

    assert "ID: 1, Описание: Перевод организации" in captured.out
    assert "ID: 2, Описание: Перевод со счета на счет" in captured.out
    assert "ID: 3, Описание: Перевод с карты на карту" in captured.out
