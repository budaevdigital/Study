"""
Васе нужно распечатать свой список дел на сегодня. 

Напишите функцию, которая печатает все его дела. 
Известно, что дел у Васи не больше 5000.

Внимание: 
в этой задаче не нужно считывать входные данные. 
Нужно написать только функцию, которая принимает на вход голову списка и печатает его элементы.
Ниже дано описание структуры, которая задаёт узел списка. Используйте компилятор Make.

## Формат ввода
В качестве ответа сдайте только код функции, которая печатает элементы списка. 
Длина списка не превосходит  5000 элементов. Список не бывает пустым.

## Формат вывода
Функция должна напечатать элементы списка по одному в строке.
"""


class Node:
    def __init__(self, value: str | None, next=None) -> None:
        self.value = value
        self.next = next

def printed_linked_list(nodes: Node):
    while nodes:
        print(nodes.value, end='\n')
        nodes = nodes.next

def create_list_task() -> Node:
    node_3 = Node('Four task')
    node_2 = Node('Three task', node_3)
    node_1 = Node('Second task', node_2)    
    node_0 = Node('First task', node_1)
    return node_0, node_1, node_2, node_3

if __name__ == '__main__':
    node_0, node_1, node_2, node_3 = create_list_task()
    printed_linked_list(node_2)