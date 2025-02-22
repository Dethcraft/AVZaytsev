import unittest
from unittest.mock import patch, mock_open
import json
from src.utils import read_transactions


class TestUtils(unittest.TestCase):

    def test_read_transactions_valid(self):
        mock_data = [{"amount": 100, "currency": "USD"}]

        with patch('builtins.open', mock_open(read_data=json.dumps(mock_data))) as mock_file:
            with patch('os.path.exists', return_value=True):
                result = read_transactions("data/operations.json")

        mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")
        self.assertEqual(result, [{"amount": 100, "currency": "USD"}])


if __name__ == "__main__":
    unittest.main()