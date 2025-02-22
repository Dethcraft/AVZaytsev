import os
import sys
import pytest
from src.widget import mask_account_card, get_data

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


def test_mask_account_card():
    assert mask_account_card("card", "4111111111111111") == "4111 11** **** 1111"
    assert mask_account_card("account", "12345678901234567890") == "**34567890"
    with pytest.raises(ValueError):
        mask_account_card("invalid_type", "4111111111111111")


@pytest.mark.parametrize("input_str, expected", [
    ("Transaction on 2023-10-01", "2023-10-01"),
    ("No date here", ""),
    ("Another date: 2023/10/01", "2023-10-01")
])
def test_get_data(input_str, expected):
    assert get_data(input_str) == expected
