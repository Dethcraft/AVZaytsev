# Проект "Обработка Операций"

## Описание:
Проект "Обработка Операций" - это Python-приложение для обработки, фильтрации и сортировки данных. Основной функционал включает:
- Фильтрацию данных по статусу `state`;
- Сортировку данных по дате `date`.

## Установка:
1. Клонируйте репозиторий:
   ``` 
   git clone https://github.com/Dethcraft/AVZaytsev.git
   ```
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование:
1. Импортируйте реализованные функции в свой проект:
   ```
   from processing import filter_by_state, sort_by_date
   ```
2. Используйте функции для обработки данных, например:
   ```
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
   ```

## Тестирование

Проект покрыт автотестами. Для запуска тестов используйте команду:
```
pytest
```

Для проверки покрытия тестами выполните:
```
pytest --cov=src --cov-report=html
```

Отчет о покрытии тестами будет создан в папке `htmlcov`. Откройте файл `htmlcov/index.html` в браузере для просмотра.

# Модуль `generators`

Модуль `generators` содержит функции и генераторы для обработки данных, связанных с транзакциями.  
С его помощью можно фильтровать транзакции по валюте, выводить описания операций и генерировать номера карт в заданных диапазонах.

---

## **Функции модуля**

### **1. `filter_by_currency`**
Фильтрует транзакции по указанной валюте и возвращает итератор.

- **Аргументы:**
  - `transactions` — список словарей, представляющих транзакции.
  - `currency` — валюта, по которой выполняется фильтрация (например, `USD`).
- **Возвращает:** Итератор транзакций, соответствующих заданной валюте.

#### Пример использования:
```python
from src.generators import filter_by_currency

transactions = [
    {
        "id": 939719570,
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод организации",
    },
    {
        "id": 873106923,
        "operationAmount": {"currency": {"code": "RUB"}},
        "description": "Перевод со счета на счет",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
# Вывод:
# {'id': 939719570, 'operationAmount': {'currency': {'code': 'USD'}}, 'description': 'Перевод организации'}
```

---

### **2. `transaction_descriptions`**
Генерирует описания операций для каждой транзакции.

- **Аргументы:**
  - `transactions` — список словарей с транзакциями.
- **Возвращает:** Итератор с описаниями операций.

#### Пример использования:
```python
from src.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод с карты на карту"},
]

descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)
# Вывод:
# Перевод организации
# Перевод со счета на счет
# Перевод с карты на карту
```

---

### **3. `card_number_generator`**
Генерирует номера карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне.

- **Аргументы:**
  - `start` — начальное значение диапазона.
  - `stop` — конечное значение диапазона.
- **Возвращает:** Итератор с номерами карт в заданном формате.

#### Пример использования:
```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
# Вывод:
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005
```

---

### **4. `print_transactions`**
Выводит в консоль информацию о транзакциях в удобном формате.

- **Аргументы:**
  - `transactions` — список словарей с транзакциями.
- **Возвращает:** `None`, выводит данные через `print`.

#### Пример использования:
```python
from src.generators import print_transactions

transactions = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Перевод со счета на счет"},
]

print_transactions(transactions)
# Вывод:
# ID: 1, Описание: Перевод организации
# ID: 2, Описание: Перевод со счета на счет
```

---

## Пример входных данных для проверки функций

Для функций `filter_by_currency` и `transaction_descriptions` используйте следующий пример данных:

```python
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]
```

---

## Проверка проекта

### **1. Запуск функций с помощью тестовых данных**
Запустите скрипт и вызовы функций в файле `generators.py`.

### **2. Запуск тестов**
Для проверки правильности работы модулей выполните тесты:
```
pytest tests/
```

### **3. Анализ покрытия кода**
Проверьте покрытие тестами:
```
pytest --cov=src --cov-report=html
```
Откройте файл `htmlcov/index.html` в браузере, чтобы убедиться, что покрытие превышает минимум 80%.


## Проверка стиля:
Убедитесь, что код соответствует стандартам качества:
1. Запустите `flake8` для проверки стиля:
   ```
   flake8 src/
   ```
2. Проверьте аннотацию типов с помощью `mypy`:
   ```
   mypy src/
   ```
3. Сортируйте импорты с использованием `isort`:
   ```
   isort src/
   ```