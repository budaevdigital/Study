"""
## Ограниченная очередь
Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size,
означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди.
Функции, которые надо поддержать, описаны в формате ввода.


## Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.

Далее идут команды по одной на строке. Команды могут быть следующих видов:
    - push(x) — добавить число x в очередь;
    - pop() — удалить число из очереди и вывести на печать;
    - peek() — напечатать первое число в очереди;
    - size() — вернуть размер очереди;

При превышении допустимого размера очереди нужно вывести «error».

При вызове операций pop() или peek() для пустой очереди нужно вывести «None».

## Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке

Пример ввода:
12
2
push -34
push -23
push 8
peek
size
pop
size
peek
pop
pop
push 80
size

Пример вывода:
error
-34
2
-34
1
-23
-23
None
1
"""
from typing import List


class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size_queue = 0

    def push(self, object):
        if self.size() >= self.max_size:
            return "error"
        self.queue[self.tail] = object
        self.tail = (self.tail + 1) % self.max_size
        self.size_queue += 1

    def pop(self):
        if self.isEmpty():
            return "None"
        current_position = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_queue -= 1
        return current_position

    def peek(self):
        if self.isEmpty():
            return "None"
        return self.queue[self.head]

    def size(self):
        return self.size_queue

    def isEmpty(self):
        return self.size_queue == 0


def read_input() -> List[str]:
    result = []
    count_commands = int(input())
    size_queue = int(input())
    my_queue = MyQueueSized(size_queue)
    for count in range(count_commands):
        command = input().split()
        if command[0] == "push":
            add_queue = my_queue.push(command[1])
            if add_queue == "error":
                result.append("error")
        if command[0] == "pop":
            result.append(my_queue.pop())
        if command[0] == "peek":
            result.append(my_queue.peek())
        if command[0] == "size":
            result.append(my_queue.size())
    return result


def print_result(result: List[str]) -> None:
    for string in result:
        print(string)


if __name__ == "__main__":
    print_result(read_input())
