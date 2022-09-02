"""
Задача
--------
Напишите view-функцию api_posts_detail(), которая обрабатывает запросы GET, PUT, PATCH и DELETE: 
возвращает, перезаписывает, изменяет или удаляет объект модели Post по его id.

В файл urls.py добавьте эндпоинт api/v1/posts/<int:pk>/, который должен вызывать view-функцию api_posts_detail().

Подсказка
---------
Для удаления объекта используйте его метод delete(), остальное вы уже делали.
При удалении объекта сериализация не используется.

В urls.py импортируйте view-функцию api_posts_detail().
Используйте параметр partial, чтобы разрешить частичные обновления.
"""

# ------------------------------------------
# views.py
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import Post
from rest_framework import status


@api_view(['GET', 'POST'])
def api_posts(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_posts_detail(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = PostSerializer(post)
    return Response(serializer.data)

# ------------------------------------------
# urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/posts/', views.api_posts),
    path('api/v1/posts/<int:pk>/', views.api_posts_detail),
]

# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post
