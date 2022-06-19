"""
Задача
------
Напишите на основе дженериков два view-класса: APIPostList и APIPostDetail.

Опишите два эндпоинта:
 - api/v1/posts/,
 - api/v1/posts/<pk>/.

Через эти эндпоинты должны быть доступны любые операции с моделью Post:
 - POST-запрос на api/v1/posts/ создаст новую запись.
 - Запросы PUT, PATCH или DELETE к адресу api/v1/posts/<pk>/ удалят или изменят существующую запись.
 - GET-запрос на те же адреса вернёт список объектов или один объект.

Подсказка
----------
Для каждого класса пропишите queryset и serializer_class.
"""


# ------------------------------------------
# views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class APIPostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# ------------------------------------------
# urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/posts/', views.APIPostList.as_view()),
    path('api/v1/posts/<int:pk>', views.APIPostDetail.as_view()),
]

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post
