"""
Задание
-------
Допишите тестирующую функцию test_sort(). 
Она должна проверять функции, сортирующие списки из чисел 
по возрастанию (от меньшего к большему).
Например, если на вход такая функция получит список 
[1, 3, 2, 4], то вернуть она должна [1, 2, 3, 4].
В прекоде заготовлен вызов тестирования нескольких сортирующих 
функций (эти функции хранятся в пакете ttd_sprint5_data, их код вам не виден).

В тесте проверьте, работают ли эти функции:
со списком, содержащим int и float;
со списком, содержащим отрицательные величины, нулевое значение;
со списком, содержащим одинаковые числа;
с пустым списком (всегда стоит проверять граничные значения).

Часть функций не пройдёт все тесты.
Когда вы обнаружите неработающие функции — удалите из кода строки,
где они вызываются для тестирования. После этого отправляйте код на проверку.

Подсказка
---------
Каждую проверку описывайте в отдельном ассерте, задавая для 
тестируемой функции нужный аргумент и ожидаемый ответ.
"""

from .data_sprint5.sprint5_data_sorting import bubble_sort

def test_sort(sorting_algorithm):
    """ Тестируем алгоритм, сортирующий список по возрастанию."""    
    # Напечатать имя функции
    print(f'Тестируем функцию: {sorting_algorithm.__name__}')

    source = [1, 2.2, 3, 4.4]
    result = [1, 2.2, 3, 4.4]
    # тестируем алгоритм на уже отсортированном списке
    assert sorting_algorithm(source) == result, (
        f'{sorting_algorithm.__name__} не работает с данными {source}')

    source = [1, -1, 2.2, -4, 0 ]
    result = [-4, -1, 0, 1, 2.2]
    # тестирует алгоритм с отрицательными значениями
    assert sorting_algorithm(source) == result, (
        f'{sorting_algorithm.__name__} не корректно работает '
        f'с отрицательными значениями {source}')

    source = [1, 1, 1, 1]
    result = [1, 1, 1, 1]
    # тестирует алгоритм с одинаковыми значениями
    assert sorting_algorithm(source) == result, (
        f'{sorting_algorithm.__name__} не корректно работает '
        f'с одинаковыми значениями {source}')
   
    source = []
    result = []
    # тестирует алгоритм с пустым значением
    assert sorting_algorithm(source) == result, (
        f'{sorting_algorithm.__name__} не корректно работает '
        f'с пустым значением {source=}')


    print(f'Тест для {sorting_algorithm.__name__} пройден')



# Ипортируем тестируемые функции из пакета ttd_sprint5_data
test_sort(bubble_sort)
# test_sort(ttd_sprint5_data.timsort_sort)
# test_sort(ttd_sprint5_data.selection_sort)
# test_sort(ttd_sprint5_data.insertion_sort)
# test_sort(ttd_sprint5_data.cap_sort) 
# test_sort(ttd_sprint5_data.merge_sort)
# test_sort(ttd_sprint5_data.heap_sort)
# test_sort(ttd_sprint5_data.stepa_sort)  
# test_sort(ttd_sprint5_data.quick_sort)
# test_sort(ttd_sprint5_data.sus_sort)