import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENT_CORRECT


class TestIngredient:

    def test_get_name_correct_data(self):
        type, name, price = INGREDIENT_CORRECT
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_name() == name
    
    def test_get_price_correct_data(self):
        type, name, price = INGREDIENT_CORRECT
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_price() == price

    def test_get_type_correct_data(self):
        type, name, price = INGREDIENT_CORRECT
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_type() == type

    @pytest.mark.parametrize('type, name, price', [
            (INGREDIENT_CORRECT)
        ]
    )
    def test_initialization_correct_data(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.type == type and ingredient.name == name and ingredient.price == price
