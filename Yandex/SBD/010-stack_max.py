"""
Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().

## Формат ввода
В первой строке записано одно число n — количество команд, которое не превосходит 10000.
В следующих n строках идут команды. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;

Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

## Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».

Пример ввода:
8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max

Пример вывода:
None
-2
-2


Пример ввода:
7
get_max
pop
pop
pop
push 10
get_max
push -9

Пример вывода:
None
error
error
error
10
"""
from typing import List


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return "error"
        self.items.pop()

    def get_max(self):
        if self.isEmpty():
            return "None"
        return max(self.items)

    def isEmpty(self):
        return self.items == []


def read_input() -> List[str]:
    result = []
    stack = StackMax()
    count_command = int(input())
    for count in range(count_command):
        command = input().split()
        if command[0] == "push":
            stack.push(command[1])
        if command[0] == "pop":
            if stack.pop() == "error":
                result.append("error")
        if command[0] == "get_max":
            result.append(stack.get_max())
    return result


def print_result(result: List[str]) -> None:
    for string in result:
        print(string)


if __name__ == "__main__":
    print_result(read_input())
