"""
# Два велосипеда

Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
У Васи есть копилка, в которую каждый день он может добавлять деньги
(если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у
Васи в копилке было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить

первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.

Подсказка: решение должно работать за O(log n).

## Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания.
Каждое из чисел не превосходит 10^6.

В третьей строке записано целое положительное число s — стоимость велосипеда.
Это число не превосходит 10^6.

## Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.

Ввод
6
1 2 4 4 6 8
3

Вывод
3 5

Ввод
6
1 2 4 4 4 4
3

Вывод
3 -1

Ввод
6
1 2 4 4 4 4
10

Вывод
-1 -1
"""
from typing import List, Tuple


def read_input() -> Tuple[int, List[int], int]:
    days = int(input())
    arr_numbers = list(map(int, input().split()))
    cost_bike = int(input())
    return days, arr_numbers, cost_bike


def to_buy_bycycle_binary_search(
    arr_numbers: List[int], cost_bike: int, days_left: int, days_right: int
) -> List[str]:
    if days_right <= days_left:
        return -1
    days_middle = (days_left + days_right) // 2
    if arr_numbers[days_middle] == cost_bike:
        return days_middle
    elif cost_bike < arr_numbers[days_middle]:
        return to_buy_bycycle_binary_search(
            arr_numbers, cost_bike, days_left, days_middle
        )
    else:
        return to_buy_bycycle_binary_search(
            arr_numbers, cost_bike, days_middle + 1, days_right
        )


def find_first_day_to_buy(days: int, arr_numbers: int, cost_bike: int) -> int:
    if cost_bike > arr_numbers[-1]:
        return -1
    if cost_bike in arr_numbers:
        # Проверяем есть ли в массиве данное значение
        # и если есть, возвращаем индекс+1
        return arr_numbers.index(cost_bike) + 1
    # Так же возвращаем индекс+1 = на какой из дней будет совершена покупка
    return (
        to_buy_bycycle_binary_search(
            arr_numbers=arr_numbers,
            cost_bike=cost_bike,
            days_left=0,
            days_right=days,
        ) + 1
    )


def main():
    result = []
    days, arr_numbers, cost_bike = read_input()
    result.append(find_first_day_to_buy(days, arr_numbers, cost_bike))
    result.append(find_first_day_to_buy(days, arr_numbers, (cost_bike * 2)))
    result = " ".join(map(str, result))
    print(result)


if __name__ == "__main__":
    main()
