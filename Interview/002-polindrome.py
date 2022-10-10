from typing import Tuple


class TypeErrorPolindrom(Exception):
    """Для отлова ошибок"""


def resize_string(string: str) -> Tuple[str, str]:
    if not isinstance(string, str):
        raise TypeErrorPolindrom("Передана не строка. Передайте строчку!")
    one = ""
    two = ""
    try:
        if len(string) % 2 == 0:
            one = string[0 : int(len(string) / 2)]
            two = (string[::-1])[0 : int(len(string) / 2)]
        else:
            one = string[0 : int((len(string) + 1) / 2)]
            two = (string[::-1])[0 : int((len(string) + 1) / 2)]
    except Exception as error:
        print(f"Что-то пошло не так и возникла ошибка {error}")
    return one, two


def is_polindrom(one: str, two: str):
    return one == two


def print_result(is_polindrom: bool):
    """
    Проверяет, является ли строка полиндромом

    >>> print_result(True)
    Строка полиндром

    >>> print_result(False)
    Строка НЕ полиндром
    """
    if is_polindrom:
        print("Строка полиндром")
    else:
        print("Строка НЕ полиндром")


def main():
    assert resize_string("adsda") == (
        "ads",
        "ads",
    ), "Ошибка в функции resize_string"
    assert is_polindrom("ads", "ads") == True, "Ошибка в сравнении строк"

    words = ["попоп", "воробей", "берег", "аса", "AdЫdA"]
    for row in words:
        one_strint, two_string = resize_string(row)
        print_result(is_polindrom(one_strint, two_string))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
