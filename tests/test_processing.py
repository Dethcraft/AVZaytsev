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


def test_sort_by_date(sample_operations):
    sorted_asc = sort_by_date(sample_operations, ascending=True)
    assert sorted_asc[0]["date"] == "2023-09-30"
    assert sorted_asc[-1]["date"] == "2023-10-02"

    sorted_desc = sort_by_date(sample_operations, ascending=False)
    assert sorted_desc[0]["date"] == "2023-10-02"
    assert sorted_desc[-1]["date"] == "2023-09-30"
