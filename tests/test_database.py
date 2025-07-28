from typing import List

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    """
    Тестирование функциональности класса Database.
    Проверяет корректность работы с базой данных:
    - Инициализация и наполнение данными
    - Получение списков доступных булочек и ингредиентов
    - Проверка типов и наполненности возвращаемых данных
    """

    def test_available_buns_correct_data_return_non_empty_list(self):
        """
        Проверяет, что метод available_buns() возвращает непустой список объектов Bun
        """
        database = Database()

        buns = database.available_buns()

        assert len(buns) > 0 and isinstance(buns, List) and type(buns[0]) == Bun
    
    def test_available_ingredients_correct_data_return_non_empty_list(self):
        """
        Проверяет, что метод available_ingredients() возвращает непустой список объектов Ingredient
        """
        database = Database()

        ingredients = database.available_ingredients()

        assert len(ingredients) > 0 and isinstance(ingredients, List) and type(ingredients[0]) == Ingredient

    def test_init_correct_data_lists_populated(self):
        """
        Проверяет, что при инициализации Database заполняются списки булочек и ингредиентов
        """
        database = Database()

        assert len(database.buns) > 0 and len(database.ingredients) > 0
