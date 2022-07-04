"""
Задача
-------
В проекте Yatube ограничьте число запросов к API на уровне проекта:
для анонимных пользователей — не более десяти в минуту;
для аутентифицированных пользователей — не более ста в минуту.

Подсказка
---------
В файле настроек проекта settings.py добавьте ключи DEFAULT_THROTTLE_CLASSES 
и DEFAULT_THROTTLE_RATES с необходимыми параметрами в словарь REST_FRAMEWORK.
"""

# ------------------------------------------
# settings.py
# Ограничения на уровне проекта
REST_FRAMEWORK = {     
	'DEFAULT_THROTTLE_CLASSES': [         
		'rest_framework.throttling.UserRateThrottle',         
		'rest_framework.throttling.AnonRateThrottle',     
	],
    # период времени указывается как `second`, `minute`, `hour` или `day`
	'DEFAULT_THROTTLE_RATES': {         
		'user': '100/minute',  
		# Лимит для UserRateThrottle         
		'anon': '10/minute',  
		# Лимит для AnonRateThrottle     
	} 
}
