"""
Задача
------
Доработайте метод summ: он должен возвращать None, если вызывается с одним аргументом или без аргументов.

Подсказка
---------
Количество переданных аргументов можно узнать с помощью len(args)
"""

import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""
        if len(args) > 1:
            return sum(i for i in args)
        else:
            return None


class TestCalculator(unittest.TestCase):
    """Тестируем Calculator."""
    # Следуем паттерну AAA, проводим необходимую настройку(ARRANGE),
    # которая не нарушает принцип DRY
    @classmethod
    def setUpClass(cls) -> None:
        # создаём экземпляр класса
        cls.calc_method = Calculator()

    def test_sum_with_arguments(self):
        """
        тестируем вызов функции c 3 аргументами
        """        
        result = TestCalculator.calc_method.summ(3, -3, 5)
        self.assertEqual(result, 5,
            f'{self=} функция работает некорректно')

    def test_sum_no_argument(self):
        """
        тестируем вызов функции без аргументов
        """
        result = TestCalculator.calc_method.summ()
        self.assertIsNone(result, 
            f'{self=} у функции нет аргументов для рассчёта')

    def test_sum_one_argument(self):
        """
        тестируем вызов функции с одним аргументом
        """
        result = TestCalculator.calc_method.summ(3)
        self.assertIsNone(result,
            f'{self=} у функции всего один аргумент для рассчёта')
