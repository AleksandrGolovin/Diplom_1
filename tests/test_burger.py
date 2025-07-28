from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BUN_CORRECT, INGREDIENT_SAUCE_CORRECT, INGREDIENT_FILLING_CORRECT


class TestBurger:
    """
    Тестирование функциональности класса Burger.
    Проверяет корректность работы с бургерами:
    - Установка булочек
    - Добавление/удаление/перемещение ингредиентов
    - Расчет общей стоимости
    - Формирование чека
    - Поведение при разных комбинациях данных
    """

    def test_set_buns_correct_data_bun_set_successfully(self):
        """
        Проверяет, что метод set_buns() корректно устанавливает булочку для бургера
        """
        bun = Bun(*BUN_CORRECT)
        burger = Burger()

        burger.set_buns(bun)

        assert burger.bun and burger.bun.name == bun.name and burger.bun.price == bun.price

    def test_add_ingredient_correct_data_ingredient_added(self):
        """
        Проверяет, что метод add_ingredient() добавляет ингредиент в список ингредиентов бургера
        """
        ingredient = Ingredient(*INGREDIENT_SAUCE_CORRECT)
        burger = Burger()
        
        burger.add_ingredient(ingredient)
        ingredients = burger.ingredients

        assert len(ingredients) == 1 and ingredients[0].name == ingredient.name and ingredients[0].type == ingredient.type and ingredients[0].price == ingredient.price

    def test_remove_ingredient_correct_data_ingredient_removed(self):
        """
        Проверяет, что метод remove_ingredient() удаляет ингредиент из списка ингредиентов по индексу
        """
        ingredient = Ingredient(*INGREDIENT_SAUCE_CORRECT)
        burger = Burger()
        burger.ingredients.append(ingredient)
        
        burger.remove_ingredient(0)
        ingredients = burger.ingredients

        assert len(ingredients) == 0

    def test_move_ingredient_correct_data_ingredient_moved(self):
        """
        Проверяет, что метод move_ingredient() перемещает ингредиент на новую позицию в списке
        """
        burger = Burger()
        ingredient_0 = Ingredient(*INGREDIENT_SAUCE_CORRECT)
        ingredient_1 = Ingredient(*INGREDIENT_FILLING_CORRECT)
        burger.ingredients.append(ingredient_0)
        burger.ingredients.append(ingredient_1)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[1].type == ingredient_0.type
    
    def test_get_price_correct_data_return_correct_sum(self):
        """
        Проверяет, что метод get_price() возвращает корректную сумму цен булочки (учтённой дважды) и всех ингредиентов
        """
        burger = Burger()
        bun = Bun(*BUN_CORRECT)
        burger.bun = bun
        ingredient_0 = Ingredient(*INGREDIENT_SAUCE_CORRECT)
        ingredient_1 = Ingredient(*INGREDIENT_FILLING_CORRECT)
        burger.ingredients.append(ingredient_0)
        burger.ingredients.append(ingredient_1)
        manual_price = bun.price * 2 + ingredient_0.price + ingredient_1.price

        price = burger.get_price()

        assert price == manual_price

    def test_get_receipt_correct_data_return_valid_receipt_lines_count(self):
        """
        Проверяет, что метод get_receipt() возвращает чек с ожидаемым количеством строк
        """
        burger = Burger()
        bun = Bun(*BUN_CORRECT)
        burger.bun = bun   # 2 строки
        ingredient_0 = Ingredient(*INGREDIENT_SAUCE_CORRECT)
        ingredient_1 = Ingredient(*INGREDIENT_FILLING_CORRECT)
        burger.ingredients.append(ingredient_0)  # 1 строка
        burger.ingredients.append(ingredient_1)  # 1 строка

        receipt = burger.get_receipt()  # +2 строки на price с отступом

        assert len(receipt.split('\n')) == 6