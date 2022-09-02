"""
Задача
------
Измените используемую по умолчанию структуру ответа при пагинации. 
Уберите поля next и previous из выдачи, а название ключа results измените на response.

Создайте файл pagination.py в директории приложения api 
и опишите в нём собственный пагинатор-класс CustomPagination.

Подсказка
---------
Чтобы создать файл в тренажёре — нажмите правой кнопкой мыши на ту директорию, 
в которой он должен появиться.

В классе CustomPagination переопределите метод get_paginated_response 
и уберите поля next и previous из выдачи. Название ключа results измените на response.

Подключите класс CustomPagination для пагинации на уровне проекта.
Теория урока и примеры из официальной документации помогут вам выполнить задание.
"""

# ------------------------------------------
# pagination.py
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'response': data
        })


# ------------------------------------------
# views.py
from .pagination import CatsPagination  


class PostViewSet(viewsets.ModelViewSet):     
	queryset = Post.objects.all()     
	serializer_class = PostSerializer     
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)     
	# Вот он наш собственный класс пагинации
	pagination_class = CustomPagination