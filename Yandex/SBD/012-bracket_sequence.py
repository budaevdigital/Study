"""
Скобочная последовательность
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно популярная.

Дана скобочная последовательность.
Нужно определить, правильная ли она.

Будем придерживаться такого определения:
    - пустая строка —– правильная скобочная последовательность;
    - правильная скобочная последовательность, взятая в скобки одного
        типа, –— правильная скобочная последовательность;
    - правильная скобочная последовательность с приписанной слева или справа правильной
        скобочной последовательностью —– тоже правильная.

На вход подаётся последовательность из скобок трёх видов: [], (), {}.

Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная, а иначе False.

## Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность.
Скобки записаны подряд, без пробелов.

## Формат вывода
Выведите «True» или «False».


Пример ввода:	
{[()]}

Пример вывода:
True


Пример ввода:	
()

Пример вывода:
True
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return "error"
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []


def read_input() -> str:
    result = input()
    return result


def is_correct_bracket_seq(string_sequence: str) -> bool:
    correct_sequence = {"[": "]", "{": "}", "(": ")"}
    stack_sequence = Stack()
    # Отлавливаем вариант, когда последовательность не полная
    if (len(string_sequence) % 2) != 0 or len(string_sequence) == 0:
        return False
    for char in string_sequence:
        # Содержттся ли переданный символ в correct_sequence
        if char in correct_sequence.keys():
            stack_sequence.push(char)
        # Если не пустой и value correct_sequence равен char в цикле
        elif (
            not stack_sequence.isEmpty()
            and correct_sequence[stack_sequence.peek()] == char
        ):
            stack_sequence.pop()
    if stack_sequence.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_correct_bracket_seq(read_input()))
