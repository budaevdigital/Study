"""
Вот несколько самых популярных методов класса TestCase в Unittest:
    - assertEqual(a, b) a == b
    - assertNotEqual(a, b) a != b
    - assertTrue(x) bool(x) is True
    - assertFalse(x) bool(x) is False
    - assertIs(a, b) a is b
    - assertIsNot(a, b) a is not b
    - assertIsNone(x) x is None
    - assertIsNotNone(x) x is not None
    - assertIn(a, b) a in b
    - assertNotIn(a, b) a not in b
    - assertIsInstance(a, b) isinstance(a, b)
    - assertNotIsInstance(a, b) not isinstance(a, b)
Все эти методы могут в качестве необязательного последнего 
аргумента содержать текст сообщения об ошибке.


Unittest позволяет пропускать (не выполнять) классы тестов и 
отдельные тесты. Для этого в библиотеке есть специальные декораторы:
    @unittest.skip(reason) — пропустить тест. В параметре reason описывается причина пропуска.
    @unittest.skipIf(condition, reason) — пропустить тест, если условие condition истинно.
    @unittest.skipUnless(condition, reason) — пропустить тест, если условие condition ложно.

Можно отмаркировать тест меткой «тест не работает, но это так и задумано».
    @unittest.expectedFailure — ставит на тесте отметку «ожидаемая ошибка».


Для получения подробного отчёта можно вызвать 
юниттест из консоли с флагом -v (--verbose, «подробно»).

python3 -m unittest -v 0005-unittest-teory-01.py

"""

import sys 
import unittest  

class TestExample(unittest.TestCase):     
	"""Демонстрирует возможности по пропуску тестов."""
	
	@unittest.skip('Этот тест мы просто пропускаем')     
	def test_show_msg(self):         
		self.assertTrue(False, 'Значение должно быть истинным')
		
	@unittest.skipIf(sys.version_info.major == 3 and sys.version_info.minor == 9,
		'Пропускаем, если питон 3.9')     
	def test_python3_9(self):         
		# Тест будет запущен, только если версия питона отлична от 3.9.         
		# В условиях можно проверять версии библиотек, доступность внешних сервисов,         
		# время или дату - любые данные         
		pass      
	
	@unittest.skipUnless(sys.platform.startswith('linux'), 
		'Тест только для Linux')     
	def test_linux_support(self):         
		# Тест будет запущен только в Linux         
		pass      
		
	@unittest.expectedFailure     
	def test_fail(self):         
		self.assertTrue(False, 'Ожидаем истинное значение')  


class TestSeriesSum(unittest.TestCase):
    """Тестируем series_sum."""

    def test_mixed_numbers(self):  # Это - test case
        # Вызов тестируемой функции
        call = series_sum([1, 2.5, 3, 4])
        # Ожидаемый результат
        result = '12.534'
        # Проверка: идентичен ли результат вызова ожидаемому результату
        self.assertEqual(
            call, result, 'Функция series_sum() не работает со списком чисел'
        )

    def test_mixed_numbers_strings(self):  # И это - test case
        call = series_sum([1, 'fff', 3, 4])
        result = '1fff34'
        self.assertEqual(
            call, result, 'Функция series_sum не работает со смешанным списком'
        )

    def test_empty(self):  # И это - тоже test case
        call = series_sum([])
        result = ''
        self.assertEqual(
            call, result, 'Функция series_sum не работает с пустым списком'
        )


def series_sum(incoming):
    """Конкатенирует все элементы списка, приводя их к строкам."""
    return ''.join(str(i) for i in incoming) 



if __name__ == '__main__':     
	unittest.main()
