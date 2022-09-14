"""
Все наоборот
Вася решил запутать маму – делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.

Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову двусвязного
списка и возвращает голову перевёрнутого списка.
Ниже дано описание структуры, которая задаёт вершину списка.

## Формат ввода
Функция принимает на вход единственный аргумент — голову двусвязного списка.
Длина списка не превосходит 1000 элементов. 
Список не бывает пустым.

## Формат вывода
Функция должна вернуть голову развернутого списка.
"""


class DoubleConnectedNode:
    def __init__(self, value: str | None, next=None, previous=None) -> None:
        self.value = value
        self.next = next
        self.previous = previous


def printed_linked_list(nodes: DoubleConnectedNode):
    while nodes:
        print(nodes.value, end="\n")
        nodes = nodes.next


def solution(nodes):
    last = nodes
    pre_last = last.next
    last.next = None
    last.previous = pre_last
    while pre_last is not None:
        pre_last.previous = pre_last.next
        pre_last.next = last
        last = pre_last
        pre_last = pre_last.previous
    return last


if __name__ == "__main__":
    node_3 = DoubleConnectedNode("Four task")
    node_2 = DoubleConnectedNode("Three task", node_3)
    node_1 = DoubleConnectedNode("Second task", node_2)
    node_0 = DoubleConnectedNode("First task", node_1)
    print("\nНормальный двусвязный список:")
    printed_linked_list(node_0)
    flipped_nodes = solution(node_0)
    print("\nПеревернутый двусвязный список:")
    printed_linked_list(flipped_nodes)
