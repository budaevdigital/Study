from typing import List

dict_test = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"},
    {"key3": "value2"},
    {"key1": "value1"},
]


# Проходим циклом с конца (чтобы алгоритм оставил только первое упоминание)
# Удаляем элемент из словаря, если у него есть дубль
def delete_dublicat_item_from_end(sample: List[dict]) -> List[dict]:
    count = len(sample) - 1
    while count != 0:
        if sample[count] in sample[0:count]:
            del sample[count]
        count -= 1
    return sample


# Создаём новый массив с помощью включения в последовательность (comprehension), делаем преобразование
# ко множеству, но для этого нужен такой же хешируемый тип, как и dict (сам set не является хешируемым)
# поэтому выбран frozenset. Единственное - он неизменяемый и нужно обратное преобразование в List
def set_comprehension_with_frozenset(sample: List[dict]) -> List[dict]:
    return list({frozenset(index.items()): index for index in sample}.values())


# Почти то же самое, как и верхняя функция, но со списковым включением (comprehension)
# и с enumerate - нужен для возврата индекса, для итерация по словарю в цикле
def list_comprehension_with_enumerate(sample: List[dict]) -> List[dict]:
    return [
        value
        for index, value in enumerate(sample)
        if value not in sample[index + 1 :]
    ]


if __name__ == "__main__":
    # Создаём копии массива
    dict_test1 = dict_test.copy()
    dict_test2 = dict_test.copy()
    dict_test3 = dict_test.copy()
    print("RAW:", dict_test)

    print("1) ", delete_dublicat_item_from_end(dict_test1))
    print("2) ", set_comprehension_with_frozenset(dict_test2))
    print("3) ", list_comprehension_with_enumerate(dict_test3))
