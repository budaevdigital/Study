"""
Задание
---------
Напишите тесты на метод divider() класса Calculator.
Сам метод пока не написан, но есть docstring с его описанием.

Проверьте:
правильно ли работает деление;
выбрасывается ли исключение при делении на 0.

Подсказка
----------
Подготовьте данные для теста методом setUpClass или setUp.
Делить на ноль нельзя.
При попытке разделить на ноль метод должен выбрасывать исключение ZeroDivisionError.
Один тест — одна проверка. Не включайте все проверки в один test case.
"""

import unittest


class Calculator:
    """Производит различные арифметические действия."""
    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        return num1/num2

class TestCalcMethod(unittest.TestCase):
    """
    Тестируем калькулятор деления
    """
    # Следуем паттерну AAA, проводим необходимую настройку(ARRANGE),
    # которая не нарушает принцип DRY
    @classmethod
    def setUpClass(cls) -> None:
        # создаём экземпляр класса
        cls.calc_method = Calculator()

    def test_divider_method(self):
        result = TestCalcMethod.calc_method.divider(10, 5)
        self.assertEqual(result, 2,
            f'{self=} не работает деление с целыми числами')

    def test_divider_on_zero(self):
        # self.assertRaises(ZeroDivisionError, TestCalcMethod.calc_method.divider, 4, 0)
        # а можно использовать и менеджер контекста
        with self.assertRaises(ZeroDivisionError):
            TestCalcMethod.calc_method.divider(4, 0)
        