"""
Гоша любит играть в игру «Подпоследовательность»: даны 2 строки,
и нужно понять, является ли первая из них подпоследовательностью второй.
Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос,
просто посмотрев на них.

Помогите Гоше написать функцию, которая решает эту задачу.

Формат ввода:
В первой строке записана строка s.
Во второй —- строка t.
Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000.
Строки не могут быть пустыми.

Формат вывода:
Выведите True, если s является подпоследовательностью t, иначе —– False.

Пример 1

Ввод
abc
ahbgdcu

Вывод
True

Пример 2

Ввод
abcp
ahpc

Вывод
False
"""
from typing import Tuple


def input_string() -> Tuple[str, str]:
    first_str = input()
    second_str = input()
    return first_str, second_str


def search_subsequence(first_str: str, second_str: str):
    """
    Находит подпоследовательность и возвращает True - если найдена и False - если нет


    >>> search_subsequence('abc', 'ahbgdcu')
    True

    >>> search_subsequence('abcp', 'ahpc')
    False
    """

    for index_one in range(0, len(first_str)):
        if (
            first_str[index_one]
            in second_str[index_one : int(len(second_str))]
        ):
            continue
        else:
            return False
    return True


def main():
    first_str, second_str = input_string()
    result = search_subsequence(first_str, second_str)
    print(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
