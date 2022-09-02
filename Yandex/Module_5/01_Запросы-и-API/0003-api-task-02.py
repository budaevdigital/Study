"""
Задача
---------
Вся галактика ищет Люка Скайуокера.
Опередите конкурентов: найдите его через API и напечатайте в терминале информацию о нём.
SWAPI предоставляет возможность поиска по ресурсам: 
в документации описан GET-параметр, с помощью которого можно 
сделать запрос и найти нужного персонажа по его имени. 

Вам нужен 'Luke'.

Подсказка
----------
Сделайте GET-запрос к адресу https://www.swapi.tech/api/people с GET-параметром name, равным 'luke'.

Из документации
--------------
Searching
All resources support a search parameter that filters the set of resources returned. This allows you to make queries like:
https://www.swapi.tech/api/people/?name=r2
"""

import requests
from pprint import pprint

search_name = 'Luke'
response = requests.get(f'https://swapi.tech/api/people/?name={search_name}').json()
pprint(response.get('result'))