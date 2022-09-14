"""
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t, игрок должен одновременно нажать на все клавиши, на которых написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.

## Формат ввода

В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке.
Каждый символ —– либо точка, либо цифра от 1 до 9.  
Символы одной строки идут подряд и не разделены пробелами.

## Формат вывода

Выведите единственное число –— максимальное количество баллов,
которое смогут набрать Гоша и Тимофей.

Пример ввода:
3
1231
2..2
2..2
2..2

Пример вывода:
2
"""
from typing import Tuple

def read_input() -> Tuple[int, str]:
    numb_time = int(input())
    numb_massive = ''.join([input() for i in range(4)])
    return numb_time, numb_massive

def print_result(result: int) -> None:
    print(result)

def calculate_result(numb_massive: str, numb_time: int) -> int:
    numbers = []
    for i in range(1, 10):
        count = numb_massive.count(str(i))
        numbers.append(count)
    scores = len([
        element for element in numbers if 0 < int(element) <= numb_time * 2
    ])
    return scores

if __name__ == '__main__':  
    numb_time, numb_massive = read_input()
    print_result(calculate_result(numb_massive, numb_time))
