"""
Задание 
-------
Напишите тест на функцию bubble_sort(), которая сортирует 
полученный список по возрастанию.

Проверьте работу функции:
    - С несортированным списком чисел, состоящим из int и float.
    - С пустым списком.

Подсказка
---------
Несортированный список может быть любым. Например,
[1, 3, 2.5] или [1, -3, 10, 2.5].
Сортированный пустой список — это пустой список.

Запуск
-------
python3 -m unittest -v 0006-unittest-task-01.py
"""

import unittest
from typing import List


class TestBubbleSort(unittest.TestCase):
    """Тестируем bubble_sort."""
    def test_int_float(self):
        # С несортированым списком чисел
        call = bubble_sort([3, 4.4, 2.4, 1, -3, -2.4])
        result = [-3, -2.4, 1, 2.4, 3, 4.4] 
        self.assertEqual(call, result,
            f'Функция {self=} не работает со списком чисел (int и float)')

    def test_empty(self):
        # С пустым списком
        call = bubble_sort([])
        result = []
        self.assertEqual(call, result,
            f'Функция {self=} не работает с пустым списком')


def bubble_sort(array: List[float]) -> List[float]:
    """Сортировка списка методом пузырька по возрастанию."""
    length = len(array)
    for bypass in range(1, length):
        for k in range(0, length - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array


if __name__ == '__main__':     
	unittest.main()
