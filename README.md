# Проект "Обработка Операций"

## Описание

Проект "Обработка Операций" — это Python-приложение для обработки, фильтрации, сортировки и поиска данных о финансовых операциях.

**Основной функционал включает:**
- Фильтрацию данных по статусу поля `state`;
- Сортировку данных по дате поля `date`;
- Загрузку операций из файлов CSV и Excel;
- Сохранение обработанных операций в файлы CSV и Excel;
- Поиск операций по описанию с использованием регулярных выражений.

---

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/Dethcraft/AVZaytsev.git

2. Установите зависимости:
   pip install -r requirements.txt

---

## Использование

### Основные функции обработки данных

Импортируйте функции в свой проект:
from processing import filter_by_state, sort_by_date

Пример использования:
operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
    {"id": 2, "state": "PENDING", "date": "2023-09-30"},
    {"id": 3, "state": "EXECUTED", "date": "2023-10-02"}
]

# Фильтруем по статусу
filtered_operations = filter_by_state(operations, state="EXECUTED")

# Сортируем по дате
sorted_operations = sort_by_date(filtered_operations, ascending=True)
print(sorted_operations)

---

### Работа с файлами CSV и Excel

#### Загрузка данных

Импортируйте функции для загрузки:
from file_operations import read_operations_from_csv, read_operations_from_excel

Загрузка из CSV:
operations = read_operations_from_csv('transactions.csv')

Загрузка из Excel:
operations = read_operations_from_excel('transactions.xlsx')

#### Сохранение данных

Импортируйте функции для сохранения:
from file_operations import save_operations_to_csv, save_operations_to_excel

Сохранение в CSV:
save_operations_to_csv(operations, 'export.csv')

Сохранение в Excel:
save_operations_to_excel(operations, 'export.xlsx')

---

### Поиск операций в описании с помощью регулярных выражений

Импортируйте функцию для поиска:
from widget import search_operations

Использование:

operations = [
    {"id": 1, "description": "Открытие вклада"},
    {"id": 2, "description": "Перевод на карту"},
    {"id": 3, "description": "Оплата телефона"},
    {"id": 4, "description": "Покупка в магазине"},
]

# Найти все операции, где в описании есть слово "вклад" или что-то подходящее под регулярку
matches = search_operations(operations, "вклад")
print(matches)

Описание функции:
search_operations(data, pattern)
- data: список словарей с ключом description
- pattern: строка или регулярное выражение

Функция возвращает все операции, для которых значение поля description содержит подстроку или подходит под регулярное выражение (без учета регистра).

---

## Тестирование

Проект покрыт автотестами. Для запуска тестов используйте команду:
pytest

Для проверки покрытия тестами выполните:
pytest --cov=src --cov-report=html

Отчет о покрытии тестами будет создан в папке htmlcov. Откройте файл htmlcov/index.html в браузере для просмотра.

---

## Проверка стиля

Убедитесь, что код соответствует стандартам качества.

Запуск проверки стиля:
flake8 src/

Проверка аннотаций типов:
mypy src/

Автоматическая сортировка импортов:
isort src/