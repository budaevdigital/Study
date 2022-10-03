"""
Чтобы выбрать самый лучший алгоритм для решения задачи,
Гоша продолжил изучать разные сортировки.
На очереди сортировка пузырьком — https://ru.wikipedia.org/wiki/Сортировка_пузырьком

Её алгоритм следующий (сортируем по неубыванию):

На каждой итерации проходим по массиву, поочередно сравнивая пары соседних элементов.
Если элемент на позиции i больше элемента на позиции i + 1, меняем их местами.
После первой итерации самый большой элемент всплывёт в конце массива.

Проходим по массиву, выполняя указанные действия до тех пор, пока на очередной
итерации не окажется, что обмены больше не нужны, то есть массив уже отсортирован.
После не более чем n – 1 итераций выполнение алгоритма заканчивается, так как
на каждой итерации хотя бы один элемент оказывается на правильной позиции.

Помогите Гоше написать код алгоритма.

Формат ввода
В первой строке на вход подаётся натуральное число n — длина массива, 2 ≤ n ≤ 1000.
Во второй строке через пробел записано n целых чисел.
Каждое из чисел по модулю не превосходит 1000.

Обратите внимание, что считывать нужно только 2 строки: значение n и входной массив.

Формат вывода
После каждого прохода по массиву, на котором какие-то элементы меняются местами,
выводите его промежуточное состояние.

Таким образом, если сортировка завершена за k меняющих массив итераций,
то надо вывести k строк по n чисел в каждой — элементы массива после каждой из итераций.
Если массив был изначально отсортирован, то просто выведите его.

Пример сортировки выбором:
def select_sort(A):
    for i in range(len(A)-1):
        for k in range(i+1, len(A)):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]


Ввод	
5
4 3 9 2 1

Вывод
3 4 2 1 9
3 2 1 4 9
2 1 3 4 9
1 2 3 4 9


Ввод	
5
12 8 9 10 11

Вывод
8 9 10 11 12
"""
import random
from typing import List, Tuple
from timer_func import Timer

# Сортировка вставками
# Устойчивая сортировка - сохраняет позиции элементов, относительно друг друга
def insertion_sort(list: List[str]) -> List[str]:
    for index in range(0, len(list)):
        item = list[index]
        numb = index
        while numb > 0 and item < list[numb-1]:
            list[numb] = list[numb-1]
            numb -= 1
        list[numb] = item
        print(list)
    return list

# Пузырьковая сортировка
# Не устойчивая сортировка - НЕ сохраняет позиции элементов, относительно друг друга
def bubble_sort(list: List[int]) -> List[int]:
    for index in range(0, len(list)):
        is_not_sort = False
        for search in range(0, len(list)-1):
            if list[search] > list[search+1]:
                list[search], list[search+1] = list[search+1], list[search]
                is_not_sort = True
        print(list)
        if not is_not_sort:
            return list

def read_input() -> Tuple[int, List[int]]:
    size_list = int(input())
    if size_list < 3:
        list_for_sort = [random.randint(0, 99) for i in range(0, random.randint(5, 10))]
        size_list = len(list_for_sort)
    else:
        list_for_sort = list(map(int, input().split()))
    return size_list, list_for_sort

def main():
    size_list, list_for_sort = read_input()
    t1 = Timer()

    # insertion_sort - Вычисление заняло 0.0034 секунд
    # bubble_sort - Вычисление заняло 0.0103 секунд

    # Для запуска замера времени, раскомментируйте t1
    # t1.start()
    list = insertion_sort(list_for_sort)
    # t1.stop()



if __name__ == "__main__":
    main()