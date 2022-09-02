import requests
from pprint import pprint  # для красивого вывода в консоль

response = requests.get('https://www.swapi.tech/api/starships/9/')
# Преобразовать JSON-строку в тип данных
# позволит обрабатывать встроенными методами и функциями
# print(response.json()['result']['properties']['name'])  

# А если запросить несуществующий ключ словаря - вернёт ошибку:
# AttributeError: 'dict' object has no attribute 'json'
# print(response.json()['result']['properties']['my_name'])


"""
У словарей Python есть встроенный метод get(), который имеет два параметра:
    - ключ: значение которого нужно получить;
    - значение по-умолчанию: вернёт его, если запрошенного ключа нет в словаре. 
"""
# Если значение по-умолчанию не прописано, когда значения
# по ключу нет, вернёт None 
print(response.json().get('result').get('properties').get('my_name'))

pprint(response)
