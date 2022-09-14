"""
## Формат ввода

В первой строке записано количество фишек n, 2 ≤ n ≤ 105.
Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

## Формат вывода

Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».

Пример ввода:
6
-9 -7 -6 -1 -1 3
2

Пример вывода:
-1 3
"""

from typing import List, Tuple, Optional

# Первый вариант решения
# оптимизация с отсортированным списком
# ВРЕМЯ: 135ms ПАМЯТЬ: 13.17Mb
# def two_sum(
#     numb_chips: int, points_chips: List[int], numb_wish: int
# ) -> Optional[Tuple[int, int]]:
#     # Сортируем исходный массив стандартной функцией
#     points_chips.sort()
#     left_cursor = 0
#     right_cursor = len(points_chips) - 1
#     while left_cursor < right_cursor:
#         current_sum = points_chips[left_cursor] + points_chips[right_cursor]
#         if current_sum == numb_wish:
#             return points_chips[left_cursor], points_chips[right_cursor]
#         if current_sum < numb_wish:
#             left_cursor += 1
#         else:
#             right_cursor -= 1

# Второй вариант решения
# оптимизация со СТРУКТУРОЙ ДАННЫХ ПОИСКА
# ВРЕМЯ: 115ms ПАМЯТЬ: 14.01Mb
def two_sum(
    numb_chips: int, points_chips: List[int], numb_wish: int
) -> Optional[Tuple[int, int]]:
    previous = set()
    for i in points_chips:
        y = numb_wish - i
        if y in previous:
            return i, y
        else:
            previous.add(i)
    return None


def read_input() -> Tuple[int, List[int], int]:
    numb_chips = int(input())
    points_chips = list(map(int, input().split()))
    numb_wish = int(input())
    return numb_chips, points_chips, numb_wish


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result == None:
        print(None)
    else:
        print(" ".join(list(map(str, result))))


numb_chips, points_chips, numb_wish = read_input()
print_result(two_sum(numb_chips, points_chips, numb_wish))
