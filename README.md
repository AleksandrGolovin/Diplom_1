## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

---

## Diplom_1: Stellar Burgers unit testing

Проект содержит юнит-тесты для модулей бургерной "Stellar Burgers". Тесты проверяют функциональность основных классов системы:
- Булочка (Bun)
- Ингредиент (Ingredient)
- Бургер (Burger)
- База данных (Database)

Тесты написаны с использованием фреймворка pytest и покрывают основные сценарии работы с объектами бургерной.

### Тестовые классы

#### 1. TestBun (`test_bun.py`)
Тестирует функциональность класса `Bun` (булочка):
- Проверка получения названия булочки (`test_get_name_correct_data_return_correct_name`)
- Проверка получения цены булочки (`test_get_price_correct_data_return_correct_price`)
- Проверка инициализации объекта с разными типами данных (`test_init_correct_data_attributes_set_correctly`)

#### 2. TestIngredient (`test_ingredient.py`)
Тестирует функциональность класса `Ingredient` (ингредиент):
- Проверка получения названия ингредиента (`test_get_name_correct_data_return_correct_name`)
- Проверка получения цены ингредиента (`test_get_price_correct_data_return_correct_price`)
- Проверка получения типа ингредиента (`test_get_type_correct_data_return_correct_type`)
- Проверка инициализации объекта (`test_init_correct_data_attributes_set_correctly`)

#### 3. TestBurger (`test_burger.py`)
Тестирует функциональность класса `Burger` (бургер):
- Установка булочек (`test_set_buns_correct_data_bun_set_successfully`)
- Добавление ингредиентов (`test_add_ingredient_correct_data_ingredient_added`)
- Удаление ингредиентов (`test_remove_ingredient_correct_data_ingredient_removed`)
- Перемещение ингредиентов (`test_move_ingredient_correct_data_ingredient_moved`)
- Расчет стоимости (`test_get_price_correct_data_return_correct_sum`)
- Формирование чека (`test_get_receipt_correct_data_return_valid_receipt_lines_count`)

#### 4. TestDatabase (`test_database.py`)
Тестирует функциональность класса `Database` (база данных):
- Получение списка булочек (`test_available_buns_correct_data_return_non_empty_list`)
- Получение списка ингредиентов (`test_available_ingredients_correct_data_return_non_empty_list`)
- Проверка инициализации базы данных (`test_init_correct_data_lists_populated`)

### Фикстуры (`conftest.py`)

Фикстуры предоставляют предустановленные данные для тестов:

1. **burger_factory**  
   Фабрика для создания объектов Burger:
   - Может создавать пустой бургер
   - Может создавать бургер с указанной булочкой и ингредиентами

2. **burger_full**  
   Создает полностью собранный бургер:
   - Булочка: "baguette" (цена 100)
   - Ингредиенты: 
     - Соус "hot sauce" (цена 100)
     - Начинка "cutlet" (цена 100)

3. **burger_empty**  
   Создает пустой объект бургера без булочки и ингредиентов