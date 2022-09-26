"""
## Списочная очередь
Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка.
Помогите ему с реализацией.

Очередь должна поддерживать выполнение трёх команд:
    - get() — вывести элемент, находящийся в голове очереди, и удалить его.
        Если очередь пуста, то вывести «error».
    - put(x) — добавить число x в очередь
    - size() — вывести текущий размер очереди

## Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 1000.
В каждой из следующих n строк записаны команды по одной строке.

## Формат вывода
Выведите ответ на каждый запрос по одному в строке.
"""
from typing import List


class QueueList:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next
        
        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size_list = 0

    def get(self):
        if self.isEmpty():
            return 'error'
        result = self.head
        if self.size == 1:
            self.head = self.Node()
            self.tail = self.Node()
            self.size_list -= 1
            return result
        elif self.size == 2:
            self.head = self.tail
            self.size_list -= 1
            return result
        else:
            self.tail.next = self.head
            self.head = self.tail.next.next
            self.size_list -= 1
            return result

    def put(self, set_value):
        if self.isEmpty():
            self.head = self.Node(value=set_value)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=set_value)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.size_list += 1

    def size(self):
        return self.size_list
    
    def isEmpty(self):
        return self.size_list == 0

def read_input() -> List[str]:
    result = []
    count_commands = int(input())
    queue_list = QueueList()
    for count in range(count_commands):
        command = input().split()
        if command[0] == 'put':
            queue_list.put(command[1])
        if command[0] == 'get':
            get_queue = queue_list.get()
            # if get_queue == 'error':
            #     result.append('error')
            result.append(get_queue)
        if command[0] == 'size':
            size_queue = queue_list.size()
            result.append(size_queue)
    return result

def printed_list_queue(results: List[str]) -> None:
    for row in results:
        print(row)


if __name__ == '__main__':
    printed_list_queue(read_input())
