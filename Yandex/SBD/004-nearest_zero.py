"""
Тимофей ищет место, чтобы построить себе дом. 
Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка.
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния.
Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, 
в котором строились, поэтому их номера на карте никак не упорядочены. 

Пустые участки обозначены нулями.

## Формат ввода

В первой строке дана длина улицы —– n (1 ≤ n ≤ 106).
В следующей строке записаны n целых неотрицательных чисел — 
номера домов и обозначения пустых участков на карте (нули). 
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

## Формат вывода

Для каждого из участков выведите расстояние до ближайшего нуля.
Числа выводите в одну строку, разделяя их пробелами.

Пример ввода:
5
0 1 4 9 0

Пример вывода:
0 1 2 1 0
"""

from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    numb_count = int(input())
    numb_house = list(map(int, input().split()))
    return numb_count, numb_house


def print_result(result: List[int]) -> None:
    print(" ".join(list(map(str, result))))


def nearest_zero(numb_house: List[int], numb_count: int) -> List[int]:
    output = [0] * len(numb_house)
    zero_index = [
        index for index, value in enumerate(numb_house) if value == 0
    ]
    for index in range(zero_index[0]):
        output[index] = zero_index[0] - index
    for index in range(len(zero_index) - 1):
        for position in range(zero_index[index] + 1, zero_index[index + 1]):
            output[position] = min(
                position - zero_index[index], zero_index[index + 1] - position
            )
    for index in range(zero_index[-1] + 1, len(numb_house)):
        output[index] = index - zero_index[-1]
    return output


if __name__ == "__main__":
    numb_count, numb_house = read_input()
    print_result(nearest_zero(numb_house, numb_count))
