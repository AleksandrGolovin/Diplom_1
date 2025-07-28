import pytest
from praktikum.bun import Bun
from data import BUN_CORRECT


class TestBun:
    """
    Тестирование функциональности класса Bun.
    Проверяет корректность работы с различными типами данных:
    - Стандартные валидные данные
    - Граничные случаи (пустые строки, нулевые значения)
    """
    def test_get_name_correct_data(self):
        """
        Проверка получения названия булочки при корректных данных.
        Убеждаемся, что метод get_name() возвращает ожидаемое значение,
        соответствующее переданному при инициализации объекта.
        """
        name, price = BUN_CORRECT
        bun = Bun(name, price)

        assert bun.get_name() == name
    
    def test_get_price_correct_data(self):
        """
        Проверка получения цены булочки при корректных данных.
        Убеждаемся, что метод get_price() возвращает значение цены,
        идентичное переданному при создании объекта.
        """
        name, price = BUN_CORRECT
        bun = Bun(name, price)

        assert bun.get_price() == price

    @pytest.mark.parametrize('name, price', [
            (BUN_CORRECT),
            (BUN_CORRECT[0], 0),
            ("", BUN_CORRECT[1]),
            ("", 0)
        ]
    )
    def test_initialization_correct_data(self, name, price):
        """
        Параметризованная проверка инициализации объекта с разными данными.
        Тестирует комбинации:
        1. Валидные данные 
        2. Граничные значения (0, пустая строка)
        Убеждаемся, что атрибуты сохраняют переданные значения.
        """
        bun = Bun(name, price)

        assert bun.name == name and bun.price == price
