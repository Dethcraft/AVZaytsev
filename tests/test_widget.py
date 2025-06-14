from src.widget import (
    mask_account_card,
    get_data_date,
    search_operations,
    count_by_category,
)


def test_mask_account_card():
    assert mask_account_card('card', '4111111111111111') == "4111 11** **** 1111"
    assert mask_account_card('account', '12345678901234567890') == "**34567890"


def test_get_data_date():
    assert get_data_date("Transaction on 2023-10-01") == "2023-10-01"
    assert get_data_date("No date here") == ""


def test_search_operations():
    data = [
        {"description": "Вклад"},
        {"description": "перевод"},
        {"description": "магазин"}
    ]
    assert search_operations(data, "вклад")[0]['description'] == "Вклад"
    assert search_operations(data, "магазин")[0]['description'] == "магазин"
    assert search_operations(data, "нетсовпадений") == []


def test_count_by_category():
    data = [
        {"description": "Вклад"},
        {"description": "Открытие вклада"},
        {"description": "Магазин"}
    ]
    cats = ["вклад", "магазин"]
    result = count_by_category(data, cats)
    assert result["вклад"] == 2
    assert result["магазин"] == 1
