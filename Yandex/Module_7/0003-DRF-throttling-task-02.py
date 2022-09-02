"""
Задача
------
Запретите любые запросы к публикациям в обеденное время (с 13:00 до 14:00). 
Опишите в приложении api тротлинг-класс LunchBreakThrottle 
и подключите его к соответствующему view-классу публикаций.

Подсказка
---------
Вам потребуется библиотека datetime. Посмотрите документацию, это поможет.
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

# ------------------------------------------
# throttling.py
from rest_framework import throttling
import datetime


class LunchBreakThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 13 and now <= 14:
            return False
        return True

# ------------------------------------------
# views.py
from .throttling import LunchBreakThrottle


class ViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Если кастомный тротлинг-класс вернёт True - запросы будут обработаны     
    # Если он вернёт False - все запросы будут отклонены     
    throttle_classes = (LunchBreakThrottle, )
    permission_classes = (OwnerOrReadOnly, )