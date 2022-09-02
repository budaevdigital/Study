"""
Задача
---------
Досье Люка Скайуокера на экране. В этом досье упоминается его родная планета.
Сделайте новый запрос к SWAPI и распечатайте на экран данные о диаметре его планеты.

Подсказка
----------
URL ресурса, в котором хранится информация о его родной планете,
содержится в досье Люка под ключом homeworld. 
Сделайте запрос к этому адресу и извлеките из ответа информацию о диаметре планеты.

"""

import requests
from pprint import pprint

# Ищем Люка и его родную планету
search_name = 'Luke'
response_for_search = requests.get(f'https://swapi.tech/api/people/?name={search_name}').json()
homeword_planet_url = str(response_for_search.get('result')[0].get('properties').get('homeworld'))
# Собираем информацию о его планете
response_for_planet_detail = requests.get(homeword_planet_url).json()
name_planet = response_for_planet_detail.get('result').get('properties').get('name')
diameter_planet = int(response_for_planet_detail.get('result').get('properties').get('diameter'))

pprint(f'Диаметр планеты {name_planet}, равен: {diameter_planet} км.')