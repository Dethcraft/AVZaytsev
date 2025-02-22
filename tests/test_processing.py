import os
import sys
import pytest
from src.processing import sort_by_date


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
        {"id": 2, "state": "PENDING", "date": "2023-09-30"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-02"}
    ]


@pytest.mark.parametrize("ascending, expected_first, expected_last", [
    (True, "2023-09-30", "2023-10-02"),
    (False, "2023-10-02", "2023-09-30"),
])
def test_sort_by_date(sample_operations, ascending, expected_first, expected_last):
    sorted_operations = sort_by_date(sample_operations, ascending=ascending)
    assert sorted_operations[0]["date"] == expected_first
    assert sorted_operations[-1]["date"] == expected_last
