"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке.
Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None.
При этом push(x) и pop() также должны выполняться за константное время.

## Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000.
Далее идут команды по одной в строке.

Команды могут быть следующих видов:
    - push(x) — добавить число x в стек;
    - pop() — удалить число с вершины стека;
    - get_max() — напечатать максимальное число в стеке;

Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».

## Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».

Пример ввода:
10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max

Пример вывода:
error
error
4
None


Пример ввода:
10
get_max
push -6
pop
pop
get_max
push 2
get_max
pop
push -2
push -6

Пример вывода:
None
error
None
2
"""
from typing import List


class StackMaxEffective:
    def __init__(self) -> None:
        self.items = []
        self.max_item = []

    def push(self, item) -> None:
        if len(self.items) == 0 or item > self.max_item[len(self.items) - 1]:
            self.max_item.append(item)
        else:
            self.max_item.append(self.max_item[len(self.items) - 1])
        self.items.append(item)

    def pop(self) -> str | None:
        if self.isEmpty():
            return "error"
        self.max_item.pop()
        self.items.pop()

    def get_max(self) -> str:
        if self.isEmpty():
            return "None"
        return self.max_item[len(self.items) - 1]

    def isEmpty(self) -> bool:
        return self.items == []


def read_input() -> List[str]:
    result = []
    stack = StackMaxEffective()
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
