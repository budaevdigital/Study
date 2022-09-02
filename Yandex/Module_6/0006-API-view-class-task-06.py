"""
Задача 
--------
Опишите код класса APIPostDetail(), наследующегося от APIView.

Этот класс должен обрабатывать запросы GET, PUT, PATCH и DELETE: 
возвращать, изменять или удалять отдельный объект модели Post.

В файл urls.py добавьте эндпоинт api/v1/posts/<int:pk>/, 
который будет вызывать view-класс APIPostDetail().

Подсказка
---------
Опишите методы get(), put(), patch() и delete().
Не забудьте импортировать в urls.py класс APIPostDetail().
"""

# ------------------------------------------
# views.py
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class APIPost(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer =  PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIPostDetail(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        # найдем единственно-нужный пост
        post = Post.objects.get(pk=pk)
        # передадим его в сериализатор с параметром partial=True, чтобы 
        # изменить не все значения в модели в БД, а только указанные 
        # в request.data
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(staus=status.HTTP_204_NO_CONTENT)

# ------------------------------------------
# urls.py
from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/posts/', views.APIPost.as_view()),
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
