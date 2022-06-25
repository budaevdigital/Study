"""
Задача
-------
Добавьте механизм аутентификации при помощи обычного токена в проект 
Yatube API, реализованный на view-функциях.

Сделайте так, чтобы при создании нового поста через POST-запрос 
в поле author автоматически записывался объект автора по токену.

Вам нужно:
 - Сделать доступ к API только после авторизации; 
    опишите эндпоинт, по которому можно будет получать токен.
 - В сериализаторе настроить поле author в режим «только для чтения».
 - При создании публикации в качестве автора указывать 
    пользователя, полученного из объекта request.user.
 - Разрешить изменение или удаление постов только авторам 
    этих постов, в противном случае возвращать статус 403.
"""

# ------------------------------------------
# views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
def api_posts(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_posts_detail(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)

    if request.user != post.author:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == "POST":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------------
# serizlizers.py
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        read_only_fields = ('author',)
        model = Post
