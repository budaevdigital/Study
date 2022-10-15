"""
Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового.
После того как вещи других расцветок были убраны,
Рита захотела отсортировать свой новый гардероб по цветам.
Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового.
Помогите Рите справиться с этой задачей.

Примечание: попробуйте решить задачу за один проход по массиву!

ФОРМАТ ВВОДА
В первой строке задано количество предметов в гардеробе:
n –— оно не превосходит 1000000.

Во второй строке даётся массив, в котором указан цвет для каждого предмета.
Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.

ФОРМАТ ВЫВОДА
Нужно вывести в строку через пробел цвета предметов в правильном порядке.

Пример 1
Ввод
7
0 2 1 2 0 0 1

Вывод
0 0 0 1 1 2 2

Пример 2
Ввод
5
2 1 2 0 1

Вывод
0 1 1 2 2

Пример 3
Ввод
6
2 1 1 2 0 2

Вывод
0 1 1 2 2 2
"""
from typing import List, Tuple


class ArraySizeError(Exception):
    """
    Для отлова ошибок несовпадения размера массива
    """


def reading_input() -> Tuple[int, List[int]]:
    size_array = int(input())
    array = list(map(int, input().split()))
    if len(array) != size_array:
        raise ArraySizeError(
            "Неверно задан размер массива. "
            f"Указанно {size_array} позиций, но передан массив другого размера."
        )
    return size_array, array


def counting_sort(array: List[int]) -> List[int]:
    # Заведём заранее известный массив - количество цветов (3 позиции - 0,1,2)
    counted_color = [0] * 3
    # Проёдемся по переданному массиву и посмотрим,
    # сколько раз встречался цвет по индексу "counted_color"
    for value in array:
        counted_color[value] += 1
    # Заведём инкремент для передвижения по массиву, для замены значений
    index = 0
    # Для начала проходим циклом по позициям (j) [0,1,2]
    for j in range(len(counted_color)):
        # Следом определям количество проходов цикла по значениям в counted_color[j]
        for i in range(0, counted_color[j]):
            # Присваиваем значение (j) [0,1,2] массиву
            array[index] = j
            # Сдвигаемся дальше по позиции массива
            index += 1
    return array


def print_array(array: List[int]) -> None:
    print(*array)


def main():
    size_array, array = reading_input()
    result = counting_sort(array)
    print_array(result)


if __name__ == "__main__":
    main()
