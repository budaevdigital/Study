"""
Задача
---------
напечатать из кода информацию о десяти персонажах, живущих в далёкой-далёкой галактике.
Сделайте запрос к SWAPI: обратитесь к ресурсу, отвечающему за персонажей вселенной «Звёздных войн».
SWAPI по умолчанию разбивает выдачу: возвращает не все элементы сразу, а частями,
по 10 объектов на запрос. Выведите список персонажей с первой страницы выдачи. 
Будьте внимательны: помимо объектов персонажей в выдаче будет и другая информация, 
её печатать не нужно.

Подсказка
----------
Изучите документацию к сервису SWAPI; 
найдите там ресурс, который связан с персонажами, и сделайте к нему запрос.

В ответе API найдите ключ, под которым содержится список объектов, описывающих персонажей.
По этому ключу получите список объектов персонажей и сохраните этот список в переменную characters.

Из документации
--------------
People - resource is an individual person or character within the Star Wars universe.

/people/ -- get all the people resources
/people/:id/ -- get a specific people resource
"""

import requests
from pprint import pprint

response = requests.get('https://swapi.dev/api/people/').json()
characters = response['results']
pprint(characters)