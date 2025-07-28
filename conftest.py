import pytest
from typing import List

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BUN_CORRECT, INGREDIENT_SAUCE_CORRECT, INGREDIENT_FILLING_CORRECT

# Фабрика для создания Burger
@pytest.fixture
def burger_factory():
    def _factory(bun=None, ingredients=None):
        burger = Burger()
        if bun:
            burger.bun = bun
        if ingredients:
            burger.ingredients = ingredients
        return burger
    return _factory

# Бургер с ингридиентами и булками
@pytest.fixture
def burger_full(burger_factory):
    bun_input = Bun(*BUN_CORRECT)
    ingredients_input: List[Ingredient] = [
        Ingredient(*INGREDIENT_SAUCE_CORRECT),
        Ingredient(*INGREDIENT_FILLING_CORRECT)
    ]
    return burger_factory(bun=bun_input, ingredients=ingredients_input)

# Пустой объект бургера
@pytest.fixture
def burger_empty(burger_factory):
    return burger_factory()