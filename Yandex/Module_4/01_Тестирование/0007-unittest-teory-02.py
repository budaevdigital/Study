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
    - assertRaises(exc, fun, *args, **kwds) — fun(*args, **kwds) порождает
        исключение exc
    - assertRaisesRegex(exc, r, fun, *args, **kwds) — fun(*args, **kwds) порождает 
        исключение exc и сообщение соответствует регулярному выражению r
Все эти методы могут в качестве необязательного последнего 
аргумента содержать текст сообщения об ошибке.

====================================================
Паттерн ААА:

ARRANGE -> ACT -> ASSERT
(Настройка) -> (Выполнение) -> (Проверка)
====================================================

Чтобы упростить код и не повторяться — в Unittest есть встроенные методы фикстур.

test fixtures (на сленге — «фикстуры») — это фиксированные объекты и данные 
для выполнения тестов. Перед началом теста в коде создаются объекты и данные, 
на которых будет проведено тестирование.

Например, фикстурами может быть:
    - содержимое базы данных,
    - набор переменных среды,
    - набор файлов с необходимым содержанием.

Фикстуры передаются в тест при запуске тестирования и никак не влияют
на данные проекта.

setUp()
--------
Для создания фикстур чаще всего используют метод setUp().
Это встроенный метод Unittest, он автоматически вызывается перед
запуском каждого test case

tearDown()   
----------     
Вызывается после каждого теста.   

@classmethod
setUpClass(cls)
---------------
Предназначен для установки фикстур,
но он вызывается лишь один раз, перед запуском всех test case класса.
setUpClass() — это «метод класса», его обязательно декорировать(@classmethod),
а его первый аргумент должен называться (cls)

@classmethod     
tearDownClass(cls)
------------------
Вызывается один раз после запуска всех тестов класса.   

setUpModule() (вне класса)
-------------
Вызывается один раз перед всеми классами, которые есть в файле. 

tearDownModule() (вне класса)
----------------
Вызывается один раз после всех классов, которые есть в файле.

"""

import os
import sys
import unittest

# Добавим возможность импорта из директории code в наш тест 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR_PATH = os.path.join(BASE_DIR, 'data_sprint5') 
sys.path.append(CODE_DIR_PATH)

# импортируем класс MadCalculator из другого файла
from data_sprint5 import sprint5_data_unittest01 as data


class TestCalc(unittest.TestCase):     
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """
        Подготовим данные к тесту. 
        Вызывается единоразово перед запуском всех тестов класса.
        """
        # это и есть наш Arrange в паттерне ААА
        cls.calc = data.MadCalculator()

    def test_sum_string(self):         
		# sum_string() возвращает конкатенированные строки         
        act = TestCalc.calc.sum_string(1, 100500)         
        self.assertEqual(act, 1100500,
			'Метод sum_string работает неправильно.')      
		
    def test_sum_string_first_negative_value(self):                 
		# Проверяем, что при вызове метода sum_string() с отрицательным числом         
		# в аргументе выбрасывается исключение ValueError         
        self.assertRaises(ValueError, TestCalc.calc.sum_string, -1, 500)      
		
    def test_sum_string_second_negative_value(self):         
		# Можно провести тестирование исключения,         
		# использовав менеджер контекста         
        with self.assertRaises(ValueError):             
            TestCalc.calc.sum_string(1, -100500)      
	
    def test_sum_args(self):         
		# Act - выполнение тестируемого сценария.         
		# Вызываем метод summ         
        act = TestCalc.calc.sum_args(3, -3, 5) 
		         
		# Assert - проверяем, что метод работает         
        self.assertEqual(act, 5, 
			'Метод sum_args работает неправильно.')

