from widget import (
    mask_account_card,
    get_data_date,
    search_operations,
    count_by_category,
)


def main() -> None:
    # Демонстрация работы mask_account_card и get_data_date
    print(mask_account_card('card', '4111111111111111'))
    print(mask_account_card('account', '12345678901234567890'))
    print(get_data_date('Transaction on 2023-10-01'))
    print(get_data_date('No date'))

    # Основная часть домашки: регулярки и категории
    operations = [
        {"id": 1, "description": "Открытие вклада"},
        {"id": 2, "description": "Перевод на карту"},
        {"id": 3, "description": "Оплата телефона"},
        {"id": 4, "description": "Покупка в магазине"},
    ]

    print("\nДобро пожаловать в анализатор банковских операций!\n")
    pattern = input("Введите слово или регулярное выражение для поиска по описанию: ").strip()
    found = search_operations(operations, pattern)
    print("\nРезультаты поиска:")
    if found:
        for op in found:
            print(op)
    else:
        print("Совпадений не найдено.")

    categories = ["вклад", "перевод", "магазин", "телефон"]
    counts = count_by_category(operations, categories)
    print("\nСтатистика по категориям:")
    for cat, cnt in counts.items():
        print(f"{cat}: {cnt}")


if __name__ == "__main__":
    main()
