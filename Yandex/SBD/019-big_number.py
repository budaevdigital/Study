"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. 
Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.


Ввод	
3
15 56 2

Вывод
56215

Ввод	
3
1 783 2

Вывод
78321

Ввод	
5
2 4 5 2 10

Вывод
542210
"""
from re import X
from typing import List, Tuple

class SizeArrayError(Exception):
    """Только для отлова исключений, в случае некорректного размера массива"""


def reading_input() -> Tuple[int, List[int]]:
    count_numbers = int(input())
    numbers_array = list(map(int, input().split(" ")))
    return count_numbers, numbers_array

def return_first_number(number: int) -> int:
    string = str(number)
    return int(string[0])

def compare_numbers(numb_one: int, numb_two: int) -> bool:
    return return_first_number(numb_one) > return_first_number(numb_two) 

def insertion_sort_by_comparator(array: List[int], count_numbers: int) -> List[int]:
    """
    Функция, которая возвращает массив нужной последовательности

    >>> insertion_sort_by_comparator([15, 56, 2], 3)
    [56, 2, 15]

    >>> insertion_sort_by_comparator([1, 783, 2], 3)
    [783, 2, 1]

    >>> insertion_sort_by_comparator([2, 4, 5, 2, 10], 5)
    [5, 4, 2, 2, 10]
    """
	      
    if count_numbers != len(array):
        raise SizeArrayError(
            "Указан неверный размер массива. Введите правильные данные"
        )
    for i in range(0, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and compare_numbers(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return array

def print_result(array: List[int]):
    string = "".join(map(str, array))
    print(string)

def main():
    count_numbers, numbers_array = reading_input()
    sort_array = insertion_sort_by_comparator(numbers_array, count_numbers)
    print_result(sort_array)


if __name__ == "__main__":
    # Небольшое тестирование функции алгоритма c doctest,
    # который протестируется перед запуском.
    # Либо запустить 'python3 -m doctest <название файла.py>'
    import doctest
    doctest.testmod()
    main()