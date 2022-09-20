"""
Нелюбимое дело

Вася размышляет, что ему можно не делать из того списка дел, который он составил.
Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером.
Список дел представлен в виде односвязного списка.
Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого дела и
возвращает голову обновлённого списка.

## Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля).
Список содержит не более 5000 элементов.
Список не бывает пустым.      

## Формат вывода
Верните голову списка, в котором удален нужный элемент.
"""


class Node:
    def __init__(self, value: str | None, next=None) -> None:
        self.value = value
        self.next = next


def printed_linked_list(nodes: Node):
    while nodes:
        print(nodes.value, end="\n")
        nodes = nodes.next


def solution(nodes, index):
    def get_node_by_index(nodes, index):
        while index:
            nodes = nodes.next
            index -= 1
        return nodes

    if index == 0:
        nodes = nodes.next
    else:
        previous = get_node_by_index(nodes, index - 1)
        new_node = get_node_by_index(nodes, index + 1)
        previous.next = new_node
    return nodes


if __name__ == "__main__":
    node_3 = Node("Four task")
    node_2 = Node("Three task", node_3)
    node_1 = Node("Second task", node_2)
    node_0 = Node("First task", node_1)
    new_head = solution(node_0, 1)
    printed_linked_list(new_head)
