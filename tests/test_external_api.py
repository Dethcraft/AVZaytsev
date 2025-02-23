import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub

class TestExternalAPI(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_conversion_rub_to_rub(self, mock_get):
        mock_response = {'result': 100}
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = lambda: None

        transaction = {"amount": 100, "currency": "RUB"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 100.0)

    @patch('src.external_api.requests.get')
    def test_conversion_invalid_currency(self, mock_get):
        mock_response = {}
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = lambda: None

        transaction = {"amount": 100, "currency": "XYZ"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 0.0)

if __name__ == "__main__":
    unittest.main()