"""
Комбинации
На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв.

Примерно так:
2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона,
без учета повторов.

Напечатайте все комбинации букв, которые можно набрать
такой последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.

Ввод
23

Вывод
ad ae af bd be bf cd ce cf

Ввод
92

Вывод
wa wb wc xa xb xc ya yb yc za zb zc
"""
from typing import List


def read_input() -> List[str]:
    arr_numbers = input("Введите числовую последовательность клавиш: ")
    return arr_numbers


def recursion_digits(digits, index, result):
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    if len(digits) == 0:
        result.append(index)
    else:
        for letter in letters[digits[0]]:
            recursion_digits(digits[1:], index + letter, result)


def main():
    result = []
    digits = read_input()
    recursion_digits(digits, "", result)
    print(" ".join(result))


if __name__ == "__main__":
    main()
