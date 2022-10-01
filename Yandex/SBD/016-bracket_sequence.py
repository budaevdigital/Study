"""
Генератор скобок
Рита по поручению Тимофея наводит порядок в правильных скобочных последовательностях
(ПСП), состоящих только из круглых скобок ().
Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке —– 
алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.

Помогите Рите —– напишите программу, которая по заданному n выведет все ПСП 
 в нужном порядке.

Рассмотрим второй пример. Надо вывести ПСП из четырёх символов. 

Таких всего две:
(())
()()
(()) идёт раньше ()(), так как первый символ у них одинаковый,
а на второй позиции у первой ПСП стоит (, который идёт раньше ).

Формат ввода
На вход функция принимает n — целое число от 0 до 10.

Формат вывода
Функция должна напечатать все возможные скобочные последовательности заданной
длины в алфавитном (лексикографическом) порядке.

Ввод
3

Вывод
((()))
(()())
(())()
()(())
()()() 

Ввод
2

Вывод
(())
()()
"""
from typing import List, Tuple


def gen_binaty_three_bracket(n, prefix, result, size):
    if len(prefix) == size:
        result.append(prefix)
    else:
        gen_binaty_three_bracket(n-1, prefix + '(', result, size)
        gen_binaty_three_bracket(n-1, prefix + ')', result, size)

def is_true_bracket(string_bracket: str) -> bool:
    while "()" in string_bracket:
        string_bracket = string_bracket.replace("()", "")
    return not string_bracket

def see_correct_bracket(list_bracket: List[str]) -> List[str]:
    correct_bracket = []
    for row in list_bracket:            
        if is_true_bracket(row):
            correct_bracket.append(row)
    return correct_bracket

def read_input() -> Tuple[int,int]: 
    count_bracket = int(input())
    size_string_bracket = count_bracket * 2
    return count_bracket, size_string_bracket

def print_correct_bracket(correct_bracket: List[str]) -> None:
    for row in correct_bracket:
        print(row)

def main():
    generate_bracket = []
    count, size = read_input()
    gen_binaty_three_bracket(count, "", generate_bracket, size)
    print_correct_bracket(see_correct_bracket(generate_bracket))


if __name__ == "__main__":
    main()


