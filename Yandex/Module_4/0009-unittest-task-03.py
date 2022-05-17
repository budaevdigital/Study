"""
Задание
-------
В коде задания описан метод summ.
Если вызвать этот метод без аргументов, он вернёт ноль,а если передать 
в метод summ один аргумент — он вернёт значение этого аргумента.
Это не лучшее поведение для калькулятора, надо его изменить. 

Методика TDD подразумевает, что сначала пишутся тесты, а потом код.
В этом задании напишите тесты, которые проверяют, что summ
возвращает None, если количество переданных аргументов меньше двух.

Подсказка
---------
В Unittest есть встроенный метод для проверки на None: 
assertIsNone(x)

Маленькие тесты — это всегда хорошо. 

Одна проверка — один тест:
    - test_sum_no_argument — что будет, если функция вызвана без аргументов.
    - test_sum_one_argument — что будет, если функция вызвана с одним аргументом.
"""

import unittest

class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""       
        return sum(i for i in args)


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
