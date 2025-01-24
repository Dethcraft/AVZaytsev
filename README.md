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
