# Проект "Обработка Операций"

## Описание

Проект "Обработка Операций" — это Python-приложение для обработки, фильтрации и сортировки данных о финансовых операциях.

**Основной функционал включает:**
- Фильтрацию данных по статусу поля `state`;
- Сортировку данных по дате поля `date`;
- Загрузку операций из файлов CSV и Excel;
- Сохранение обработанных операций в файлы CSV и Excel.

---

## Установка

1. Клонируйте репозиторий: 
```
2. git clone https://github.com/Dethcraft/AVZaytsev.git
```
2. Установите зависимости:
```
3. pip install -r requirements.txt
```
---

## Использование

### Основные функции обработки данных

Импортируйте функции в свой проект:
```
from processing import filter_by_state, sort_by_date
```
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
```
from file_operations import read_operations_from_csv, read_operations_from_excel
```
Загрузка из CSV:
```   
operations = read_operations_from_csv('transactions.csv')
```
Загрузка из Excel:
```   
operations = read_operations_from_excel('transactions.xlsx')
```
#### Сохранение данных

Импортируйте функции для сохранения:
```
from file_operations import save_operations_to_csv, save_operations_to_excel
```
Сохранение в CSV:
```   
save_operations_to_csv(operations, 'export.csv')
```
Сохранение в Excel:
```   
save_operations_to_excel(operations, 'export.xlsx')
```
---

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

---

## Проверка стиля

Убедитесь, что код соответствует стандартам качества.

Запуск проверки стиля:
``` 
flake8 src/
```
Проверка аннотаций типов:
```    
mypy src/
```
Автоматическая сортировка импортов:
```   
 isort src/
```