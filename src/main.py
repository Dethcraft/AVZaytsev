from src.file_operations import read_transactions_from_csv, read_transactions_from_excel


def main() -> None:
    csv_transactions = read_transactions_from_csv('../data/transactions.csv')
    excel_transactions = read_transactions_from_excel('../data/transactions_excel.xlsx')

    print("CSV Transactions:")
    print(csv_transactions)

    print("Excel Transactions:")
    print(excel_transactions)


if __name__ == "__main__":
    main()
