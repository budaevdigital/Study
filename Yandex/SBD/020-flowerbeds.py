"""
Клумбы
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам
На схеме земельного участка клумбы обозначаются просто горизонтальными
отрезками, лежащими на одной прямой.

Для ландшафтных работ было нанято n садовников.

Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок
или его часть могли быть обработаны сразу несколькими садовниками.
Таким образом, отрезки, обрабатываемые двумя разными садовниками,
сливаются в один. Непрерывный обработанный отрезок затем станет клумбой.
Нужно определить границы будущих клумб.

Рассмотрим примеры.

Пример 1:
Два одинаковых отрезка [7, 8] и [7, 8] сливаются в один, но потом их
накрывает отрезок [6, 10].
Таким образом, имеем две клумбы с координатами [2,3] и [6,10].

Пример 2:
Отрезки [2,3], [3, 4] и [3,4] сольются в один отрезок [2,4].
Отрезок [5,6] ни с кем не объединяется, добавляем его в ответ.

Input format
В первой строке задано количество садовников n. Число садовников не превосходит 100 000.

В следующих n строках через пробел записаны координаты клумб в формате:
start end, где start —– координата начала, end —– координата конца.
Оба числа целые, неотрицательные и не превосходят 107.

start строго меньше, чем end.

Output format
Нужно вывести координаты каждой из получившихся клумб в отдельных строках.
Данные должны выводится в отсортированном порядке —– сначала клумбы
с меньшими координатами, затем —– с бОльшими.

Ввод
4
7 8
7 8
2 3
6 10

Вывод
2 3
6 10

Ввод
4
2 3
5 6
3 4
3 4

Вывод
2 4
5 6


Ввод
6
1 3
3 5
4 6
5 6
2 4
7 10

Вывод
1 6
7 10
"""
from typing import List


def read_input() -> List:
    count_row = int(input())
    result_list = []
    for row in range(count_row):
        result = [int(x) for x in input().split()]
        result_list.append(result)
    return result_list


def merge_sort(array: List) -> List:
    """
    Сортирует массив по возрастанию
    >>> merge_sort([[7, 8], [7, 8], [2, 3], [6, 10]])
    [[2, 3], [6, 10], [7, 8], [7, 8]]

    >>> merge_sort([[2, 3], [5, 6], [3, 4], [3, 4]])
    [[2, 3], [3, 4], [3, 4], [5, 6]]

    >>> merge_sort([[1, 3], [3, 5], [4, 6], [5, 6], [2, 4], [7, 10]])
    [[1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [7, 10]]
    """
    if len(array) == 1:
        return array
    left = merge_sort(array[0:int(len(array)/2)])
    right = merge_sort(array[int(len(array)/2):len(array)])
    result = [0] * len(array)
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1
    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result


def search_flowerbed(sorted_array: List) -> List:
    """
    Находит клумбы в списке и заполняет NoneType ненужные участки

    >>> search_flowerbed([[2, 3], [6, 10], [7, 8], [7, 8]])
    [[2, 3], [], [], [6, 10]]

    >>> search_flowerbed([[2, 3], [3, 4], [3, 4], [5, 6]])
    [[], [], [2, 4], [5, 6]]

    >>> search_flowerbed([[1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [7, 10]])
    [[], [], [], [], [1, 6], [7, 10]]
    """
    left_pos = 0
    right_pos = 1
    for index in range(len(sorted_array)-1):
        if sorted_array[index+1][left_pos] <= sorted_array[index][right_pos]:
            # True, если правая часть меньше, чем правая часть в следующем индексе
            temp = sorted_array[index][right_pos] < sorted_array[index+1][right_pos]
            sorted_array[index+1][left_pos] = sorted_array[index][left_pos]
            sorted_array[index +
                         1][right_pos] = sorted_array[index+temp][right_pos]
            sorted_array[index] = []
    return sorted_array


def print_result(result: List):
    for index in range(len(result)):
        if result[index]:
            # Если строка в списке не пуста,
            # передаёт все числа в индексе и печатает их
            print(*result[index])


def main():
    array = read_input()
    sorted_array = merge_sort(array)
    result = search_flowerbed(sorted_array)
    print_result(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
