import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from src.file_operations import read_transactions_from_csv, read_transactions_from_excel

class TestFileOperations(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_read_transactions_from_csv(self, mock_read_csv):
        mock_data = pd.DataFrame([{'amount': 100, 'currency': 'USD'}])
        mock_read_csv.return_value = mock_data

        transactions = read_transactions_from_csv('dummy_path.csv')
        self.assertEqual(transactions, [{'amount': 100, 'currency': 'USD'}])

    @patch('pandas.read_excel')
    def test_read_transactions_from_excel(self, mock_read_excel):
        mock_data = pd.DataFrame([{'amount': 100, 'currency': 'USD'}])
        mock_read_excel.return_value = mock_data

        transactions = read_transactions_from_excel('dummy_path.xlsx')
        self.assertEqual(transactions, [{'amount': 100, 'currency': 'USD'}])

if __name__ == "__main__":
    unittest.main()