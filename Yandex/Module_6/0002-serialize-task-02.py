"""
Задача
------
Сериализатор готов, самое время проверить его в работе — отправить запрос и в ответ получить JSON. 
Но для этого необходимо описать маршрут и дописать view-функцию.

При GET-запросе по адресу api/v1/posts/ должна вызываться view-функция get_post(). 
В качестве параметра view-функция должна ожидать переменную pk с целочисленным значением. 

В ответ функция должна возвращать объект публикации по его id.
View-функция get_post() должна возвращать объект JsonResponse. 

Для этого импортируйте класс JsonResponse из модуля django.http 
и передайте в конструктор класса JsonResponse данные из сериализатора.

Подсказка
---------
В urls.py для запросов к адресам вида api/v1/posts/... 
вызовите view-функцию get_post() и передайте в неё целочисленный аргумент pk.

В файле views.py опишите view-функцию get_post(), которая принимает параметр pk.

В теле view-функции нужно получить объект публикации, соответствующий полученному pk.

Объект публикации должен быть передан сериализатору PostSerializer.

View-функция должна вернуть объект JsonResponse с параметром serializer.data.
"""

# serizlizers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('text', 'author', 'pub_date')
        model = Post

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/posts/<int:post_id>/', views.get_post),
]

# views.py
from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializer


def get_post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(pk=post_id)
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
