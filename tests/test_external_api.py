import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub

class TestExternalAPI(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_conversion_usd_to_rub(self, mock_get):
        """Тестируем конвертацию из USD в RUB"""
        mock_response = {"rates": {"RUB": 75.0}}
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = lambda: None

        transaction = {"amount": 10, "currency": "USD"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 750.0)

    def test_conversion_rub_to_rub(self):
        """Тестируем, что RUB -> RUB не изменяет сумму"""
        transaction = {"amount": 100, "currency": "RUB"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 100.0)

    @patch("src.external_api.requests.get")
    def test_conversion_invalid_currency(self, mock_get):
        """Тестируем, что при неизвестной валюте возвращается 0.0"""
        mock_response = {"rates": {}}  # Нет курса
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = lambda: None

        transaction = {"amount": 10, "currency": "XYZ"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 0.0)

if __name__ == "__main__":
    unittest.main()