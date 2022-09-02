'''
## Формат ввода

В первой строке записано количество фишек N, 2 ≤ N ≤ 104.
Во второй строке записано points_chips целых чисел —– очки на фишках Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число numb_wish, -105 ≤ numb_wish ≤ 105.

## Формат вывода

Нужно вывести два числа —– очки на двух фишках, в сумме дающие numb_wish.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».

Пример ввода:
6
-1 -1 -9 -7 3 -6
2

Пример вывода:
-1 3
'''
from typing import List, Tuple, Union


def two_sum(numb_chips: int, points_chips: List[int], numb_wish: int) -> Union[List[int], None]:
	for i in range(0, numb_chips):
		for j in range(i+1, numb_chips):
			if points_chips[i] + points_chips[j] == numb_wish:
				return points_chips[i], points_chips[j]
	return None, None

def read_input() -> Tuple[int, List[int], int]:
	numb_chips = int(input())
	points_chips = list(map(int, input().split())) 
	numb_wish = int(input())
	return numb_chips, points_chips, numb_wish

numb_chips, points_chips, numb_wish = read_input()

print(" ".join(list(map(str, two_sum(numb_chips, points_chips, numb_wish)))))