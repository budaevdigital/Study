"""
Полиномиальный хеш
Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей написать функцию, вычисляющую хеш строки s. В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:
h(s) = (s1*a^n-1 + s2*a^n-2 + ... + sn-1*a + sn) mod m

ФОРМАТ ВВОДА
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому считается хеш.

Во второй строке дано число m (1 ≤ m ≤ 10^9) –— модуль.

В третьей строке дана строка s (0 ≤ |s| ≤ 106), состоящая из больших и маленьких латинских букв.

ФОРМАТ ВЫВОДА
Выведите целое неотрицательное число –— хеш заданной строки.

Ввод
123
100003
a

Вывод
97


Ввод
123
100003
hash


Вывод
6080

Ввод
123
100003
HaSH

Вывод
56156
"""
from typing import Tuple


class ErrorSizeBase(Exception):
    """Для отлова ошибок при нарушении допустимого значения (1 ≤ a ≤ 1000)"""


class ErrorSizeModule(Exception):
    """Для отлова ошибок при нарушении допустимого значения (1 ≤ m ≤ 10^9)"""


class ErrorSizeString(Exception):
    """Для отлова ошибок при нарушении допустимого значения (0 ≤ |s| ≤ 106)"""


class ErrorInputValue(Exception):
    """Ошибка введеного типа данных - ожидается число на ввод"""


def read_input() -> Tuple[int, int, str]:
    try:
        base_a = int(input())
        if base_a >= 1000 or base_a <= 0:
            raise ErrorSizeBase(
                "Неверно указано основание для рассчёта хеша. "
                "Введите число в пределах диапозона: от 1 до 1000"
            )
        module_m = int(input())
        if module_m >= 10**9 or module_m <= 0:
            raise ErrorSizeModule(
                "Неверно указан модуль m. Введи значение в пределах от 1 до 109"
            )
        string_s = input()
        if len(string_s) >= 107 or len(string_s) == 0:
            raise ErrorSizeString(
                "Ошибка в строке s! Введите строку в диапозоне: от 0 до 106 символов"
            )
    except ValueError as error:
        raise ErrorInputValue(
            f"Ошибка в {error}. Введен не верный тип переменной. Введите число!"
        )
    return base_a, module_m, string_s


def string_to_hash(base_a: int, module_m: int, string_s: str) -> int:
    """
    Функция для расчёта хеша из строки

    >>> string_to_hash(123,100003,"a")
    97

    >>> string_to_hash(123,100003,"hash")
    6080

    >>> string_to_hash(123,100003,"HaSH")
    56156
    """
    index = 1
    result = 0
    count = len(string_s)
    for s in string_s:
        result += ord(s) * (base_a ** (count - index))
        index += 1
    hash_string = result % module_m
    return hash_string


def main():
    base_a, module_m, string_s = read_input()
    print(string_to_hash(base_a, module_m, string_s))

    assert string_to_hash(123, 100, "haha") != None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
