"""
Задача
------
Подключите к API Yatube стандартную постраничную пагинацию на уровне проекта. 
Пусть API возвращает по 10 объектов на страницу.

Подсказка
---------
Добавьте два параметра в словарь настроек проекта REST_FRAMEWORK .
"""

# ------------------------------------------
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}